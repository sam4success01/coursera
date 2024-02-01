import logo from './logo.svg';
import Signup from './SignUp';
import Receipe from './LittleLemon';
import {MyReceipe} from './Switch';
import Goals from './Goal';
import GiftCard from './GiftCard';
import { UserProvider } from './UserContext';

import {Routes, Route, Link} from 'react-router-dom'
import './App.css';
import AdvanceReact from './Hooks';
import Mouse from './MousePostion';
import FeedbackForm from './FeedBack';
import AddEdit from './AddEdit';



function App() {
  return (
    <div className="App">
      <nav>
        <Link to="/" className="nav-item">Home</Link>
        <Link to="/Signup" className="nav-item">SignUp</Link>
        <Link to="/littleLemon" className="nav-item" >Receipe</Link>
        <Link to="/Switch" className="nav-item" >Switch</Link>
        <Link to="/Goal" className="nav-item" >Goals</Link>
        <Link to="/GiftCard" className="nav-item" >GiftCard</Link>
        <Link to="/Hooks" className="nav-item" >AdvanceHooks</Link>
        <Link to="/MousePosition" className="nav-item" >Mouse</Link>
        <Link to="/FeedbackForm" className="nav-item" >Feedback</Link>
        <Link to="/AddEdit" className="nav-item" >AddEdit</Link>
      </nav>


      <Routes>
        <Route path='/l' />
        <Route path='/Signup' element={<Signup/>} />
        <Route path='/littleLemon' element={<Receipe/>} />
        <Route path='/Switch' element={<MyReceipe/>} />
        <Route path='/Goal' element={<Goals/>} />
        <Route path='/GiftCard' element={<GiftCard/>} />
        <Route path='/Hooks' element={<AdvanceReact/>} />
        <Route path='/MousePosition' element={<Mouse/>} />
        <Route path='/FeedbackForm' element={<FeedbackForm/>} />
        <Route path='/AddEdit' element={<AddEdit/>} />
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
