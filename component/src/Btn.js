function Btn(props){
    const clickHandle = ()=> console.log("click here to know more")
    return(
        <button onClick ={clickHandle}>
            Click me
        </button>
    )
}



function Mouse(props){
    const clickHandle = ()=> console.log("Mouse over function")
    return(
        <button onMouseOver ={clickHandle}>
            Click me
        </button>
    )
}

function ModeToggler(props){
    let darkModeOn = false;
    const darkMode = <h1>Dark Mode is on</h1>
    const lightMode = <h1>Light Mode is on</h1>

    const handleClick = () => {darkModeOn = !darkModeOn;
    if (darkModeOn == true){
        console.log("dark mode on")
    }else{
        console.log("light mode on")
    }}
    return(
        <div>
            {darkModeOn ? darkMode : lightMode}
            <button onClick = {handleClick}>Click Here</button>
        </div>
    )   
}


function RandomNumber() {

    function handleClick() {
        let randomNum = Math.floor(Math.random() * 3) + 1;
        console.log(randomNum);
        let userInput = prompt('type a number');
        alert(`Computer number: ${randomNum}, Your guess: ${userInput}`);
    }
    
    return (
    <div>
        <h1>Task: Add a button and handle a click event</h1>
        <button onClick={handleClick}>Guess the number between 1 and 3</button>
    </div>
    );
}


const PromoHeading = (props) => {
return(
    <div>
        <h1>{props.heading}</h1>
        <h2>{props.callToAction}</h2>
    </div>
    
)
}


function Time(props){
    return(
        <h1>{props.message}</h1>
    )
}


export {Btn, Mouse, ModeToggler, RandomNumber, PromoHeading, Time};

