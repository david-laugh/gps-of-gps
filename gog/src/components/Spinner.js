import React, {useState} from 'react';
import GridLoader  from "react-spinners/GridLoader";


function Spinner(props) {
    const [count, setCount] = useState(0);
    const [showCount, setShowCount] = useState(false);

    setInterval(() => {
        setCount(count + 1);
        // if (count > 10 && showCount === false) {
        //     setShowCount(true);
        // }
    }, 1000);

    return (
        <div
            style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                height: '100vh',
            }}
        >
            <div>
                <GridLoader
                    color={"#7cf9df"}
                    size={30}
                    margin={30}
                    speedMultiplier={1}
                />
                <div
                    style={{
                        textAlign: 'center'
                    }}
                >
                    {/*
                        showCount ?
                        <div>Loading... {count}sec...</div>
                        :
                        <div>Loading...</div>
                    */}
                    <div>Loading... {count}sec...</div>
                </div>
            </div>
        </div>
    )
}


export default Spinner;
