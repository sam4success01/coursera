import {useState} from 'react';
import {validateEmail} from '../src/utils';



function Signup(){
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [email, setEmail] = useState({
        value: "",
        isTouched: false,
    })
    const [password, setPassword] = useState({
        value: "",
        isTouched: false,
    })
    const [role, setRole] = useState("role")

    const getIsFormValid =()=>{
        return(
            firstName && 
            validateEmail(email.value) &&
            password.value.length >=8 &&
            role !== "role"
        )
    }

    const passwordErrorMessage = ()=>{
        return(
            <h6 className='FieldError'>Password Should have at least 8 characters</h6>
        )
    }


    const clearForm =() => {
        setFirstName("");
        setLastName("");
        setEmail({
            value: "",
            isTouched: false,
        });
        setPassword({
            value: "",
            isTouched: false,
        });
        setRole("role")
    }

    const handleSubmit = (e)=>{
        e.preventDefault();
        alert("Account Created");
        clearForm();
    }

    return(
        <div className='SignUp'>
            <form onSubmit={handleSubmit}>
                <br />
                <fieldset>
                    <h2>Sign Up</h2>
                    <div>
                        <label>
                            First Name <sup>*</sup>
                        </label>
                        <br />
                        <input
                        value={firstName}
                        placeholder='Fist Name'
                        onChange={(e)=> setFirstName(e.target.value)} />
                    </div>
                    <br />
                    <div>
                        <label>
                            Last Name <sup>*</sup>
                        </label>
                        <br />
                        <input  
                        value={lastName}
                        placeholder='Last Name'
                        onChange={(e) => setLastName(e.target.value)} />
                    </div>
                    <br />
                    <div>
                        <label>
                            Email address<sup>*</sup>
                        </label>
                        <br />
                        <input 
                        type='email'
                        value={email.value}
                        placeholder='Email address'
                        onChange={(e)=>setEmail({...email, value: e.target.value})} 
                        onBlur={() => setEmail({...email, isTouched: true})} />
                        {email.isTouched && !validateEmail(email.value) ? (<h6 className='FieldError'>"Please enter a valid email address"</h6>):null}
                    </div>
                    <br />
                    <div>
                        <label>
                            Password <sup>*</sup>
                        </label>
                        <br />
                        <input 
                        type='password'
                        value={password.value}
                        placeholder='Password'
                        onChange={(e)=> setPassword({...password, value: e.target.value})}
                        onBlur={() => setPassword({...password, isTouched: true})} />
                        {password.isTouched && password.value.length < 8 ? passwordErrorMessage(): null}
                    </div>
                    <br />
                    <div>
                        <label>
                            Role <sup>*</sup>
                        </label>
                        <br />
                        <select value={role} onChange={(e)=>setRole(e.target.value)} >
                            <option value="role">Role</option>
                            <option value="individual">Individual</option>
                            <option value="business">Business</option>
                        </select>
                    </div>
                    <br />
                    <button type='submit' disabled={!getIsFormValid()} className='SignUpButton'>Create Account</button>
                </fieldset>

            </form>
        </div>
    )
}

export default Signup