import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Circle } from 'react-leaflet';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';

import "../assets/Result.css";


function Result(props) {
    const params = useParams();
    const navigate = useNavigate();

    const [pos, setPos] = useState([48.06869406823506, 3.74459769969682]);
    const [zoom, _] = useState(12);
    const [data, setData] = useState([]);

    async function _getData() {
        const response = await axios.get(
          `http://127.0.0.1:3300/result/${params.distance}/${params.angle}/37/127`
        );
        const items = response.data;
        setData(items);
    }

    useEffect(()=>{
        _getData();
    },[]);

    return (
        <div>
            <MapContainer style={{ height: "100vh" }} center={pos} zoom={zoom}>
                <TileLayer
                    attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                    url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
                />
                {data.map(data => (
                    <Circle
                        center={[data.lat, data.lon]}
                        pathOptions={{ fillColor: data.color }}
                        radius={data.radius}
                        stroke={false}
                    />
                ))}
            </MapContainer>
            <button onClick={() => navigate(-1)}>Go back</button>
        </div>
    )
}


export default Result;
