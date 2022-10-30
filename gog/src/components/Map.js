import React, { useState } from "react";
import { MapContainer, TileLayer, useMapEvents, Marker } from "react-leaflet";


function Map() {
    const [position, setPosition] = useState([51.505, -0.09]);

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
        <MapContainer center={[51.505, -0.09]} zoom={13} scrollWheelZoom={false}>
            <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <LocationMarker />
            <Marker position={position}/>
        </MapContainer>
    );
}

export default Map;
