import React from "react";
import './App.css'

const reducer = (state,action) =>{
    if(action.type === 'buy_ingredients') return{money: state.money - 10}
    if(action.type === 'sell_a_meal') return{money: state.money + 10}
    if(action.type === 'celebrity_visit') return{money: state.money + 5000}
    return state;
}
function ReducerApp(){
    const initialState = {money:100}
    const [state, dispatcher] = React.useReducer(reducer, initialState);
    return(
        <div className="App">
            <h1>Use Reducer App</h1>
            <h1>Wallet: {state.money}</h1>
            <div>
                <button onClick={()=>dispatcher({type: 'buy_ingredients'})}>Shopping for veggies!</button>
                <button onClick={()=>dispatcher({type:'sell_a_meal'})}>Serve a meal to the customer</button>
                <button onClick={()=>dispatcher({type: 'celebrity_visit'})}>Celebrity visit</button>
            </div>
        </div>
    )
}


//useref

function UseRef(){
    const formInputerRef = React.useRef(null)

    const focusInput = ()=>{
        formInputerRef.current.focus()
    }
    return(
        <div>
            <h1>Using UseRef to Access Underlying DOM </h1>
            <input type="text" ref={formInputerRef}/>
            <button onClick={focusInput}>Focus Input</button>

        </div>
    )
}


//Incremental App
function Incremental() { 
    const [count, setCount] = React.useState(0); 
   
    function increment() { 
      setCount(prevCount => prevCount + 1) 
    }  
    return ( 
      <div> 
        <h1>Count: {count}</h1> 
        <button onClick={increment}>Plus 1</button> 
      </div> 
    ); 
  } 

//Get weekday with Use Effect
function Weekday(){
    const [day, setDay] = React.useState("Monday")
    const prevDay = usePrevious(day);
    const getNextDay = () => {
        if (day === "Monday"){
            setDay("Tuesday")
        } else if (day === "Tuesday"){
            setDay("Wednesday")
        } else if (day === "Wednesday"){
            setDay("Thursday")
        } else if (day === "Thursday"){
            setDay("Friday")
        } else if (day === "Friday"){
            setDay("Monday")
        }
    }
    return(
        <div style={{padding: "40px"}}>
            <h1>
                Today is: {day} <br />
                {
                    prevDay && (
                        <span>Previous workday was: {prevDay}</span>
                    )
                }
            </h1>
            <button onClick={getNextDay}>Get next day</button>

        </div>
    )
}
function usePrevious(val){
    const ref = React.useRef()
    React.useEffect(()=>{
        ref.current = val
    }, [val])
    return ref.current
}



function AdvanceReact(){
    return(
        <div>
            <ReducerApp/>
            <br />
            <br />
            <UseRef/>
            <br />
            <br />
            <Incremental/>
            <br />
            <br />
            <Weekday/>
            
        </div>
    )

}
export default AdvanceReact