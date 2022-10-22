import React from "react";
import { MapContainer, TileLayer, useMapEvents, Popup } from "react-leaflet";
import L from "leaflet";
import icon from "./constants";

export default function Maps() {
  function LocationMarker() {
    const map = useMapEvents({
      click: (e) => {
        const { lat, lng } = e.latlng;
        L.marker([lat, lng], { icon }).addTo(map);
        console.log(lat, lng);
      },
    });
    return null;
  }

  return (
    <MapContainer center={[51.505, -0.09]} zoom={13} scrollWheelZoom={false}>
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <LocationMarker />
    </MapContainer>
  );
}
