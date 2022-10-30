import React, { useState } from "react";
import { MapContainer, TileLayer, useMapEvents, Marker } from "react-leaflet";
import { useNavigate } from 'react-router-dom';

import "../assets/Home.css";
// import Map from "../components/Map";


function Home(props){
    const [distance, setDistance] = useState(50);
    const [angle, setAngle] = useState(30);
    const [position, setPosition] = useState([51.505, -0.09]);
    const navigate = useNavigate();

    function LocationMarker() {
        const map = useMapEvents({
            click: (e) => {
                const { lat, lng } = e.latlng;
                setPosition([lat, lng]);
                //console.log(lat, lng);
            }
        });
    }

    function handleDistance(e) {
        setDistance(e.target.value);
        console.log(e.target.value);
    }
    
    function handleAngle(e) {
        setAngle(e.target.value);
        console.log(e.target.value);
    }
    
    function handleSubmit(e, history) {
        e.preventDefault();
        navigate(`/Result/${distance}/${angle}/${position[0]}/${position[1]}`);
        console.log("click");
    }

    return (
        <div className="container">
            <div className="logo">
                <h3 id="logo-txt">GPS OF GPS</h3>
            </div>

            <form>
                <div className="wrapper">
                    <div className="maps">
                        <MapContainer center={[51.505, -0.09]} zoom={13} scrollWheelZoom={false}>
                            <TileLayer
                                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            />
                            <LocationMarker />
                            <Marker position={position}/>
                        </MapContainer>
                    </div>
                    <div className="options">
                        <div className="coordinate">
                            <div id="coordinate-txt">거리(km)</div>
                            <div id="coordinate">
                                <input
                                    type="range"
                                    id="temp"
                                    name="temp"
                                    min="10"
                                    max="50"
                                    step="10"
                                    list="km"
                                    onClick={handleDistance}
                                />
                                <datalist id="km">
                                    <option value="10km" label="10"></option>
                                    <option value="20km" label="20"></option>
                                    <option value="30km" label="30"></option>
                                    <option value="40km" label="40"></option>
                                    <option value="50km" label="50"></option>
                                </datalist>
                            </div>
                        </div>
                        <hr />
                        <div className="angle">
                            <div id="angle-txt">각도 :</div>
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
                                <div className="degree-angle">
                                    <input
                                    type="radio"
                                    id="60-degree-angle"
                                    name="degree-angle"
                                    value="60"
                                    onChange={handleAngle}
                                    ></input>
                                    <label for="60-degree-angle">60°</label>
                                </div>
                                <div className="degree-angle">
                                    <input
                                    type="radio"
                                    id="90-degree-angle"
                                    name="degree-angle"
                                    value="90"
                                    onChange={handleAngle}
                                    ></input>
                                    <label for="90-degree-angle">90°</label>
                                </div>
                            </div>
                        </div>
                        {/* angle end */}
                        <div className="white-box">
                            <button
                                type="submit"
                                className="btn"
                                onClick={handleSubmit}
                                >
                                    Submit
                                    {props.value}
                            </button>
                        </div>
                    </div>
                    {/* option end */}
                </div>
            </form>
        </div>
    );
}


export default Home;
