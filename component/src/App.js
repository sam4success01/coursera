import logo from './logo.svg';
import './App.css';
import Heading from './header';
import mylogo from './mylogo.jpeg';
import {Btn, Mouse, ModeToggler, RandomNumber,PromoHeading, Time} from './Btn';


function Logo(props){
  const userPics = <img src={mylogo} />;
  return userPics
}



function App() {
  const data = {
    heading: "99% off all items!",
    callToAction: "Everything must go!"
  }
  const time = new Date()

  return (
    <div style={{textAlign:"center"}}>
      <head>
        <meta http-equiv="refresh" content="5"/>
      </head>
      <input type="text" ></input>
      <Btn/>
      <br/>
      <br/>
      <br/>
      <Mouse/>
      <br/>
      <br/>
      <br/>
      <ModeToggler/>
      <br/>
      <br/>
      <br/>
      <RandomNumber/>
      <br/>
      <br/>
      <br/>
      <Time message={time.toLocaleTimeString()}/>
      <br/>
      <br/>
      <br/>
      <PromoHeading heading = {data.heading} callToAction = {data.callToAction}/>
      <Heading firstName="Anyname Other than Bob "/>
      <Heading firstName="Jack"/>
      <Logo/>
    </div>
  )

}

export default App;
