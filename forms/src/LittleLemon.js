import { useUser } from './UserContext';
import {useState, useEffect} from 'react';
import Modal from 'react-modal';
import 'reactjs-popup/dist/index.css';



const LoggedInuser =()=>{
    const {user} = useUser();
   
    return(
        <p>Hello <span className="Username">{user.name}</span></p>
    );
};


const Header = () => {
    return(
        <header>
            <h2>Blog App</h2>
            <LoggedInuser/>

        </header>
    );
};



function Receipe(){
    const {user, result, handleSubmit, setResult, toggleModal, show, theme, setTheme, toggleTheme} = useUser();




    return(
        <div className="Receipe" id={theme} > 
            <div ></div>
            <div >
                
                <div>
                    <label className='switch'>
                        <input 
                        type="checkbox"
                        checked={theme == "light"}
                        onChange={toggleTheme}
                         />
                         <span className='slider round' />
                         <p>{theme}</p>
                         
                    </label>
                </div>

                {show && (
                     <div className="modal">
                        <div onClick={toggleModal} className="overlay"></div>
                        <div className='modal-content'>
                            <form onSubmit={handleSubmit} className='content' >
                                <label >Please Input First Name</label>
                                <input value={result} onChange={(e)=>{setResult({...result, name: e.target.value})}} />
                                <button>Submit</button>
                            </form>  

                        </div>
             
                     </div>
      

                )}
               
                <div className='content'>
                    <button onClick={toggleModal} >Open Modal</button>
                    <Header/>  
                    <h2>What is Lorem Ipsum?</h2>
                    <p>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus repudiandae, laborum ratione repellendus cum vel tenetur, iure laboriosam quo dolor, possimus numquam fuga. Earum, sint voluptatem temporibus repellendus quam delectus?
                    </p>

                    <footer>Written By {user.name}</footer>  

                </div>
  
                

            </div>
            <div></div>


        </div>
    )

};


export default Receipe