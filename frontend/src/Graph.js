import React, { useEffect, useState } from "react";
import axios from "axios";
import {
    Chart as ChartJS,
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement,
    Title,
    Tooltip,
    Legend
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement,
    Title,
    Tooltip,
    Legend
);

function Graph() {
    const [data, setData] = useState([]);

    useEffect(() => {
        const interval = setInterval(() => {
            axios.get("http://127.0.0.1:5000/stats")
                .then(res => setData(res.data.rewards))
                .catch(err => console.error(err));
        }, 2000);

        return () => clearInterval(interval);
    }, []);

    if (!data.length) return <h3>Loading graph...</h3>;

    return (
        <div style={{ width: 600, margin: "auto" }}>
            <h2> Learning Curve</h2>
            <Line
                data={{
                    labels: data.map((_, i) => i),
                    datasets: [{
                        label: "Reward",
                        data: data,
                        borderColor: "blue",
                        tension: 0.3
                    }]
                }}
            />
        </div>
    );
}

export default Graph;