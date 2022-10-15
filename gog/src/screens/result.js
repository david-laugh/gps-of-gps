import React, { Component } from 'react';
import { MapContainer, TileLayer, Circle } from 'react-leaflet';


class Maps extends Component {
    constructor() {
        super();
        this.state = {
            lat: 37.600381,
            lng: 127.029889,
            zoom: 15,
            color: '#000000',
            data: []
        };
    }

    drawDartMap() {
        const { data } = this.state;
        this.setState({data: [...data, 
            {
                lat: 37.600381,
                lon: 127.029899,
                color: '#FFFF00',
                radius: 200
            },
            {
                lat: 37.600381,
                lon: 127.039879,
                color: '#000000',
                radius: 200
            },
            {
                lat: 37.610381,
                lon: 127.039869,
                color: '#000000',
                radius: 200
            }
        ]
        });
    }

    componentDidMount() {
        this.drawDartMap();
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
