import "./App.css";
import MyMap from "./components/MyMap";
import Home from "./screen/Home";

function App() {
  let component;
  switch (window.location.pathname) {
    case "/":
      component = <MyMap />;
      break;
    case "/home":
      component = <Home />;
      break;
  }
  return (
    <>
      <div>{component}</div>
    </>
  );
}

export default App;
