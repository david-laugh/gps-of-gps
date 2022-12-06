import { Route, Routes } from 'react-router-dom';

import "./App.css";
import Home from "./screens/Home";
import Search from './screens/Search';
import ResultDart from './screens/ResultDart';
import ResultCenter from './screens/ResultCenter';


const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/Search" element={<Search />} />
      <Route path="/Result/Dart/:distance/:angle/:lat/:lon" element={<ResultDart />} />
      <Route path="/Result/Center/:distance/:angle/:lat/:lon" element={<ResultCenter />} />
    </Routes>
  );
};


export default App;
