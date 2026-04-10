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
    const [rewards, setRewards] = useState([]);
    const [steps, setSteps] = useState([]);

    useEffect(() => {
        const interval = setInterval(() => {
            axios.get("http://127.0.0.1:5000/stats")
                .then(res => {
                    setRewards(res.data.rewards);
                    setSteps(res.data.steps);
                })
                .catch(err => console.error(err));
        }, 2000);

        return () => clearInterval(interval);
    }, []);

    if (!rewards.length) return <h3>Loading graph...</h3>;

    return (
        <div style={{ width: 700, margin: "auto" }}>
            <h2>Learning Curve</h2>

            <Line
                data={{
                    labels: steps,   // 🔥 FIXED X-AXIS
                    datasets: [
                        {
                            label: "Reward",
                            data: rewards,
                            borderColor: "blue",
                            tension: 0.3
                        }
                    ]
                }}
                options={{
                    responsive: true,
                    plugins: {
                        legend: { display: true }
                    },
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: "Time Steps"
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: "Reward"
                            }
                        }
                    }
                }}
            />
        </div>
    );
}

export default Graph;