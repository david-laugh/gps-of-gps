import React from 'react';
import { useNavigate } from 'react-router-dom';

import "../assets/Home.css";


function Home() {
    const navigate = useNavigate();

    return (
        <div className="Home">
            <div className="Content">
                <div>GPS OF GPS</div>
                <button
                    type="button"
                    className="Home_btn"
                    onClick={() => navigate("/Search")}
                >
                    START
                </button>
            </div>
        </div>
    );
}


export default Home;
