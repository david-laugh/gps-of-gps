import React, { Component } from "react";
import "./Home.css";
import Maps from "./Maps";

class Home extends Component {
  render() {
    return (
      <div className="container">
        <div className="logo">
          <h3 id="logo-txt">GPS OF GPS</h3>
        </div>

        <form>
          <div className="wrapper">
            <div className="maps">
              <Maps></Maps>
            </div>
            <div className="option">
              <div className="coordinate">
                <div id="coordinate-txt">거리(km)</div>
                <div id="coordinate">
                  <input
                    type="range"
                    id="temp"
                    name="temp"
                    min="10"
                    max="50"
                    list="km"
                  />
                  <datalist id="km">
                    <option value="10" label="10"></option>
                    <option value="20" label="20"></option>
                    <option value="30" label="30"></option>
                    <option value="40" label="40"></option>
                    <option value="50" label="50"></option>
                  </datalist>
                </div>
              </div>
              <hr />
              <div className="angle">
                <div id="angle-txt">각도 :</div>
                <div id="angle">
                  <div className="degree-angle">
                    <input
                      type="radio"
                      id="30-degree-angle"
                      name="degree-angle"
                      value="30-degree-angle"
                      checked
                    ></input>
                    <label for="30-degree-angle">30°</label>
                  </div>
                  <div className="degree-angle">
                    <input
                      type="radio"
                      id="60-degree-angle"
                      name="degree-angle"
                      value="60-degree-angle"
                    ></input>
                    <label for="60-degree-angle">60°</label>
                  </div>
                  <div className="degree-angle">
                    <input
                      type="radio"
                      id="90-degree-angle"
                      name="degree-angle"
                      value="90-degree-angle"
                    ></input>
                    <label for="90-degree-angle">90°</label>
                  </div>
                </div>
              </div>
              {/* angle end */}
              <div className="white-box">
                <button type="submit" className="btn">
                  Submit
                </button>
              </div>
            </div>
            {/* option end */}
          </div>
        </form>
      </div>
    );
  }
}
export default React.memo(Home);
