import React, {useState} from 'react';
import Heading from './Heading';
import Fruits from './Fruits';
import FruitsCounter from './FruitsCounter';
import './App.css';


function App() {
  const [word, setWord] = React.useState('Eat')
  function handleClick(){
    setWord("Drink")
  }

  const [inputText, setText] = useState(''); 
  function handleChange(e) { 
    setText(e.target.value); 
  } 

  const [form, setForm] = useState({
    firstName: "Luke",
    lastName: "Jones",
    email: "lukeJones@yahoo.com"
  })

  const [fruits]=React.useState([
    {fruitName: 'apple', id: 1},
    {fruitName: 'apple', id: 2},
    {fruitName: 'plum', id: 3},
  ]);


  return(
    <div className="App">
      <Heading message = {word + " at little lemon"} />
      <button onClick={handleClick}>Click Here</button>
      <br/>
      <br/>
      <br/>
      <input value={inputText} onChange={handleChange} /> 
      <p>You typed: {inputText}</p> 
      <button onClick={() => setText('hello')}>Reset</button> 
      <br/>
      <br/>
      <br/>
      <label>
        First Name: <input value={form.firstName} onChange={e =>{setForm({...form, firstName: e.target.value})}} />
      </label>
      <br />
      <br />
      <label>
        Last Name: <input value={form.lastName} onChange={e =>{setForm({...form, lastName: e.target.value})}} />
      </label>
      <br />
      <br />
      <label>
        Email Address: <input value={form.email} onChange={e =>{setForm({...form, email: e.target.value})}} />
      </label>
      <p>{form.firstName} </p>
      <p>{form.lastName} </p>
      <p>{form.email} </p>
      <br />
      <br />
      <h1>Where should the state go?</h1>
      <Fruits fruits={fruits} />
      <FruitsCounter fruits={fruits} />
    </div>
    
  )

}

export default App;
