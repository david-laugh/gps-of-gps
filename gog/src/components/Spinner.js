import React from 'react';
import GridLoader  from "react-spinners/GridLoader";


function Spinner(props) {

    return (
        <div
            style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                height: '100vh',
            }}
        >
            <GridLoader
                color={"#7cf9df"}
                size={30}
                margin={30}
                speedMultiplier={1}
            />
        </div>
    )
}


export default Spinner;
