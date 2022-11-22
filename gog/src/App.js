import { Route, Routes, HashRouter } from 'react-router-dom';

import "./App.css";
import Home from "./screens/Home";
import Search from './screens/Search';
import Result from './screens/Result';


const App = () => {
  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Search" element={<Search />} />
        <Route path="/Result/:distance/:angle/:lat/:lon" element={<Result />} />
      </Routes>
    </HashRouter>
  );
};


export default App;
