import React from "react";

const MousePosition = ({renders}) => {
    const [mousePosition, setMousePosition] = React.useState({
        x:0,
        y:0,
    })
    React.useEffect(()=>{
        const handleMousePositionChange = (e)=>{
            setMousePosition({
                x:e.clientX,
                y:e.clientY,
            })
        }
        window.addEventListener("mousemove", handleMousePositionChange)
        return()=>{
            window.removeEventListener("mousemove", handleMousePositionChange)
        }
    }, [])
    return renders({mousePosition})
}
const PanelMouseLogger = () =>{
    return(
        <div className="BasicTracker">
            <p>Mouse Position:</p>
            <MousePosition
            renders = {({mousePosition}) => (
                <p>
                    ({mousePosition.x}, {mousePosition.y})
                </p>
            )}         
            />
        </div>

    )
}

const PointMouseLogger = () => {
    return (
      <MousePosition
        renders={({ mousePosition }) => (
          <p>
            ({mousePosition.x}, {mousePosition.y})
          </p>
        )}
      />
    );
  };

  const Mouse =()=>{
    return(
        <div className="App">
            <header className="Header">Little Lemon Restaurant 🍕</header>
            <PanelMouseLogger />
            <PointMouseLogger />
        </div>
    )
  }

export default Mouse