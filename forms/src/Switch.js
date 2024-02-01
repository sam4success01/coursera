
import "./Styles.css";
import { useUser } from './UserContext';



const Switch = () => {
    const { theme, toggleTheme } = useUser();
    return (
      <label className="switch">
        <input
          type="checkbox"
          checked={theme === "light"}
          onChange={toggleTheme}
        />
        <span className="slider round" />
      </label>
    );
   };
   

const Title = ({ children }) => {
    const { theme } = useUser();
    return (
      <h2
        style={{
          color: theme === "light" ? "black" : "white",
        }}
      >
        {children}
      </h2>
    );
  };
  
  const Paragraph = ({ children }) => {
    const { theme } = useUser();
    return (
      <p
        style={{
          color: theme === "light" ? "black" : "white",
        }}
      >
        {children}
      </p>
    );
  };
  
  const Content = () => {
    return (
      <div>
        <Paragraph>
          We are a pizza loving family. And for years, I searched and searched and
          searched for the perfect pizza dough recipe. I tried dozens, or more.
          And while some were good, none of them were that recipe that would
          make me stop trying all of the others.
        </Paragraph>
        
      </div>
    );
  };
  
  const Header = () => {
    const { theme } = useUser();
    return (
      <header>
        <Title>Little Lemon 🍕</Title>
        <Switch />
        <p>{theme}</p>
      </header>

    );
  };
  
  const Page = () => {
    return (
      <div className="Page">
        <Title>When it comes to dough</Title>
        <Content />
      </div>
    );
  };
  
  function MyReceipe() {
    const { theme } = useUser();
    return (
      <div
        style={{
          backgroundColor: theme === "light" ? "white" : "black",
        }}
      >
        <Header />
        <Page />
      </div>
    );
  }
  

  export {MyReceipe, useUser}

