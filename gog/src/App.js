import { Route, Routes } from 'react-router-dom';

import "./App.css";
import Home from "./screens/Home";
import Maps from './screens/Result';


const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/Result/:distance/:angle" element={<Maps />} />
    </Routes>
  );
};


export default App;
