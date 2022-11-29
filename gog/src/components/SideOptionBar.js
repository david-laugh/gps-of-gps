import React, { useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';

import "../assets/Search.css";


function SideOptionBar(props) {
    const navigate = useNavigate();
    const [distance, setDistance] = useState(25);
    const [angle, setAngle] = useState(30);
    const [kmList, setKmList] = useState([5, 10, 15, 20, 25]);
    const [prevZoom, setPrevZoom] = useState(10);

    function handleDistance(e) {
        setDistance(e.target.value);
        // console.log(e.target.value);
    }
    
    function handleAngle(e) {
        setAngle(e.target.value);
        // console.log(e.target.value);
    }
    
    function handleDartSubmit(e, history) {
        e.preventDefault();
        navigate(`/Result/Dart/${distance}/${angle}/${props.position[0]}/${props.position[1]}`);
        // console.log("click");
    }

    function handleCenterSubmit(e, history) {
        e.preventDefault();
        navigate(`/Result/Center/${distance}/${angle}/${props.position[0]}/${props.position[1]}`);
        // console.log("click");
    }

    function handleKmList() {
        if (props.zoom > 13 && prevZoom <= 13) {
            setKmList([1, 2, 3, 4, 5]);
            setPrevZoom(props.zoom);
        }
        if (props.zoom <= 13 && prevZoom > 13) {
            setKmList([5, 10, 15, 20, 25]);
            setPrevZoom(props.zoom);
        }
    }

    useEffect(() => {
        handleKmList();
    });

    return (
        <div>
            <div className="options">
                <div className="coordinate">
                    <div id="coordinate-txt">거리(km)</div>
                    <div id="coordinate">
                        <input
                            type="range"
                            id="temp"
                            name="temp"
                            min={`${kmList[0]}`}
                            max={`${kmList[4]}`}
                            step={`${kmList[1] - kmList[0]}`}
                            list="km"
                            onClick={handleDistance}
                        />
                        <datalist id="km">
                            <option value={`${kmList[0]}km`} label={`${kmList[0]}`}></option>
                            <option value={`${kmList[1]}km`} label={`${kmList[1]}`}></option>
                            <option value={`${kmList[2]}km`} label={`${kmList[2]}`}></option>
                            <option value={`${kmList[3]}km`} label={`${kmList[3]}`}></option>
                            <option value={`${kmList[4]}km`} label={`${kmList[4]}`}></option>
                        </datalist>
                    </div>
                </div>
                <hr />
                <div className="angle">
                    <div id="angle-txt">각도(°)</div>
                    <div id="angle">
                        <div className="degree-angle">
                            <input
                                type="radio"
                                id="30-degree-angle"
                                name="degree-angle"
                                value="30"
                                onChange={handleAngle}
                                defaultChecked
                            ></input>
                            <label for="30-degree-angle">30°</label>
                        </div>
                    </div>
                </div>
                <div className="white-box">
                    <button
                        type="submit"
                        className="btn"
                        onClick={handleDartSubmit}
                    >
                        DartSubmit
                        {props.value}
                    </button>
                    <button
                        type="submit"
                        className="btn"
                        onClick={handleCenterSubmit}
                    >
                        CenterSubmit
                        {props.value}
                    </button>
                </div>
            </div>
        </div>
    )
}


export default SideOptionBar;
