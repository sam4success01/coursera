import Homepage from './Homepage';
import AboutMe from './AboutMe';
import Contact from './Contact';
import {Routes, Route, Link} from 'react-router-dom';
import rooftop from './asset/images/rooftop.jpeg';
import ReactPlayer from 'react-player';
import './App.css';

function App() {

  const randomImageUrl ="https://imageio.forbes.com/blogs-images/annabel/files/2018/06/Rooftop-at-QT.jpg?format=jpg&height=900&width=1600&fit=bounds"

  const vidUrl = "https://youtu.be/5taka1Ftu-E"

  
  return (
    <div className="App">
      <nav className="nav">
        <Link to="/" className="nav-item">Homepage</Link>
        <Link to="/AboutMe" className="nav-item">About Me</Link>
        <Link to="/Contact" className='nav-item'>Contact</Link>
      </nav>

  
      <h1>Hello Samuel</h1>

      <Routes>
        <Route path = "/" element={<Homepage/>} />
        <Route path="/AboutMe" element={<AboutMe/>} />
        <Route path="/Contact" element={<Contact/>} />
      </Routes>

     
      <img 
      height = {200}
      src={rooftop} alt="An image of a rooftop" />

      <img 
      height = {200}
      src={require('./asset/images/rooftop2.jpg')} 
      alt="An image of a rooftop" />

      <img 
      height = {200}
      src={randomImageUrl} 
      alt="An image of a rooftop" />

      <h1>React Player</h1>
      <ReactPlayer className="video"
      url={vidUrl}
      playing={false}
      volume ={0.5}
      controls/>

    </div>
  );
}

export default App;
