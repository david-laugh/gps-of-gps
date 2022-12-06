import React, { useState } from "react";
import { MapContainer, TileLayer, useMapEvents, Marker } from "react-leaflet";

import SideOptionBar from '../components/SideOptionBar';
import "../assets/Search.css";
// import Map from "../components/Map";


function Search(props){
    const [position, setPosition] = useState([51.505, -0.09]);
    const [zoom, _] = useState(13);

    function LocationMarker() {
        const map = useMapEvents({
            click: (e) => {
                const { lat, lng } = e.latlng;
                setPosition([lat, lng]);
                //console.log(lat, lng);
            }
        });
    }

    return (
        <div className="container">
            <div className="logo">
                <h3 id="logo-txt">GPS OF GPS</h3>
            </div>

            <form>
                <div className="wrapper">
                    <div className="maps">
                        <MapContainer center={[51.505, -0.09]} zoom={zoom} scrollWheelZoom={false}>
                            <TileLayer
                                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            />
                            <LocationMarker />
                            <Marker position={position}/>
                        </MapContainer>
                    </div>
                    <SideOptionBar
                        position={position}
                        zoom={zoom}
                    />
                </div>
            </form>
        </div>
    );
}


export default Search;
