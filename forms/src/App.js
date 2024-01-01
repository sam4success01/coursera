import logo from './logo.svg';
import Signup from './SignUp';
import Receipe from './LittleLemon';
import { UserProvider, useUser } from './UserContext';
import {Routes, Route, Link} from 'react-router-dom'
import './App.css';


function App() {
  return (
    <div className="App">
      <nav>
        <Link to="/" className="nav-item">Home</Link>
        <Link to="/Signup" className="nav-item">SignUp</Link>
        <Link to="/littleLemon" className="nav-item" >Receipe</Link>
      </nav>


      <Routes>
        <Route path='/l' />
        <Route path='/Signup' element={<Signup/>} />
        <Route path='/littleLemon' element={<Receipe/>} />
      </Routes>

    </div>
  );
}

function Root(){
  return(
    <UserProvider>
      <App/>
    </UserProvider>
  );
}

export default Root;
