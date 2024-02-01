import React from "react";

function GiftCards (){
    const [giftCard, setGiftCard] = React.useState(
        {
            firstName: "Jenifer",
            lastName: "Smith",
            text: "Free dinner for 4 guests",
            valid: true,
            instructions: "To use coupon, click the button below."
        }
    )
    function spendGiftCard(){
        setGiftCard(prevState=>{
            return {
                ...prevState,
                text: "Your coupon has been used.",
                valid: false,
                instructions: "Please visit our restaurant to renew your gift card"
            }
        })
    }
    return (
        <div>
            <h1>
                Gift Card Page
            </h1>
            <h2>
                Customer: {giftCard.firstName} {giftCard.lastName}
            </h2>
            <h3>
                {giftCard.text}
            </h3>
            <p>
                {giftCard.instructions}
            </p>
            {
                giftCard.valid && (
                    <button onClick={spendGiftCard}>Spend Gift Card</button>
                )
            }
        </div>
    )
}


//USEEFFECT TOPIC

function ToggleMessage(){
    const[toggle, setToggle] = React.useState(false);
    const clickHandler =()=>{
        setToggle(!toggle)
    }
    React.useEffect(()=>{
        document.title = toggle ? "Welcome to Little Lemon" : "Using the useEffect hook"
    }, [toggle])
    return(
        <div>
            <h1>Using the useEffect hook</h1>
            <button onClick={clickHandler}>Toggle message</button>
            {toggle && <h2>Welcome to Little Lemon</h2>}
        </div>
    )
}


//Set PetName

function Pet(){
    const[petName, setPetName] = React.useState("Fluffy")
    function nameLooper(){
        if (petName === "Fluffy"){
            setPetName("Rexy")
        }
        if (petName === "Rexy"){
            setPetName("Gizmo")
        }
        if (petName === "Gizmo"){
            setPetName("Fluffy")
        }
    }
    return(
        <div>
            <h1>I am thinking to name my pet {petName}</h1>
            <button onClick={nameLooper}>Pick a new name</button>
        </div>
    )
}


//Fetch Data

function DataFetch(){
    const [user, setUser] = React.useState([])
    const fetchData = ()=>{
        fetch("https://randomuser.me/api/?results=1")
            .then(response => response.json())
            .then (data => setUser(data))
            .catch((error) => console.log(error)); 
    }
    React.useEffect( ()=>{
        fetchData();
    },[])
return Object.keys(user).length>0 ? (
    <div>
        <h1>Fetch Data Returned</h1>
        <h2>First Name: {user.results[0].name.first}</h2>
        <h2>Last Name: {user.results[0].name.last}</h2>
    </div>
): (
    <h1>Data Pending...</h1>
)

}


//Fetch BTC Rate
function Btc() { 
    const [btcData, setBtcData] = React.useState({}); 
    React.useEffect(() => { 
      fetch(`https://api.coindesk.com/v1/bpi/currentprice.json`) 
        .then((response) => response.json()) 
        .then((jsonData) => setBtcData(jsonData.bpi.USD)) 
        .catch((error) => console.log(error)); 
    }, []); 
   
    return ( 
      <> 
        <h1>Fetch Current BTC/USD data</h1> 
        <p>Code: {btcData.code}</p> 
        <p>Symbol: {btcData.symbol}</p> 
        <p>Rate: {btcData.rate}</p> 
        <p>Description: {btcData.description}</p> 
        <p>Rate Float: {btcData.rate_float}</p> 
      </> 
    ); 
  } 

//Fetch Customer Data
function CustomerData(){
    const[user, setUser] = React.useState([]);
    const fetchData = ()=>{
        fetch("https://randomuser.me/api/?results=1")
            .then((response) => response.json())
            .then((data) => setUser(data))
            .catch((error) => console.log(error));
    }
    React.useEffect(()=>{
        fetchData()},
        [])
    return Object.keys(user).length>0 ? (
        <div style={{padding:"40px"}}>
            <h1>Fetch Customer Data</h1>
            <h2>Name: {user.results[0].name.first}</h2>
            <img src={user.results[0].picture.large} alt="" />
        </div>
    ):(
        <h1>Data pendind...</h1>
    )
}


function GiftCard(){
    return(
        <div>
            <GiftCards/>
            <br />
            <br />
            <br />
            <ToggleMessage/>
            <br />
            <br />
            <br />
            <Pet/>
            <br />
            <br />
            <br />
            <DataFetch/>
            <br />
            <br />
            <br />
            <Btc/>
            <br />
            <br />
            <br />
            <CustomerData/>
        </div>
   
    )
}
export default GiftCard