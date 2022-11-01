import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Circle } from 'react-leaflet';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';

import "../assets/Result.css";
import Spinner from '../components/Spinner';


function Result(props) {
    const params = useParams();
    const navigate = useNavigate();

    const [pos, setPos] = useState([params.lat, params.lon]);
    const [zoom, _] = useState(10);
    const [item, setItem] = useState([]);
    const [loading, setLoading] = useState(false);

    async function _getItem() {
        await axios.get(
          `http://127.0.0.1:3300/result/${params.distance}/${params.angle}/${params.lat}/${params.lon}`
        ).then(res => {
            setItem(res.data);
            // console.log(res.data);
            setLoading(false);
        });
    }

    useEffect(() => {
        setLoading(true);
        _getItem();
    }, []);

    return (
        <div>
            {
                loading ?
                <Spinner />
                :
                <div>
                    <MapContainer style={{ height: "100vh" }} center={pos} zoom={zoom}>
                        <TileLayer
                            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                            url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
                        />
                        {item.map(e => (
                            <Circle
                                center={[e.lat, e.lon]}
                                pathOptions={{ fillColor: e.color }}
                                radius={e.radius}
                                stroke={false}
                            />
                        ))}
                    </MapContainer>
                    <button onClick={() => navigate(-1)}>Go back</button>
                </div>
            }
        </div>
    )
}


export default Result;
