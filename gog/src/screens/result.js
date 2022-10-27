import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Circle } from 'react-leaflet';
import axios from 'axios';

import { azimuth, haversine } from '../utilities/math.js';
import { getCellData } from '../utilities/Cell.js';


function Maps(props) {
    const [pos, setPos] = useState([48.06869406823506, 3.74459769969682]);
    const [zoom, _] = useState(12);
    const [color, setColor] = useState('#000000');
    const [data, setData] = useState([]);

    async function _getData() {
        const response = await axios.get(
          'http://127.0.0.1:3300/'
        );
        const dots = [];
        const items = response.data;

        const cellData = getCellData(10, 4);
        for (let j = 0; j < cellData.length; j++) {
            for (let i = 0; i < items.length; i++) {
                let distance = haversine(
                    48.06869406823506, 3.74459769969682,
                    items[i]["lat"], items[i]["lon"]
                );
                let angle = azimuth(
                    48.06869406823506, 3.74459769969682,
                    items[i]["lat"], items[i]["lon"]
                );

                if ( angle < cellData[j][0] && distance < cellData[j][1] ) {
                    if ( cellData[j][2] == -1 ) {
                        dots.push(
                            {
                                lat: items[i]["lat"],
                                lon: items[i]["lon"],
                                color: '#FF0000',
                                radius: 200
                            }
                        );
                    } else {
                        dots.push(
                            {
                                lat: items[i]["lat"],
                                lon: items[i]["lon"],
                                color: '#000000',
                                radius: 200
                            }
                        );
                        items.splice(i, 1);
                    }
                }
            }
        }
        setData(dots);
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
        </div>
    )
}


export default Maps;
