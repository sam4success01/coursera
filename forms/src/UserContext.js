import {createContext, useContext, useState} from "react";


const UserContext = createContext("");

export const UserProvider = ({children}) => {
    const [result, setResult] = useState({
        name: "John",
        email: "john@example.com",
        dob: "01/01/2000",
    });
    const [user, setUser] = useState("")

    const handleSubmit =(e)=>{
        e.preventDefault();
        setUser(result);
        setTimeout(()=>  {
            setShow(!show);
        }, 200)
    }


    const [show, setShow] = useState(false)

    const toggleModal = (value) => {
        setShow(!show);
        setResult(value);

      };


      const [theme, setTheme] = useState("light")

      const toggleTheme = () =>{
        setTheme(theme === "light" ? "dark" : "light")
      }




    return <UserContext.Provider value={{user, handleSubmit, setResult, toggleModal, show, setShow, theme, setTheme, toggleTheme}}>{children}</UserContext.Provider>
};

export const useUser = () => useContext(UserContext);