import React, { Component } from 'react';
import { GoogleMap, LoadScript, MarkerF } from '@react-google-maps/api';


const API_KEY = process.env.REACT_APP_GOOGLE_API_KEY;

const containerStyle = {
  width: '1500px',
  height: '1200px'
};

const center = {
  lat: 37.541,
  lng: 126.986
};

class MyMap extends Component {
  constructor(props){
    super(props);
    this.state = {
      position: {
        lat: 37.541,
        lng: 126.986
      }
    };
    this.mapClickEventHandler = this.mapClickEventHandler.bind(this);
    this.markerOnLoad = this.markerOnLoad.bind(this);
  }

  mapClickEventHandler(e) {
    console.log(e.latLng.lat() + " " + e.latLng.lng());
    this.setState(() => ({
      position: {
        lat : e.latLng.lat(),
        lng : e.latLng.lng()
      }
    }));
  }

  markerOnLoad(marker) {
    console.log('marker: ', marker);
  }

  render() {
    return (
      <LoadScript
        googleMapsApiKey={API_KEY}
      >
        <GoogleMap
          mapContainerStyle={containerStyle}
          center={center}
          zoom={13}
          onClick={this.mapClickEventHandler}
        >
          { /* Child components, such as markers, info windows, etc. */ }
          <MarkerF
            onLoad={this.markerOnLoad}
            position={this.state.position}
          />
        </GoogleMap>
      </LoadScript>
    )
  }
}

export default React.memo(MyMap);
