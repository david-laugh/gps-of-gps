import React, { Component } from 'react';
import { MapContainer, TileLayer, Circle } from 'react-leaflet';
import axios from 'axios';

import { azimuth, haversine } from '../utilities/math.js';
import { getCellData } from '../utilities/cell.js';


class Maps extends Component {
    constructor() {
        super();
        this.state = {
            lat: 48.06869406823506,
            lng: 3.74459769969682,
            zoom: 12,
            color: '#000000',
            data: [],
        };
    }

    async _getData() {
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
        this.setState({data: dots});
    }

    componentDidMount() {
        this._getData();
    }

    componentWillUnmount() {
        //
    }

    render() {
        const position = [this.state.lat, this.state.lng];

        return (
            <div>
                <MapContainer style={{ height: "100vh" }} center={position} zoom={this.state.zoom}>
                    <TileLayer
                        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                        url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
                    />
                    {this.state.data.map(data => (
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
}

export default Maps;
