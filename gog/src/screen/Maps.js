import "./Home.css";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";

import L from "leaflet";
import icon from "./constants";

export default function Maps() {
  // function MyComponent() {
  //   const map = useMapEvents({
  //     click: (e) => {
  //       const { lat, lng } = e.latlng;
  //       L.marker([lat, lng], { icon }).addTo(map);
  //     },
  //   });
  //   return null;
  // }
  return (
    <MapContainer center={[51.505, -0.09]} zoom={13} scrollWheelZoom={false}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={[51.505, -0.09]}>
        <Popup>
          A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
      </Marker>
    </MapContainer>
  );
}
