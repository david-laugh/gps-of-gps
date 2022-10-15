import { useState } from "react";
import "./Home.css";

// var form = document.querySelector("form");
// var log = document.querySelector("#result");

// form.addEventListener(
//   "submit",
//   function (event) {
//     var data = new FormData(form);
//     var output = "";
//     for (const entry of data) {
//       output = output + entry[0] + "=" + entry[1] + "\r";
//     }
//     log.innerText = output;
//     event.preventDefault();
//   },
//   false
// );

export default function Home() {
  return (
    <div>
      <div className="container">
        <div className="logo">
          <h3 id="logo-txt">GPS OF GPS</h3>
        </div>

        <form>
          <div className="option">
            <div className="coordinate">
              <div id="coordinate-txt">거리(km) :</div>
              <br />
              <input
                type="range"
                id="temp"
                name="temp"
                min="10"
                max="50"
                list="km"
              />
              <datalist id="km">
                <option value="10"></option>
                <option value="20"></option>
                <option value="30"></option>
                <option value="40"></option>
                <option value="50" label="50"></option>
              </datalist>
            </div>
            <div className="angle">
              <div id="angle-txt">각도 :</div>
              <div>
                <input
                  type="radio"
                  id="30-degree-angle"
                  name="degree-angle"
                  value="30-degree-angle"
                  checked
                ></input>
                <label for="30-degree-angle">30</label>
                <input
                  type="radio"
                  id="60-degree-angle"
                  name="degree-angle"
                  value="60-degree-angle"
                ></input>
                <label for="60-degree-angle">60</label>
                <input
                  type="radio"
                  id="90-degree-angle"
                  name="degree-angle"
                  value="90-degree-angle"
                ></input>
                <label for="90-degree-angle">90</label>
              </div>
            </div>
            <div>
              <button type="submit" class="btn">
                Submit
              </button>
            </div>
          </div>
        </form>
        {/* <pre id="result"></pre> */}
      </div>
    </div>
  );
}
