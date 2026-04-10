import React, { useEffect, useState } from "react";
import axios from "axios";

function TrafficSim() {
    const [data, setData] = useState({ ns: 0, ew: 0, signal: 0, reward: 0 });

    useEffect(() => {
        const interval = setInterval(() => {
            axios.get("http://127.0.0.1:5000/step")
                .then(res => setData(res.data))
                .catch(err => console.error(err));
        }, 1000);

        return () => clearInterval(interval);
    }, []);

    const cars = (n) =>
        Array.from({ length: Math.min(n, 10) }).map((_, i) => (
            <div key={i} style={{ width: 15, height: 15, background: "blue", margin: 2 }} />
        ));

    return (
        <div>
            <h2> Intersection</h2>
            <div style={{ display: "flex", justifyContent: "center", gap: "40px" }}>
                <div>
                    <h3>NS</h3>
                    {cars(data.ns)}
                </div>

                <div>
                    <h3>Signal</h3>

                    {/* NS Signal (Top) */}
                    <div style={{
                        width: 50,
                        height: 50,
                        borderRadius: "50%",
                        backgroundColor: data.signal === 0 ? "green" : "red",
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        color: "white",
                        fontWeight: "bold"
                    }}>
                        NS
                    </div>

                    {/* EW Signal (Bottom) */}
                    <div style={{
                        width: 50,
                        height: 50,
                        borderRadius: "50%",
                        backgroundColor: data.signal === 1 ? "green" : "red",
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        color: "white",
                        fontWeight: "bold",
                        marginTop: 10
                    }}>
                        EW
                    </div>
                </div>

                <div>
                    <h3>EW</h3>
                    {cars(data.ew)}
                </div>
            </div>

            <h3>Reward: {data.reward}</h3>
        </div>
    );
}

export default TrafficSim;