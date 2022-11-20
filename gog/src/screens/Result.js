import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Circle, Marker, useMapEvents } from 'react-leaflet';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';

import "../assets/Result.css";
import Spinner from '../components/Spinner';
import SideOptionBar from '../components/SideOptionBar';


const REACT_APP_URL = process.env.REACT_APP_URL;

function Result(props) {
    const params = useParams();
    const navigate = useNavigate();

    const [position, setPosition] = useState([params.lat, params.lon]);
    const [zoom, setZoom] = useState(10);
    const [item, setItem] = useState([]);
    const [loading, setLoading] = useState(false);
    const [showMarker, setShowMarker] = useState(true);

    async function _getItem() {
        await axios.get(
          `${REACT_APP_URL}/Result/${params.distance}/${params.angle}/${params.lat}/${params.lon}`
        ).then(res => {
            setItem(res.data);
            // console.log(res.data);
            setLoading(false);
        });
    }

    function LocationMarker() {
        const map = useMapEvents({
            click: (e) => {
                const { lat, lng } = e.latlng;
                setPosition([lat, lng]);
                //console.log(lat, lng);
            }
        });
    }

    function ZoomEvents() {
        const map = useMapEvents({
            zoomend: () => {
                setZoom(map.getZoom());
            },
        });
    }

    useEffect(() => {
        setLoading(true);
        _getItem();
    }, []);

    return (
        <div>
            {
                <form>
                    <div className="wrapper">
                        <div>
                            <MapContainer center={position} zoom={zoom} scrollWheelZoom={false}>
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
                                <ZoomEvents />
                                <LocationMarker />
                                {
                                    showMarker ?
                                    <Marker position={position}/> : <></>
                                }
                            </MapContainer>
                            <button onClick={() => navigate(-1)}>Go back</button>
                            <button onClick={() => setShowMarker(false)}>
                                {
                                    showMarker ? <div>Hide Marker</div> : <div>Show Marker</div>
                                }
                            </button>
                        </div>
                        <SideOptionBar
                            position={position}
                            zoom={zoom}
                        />
                    </div>
                </form>
            }
        </div>
    )
}


export default Result;
