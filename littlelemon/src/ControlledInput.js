import { useState, useRef} from "react"


const Form = () => {
    const fileInput = useRef(null)

    const handleSubmit =(e) =>{
        e.preventDefault();
        const files = fileInput.current.files
    }

    return(
        <form onSubmit={handleSubmit}>
            <input ref={fileInput}
            type="file"
            />
        </form>
    )
}


//FORM SURVEY

function FormSurvey(){
    const [score, setScore] = useState(10)
    const [result, setResult] = useState("")

    const handleSubmit = (e) =>{
        e.preventDefault();
        setResult(`Thank you for rating us ${score}/10`);
    }

    return(
        <div className="className">
            <form onSubmit={handleSubmit}>
                <fieldset>
                    <h2>Feedback Form</h2>
                    <div>
                        <label htmlFor="">Score  {score}</label>
                        <br />
                        <input type="range" min={0} max={10} onChange={(e)=>setScore(e.target.value)} />
                    </div>
                    <button type="Submit">Submit</button>
                    <p>{result}</p>
                </fieldset>
            </form>
        </div>
    )
}

function MyForm() {
    const [inputValue, setInputValue] = useState('');
    const [name, setName] = useState('');
  
    function handleSubmit(event) {
      event.preventDefault(); // prevent the form from submitting
      setName(inputValue)
    }
  
    return (
      <form onSubmit={handleSubmit}>
        <label>
          Type something:
          <input
            type="text"
            value={inputValue}
            onChange={(event) => setInputValue(event.target.value)}
          />
        </label>
        <button type="submit">Submit</button>
        <p>{name}</p>
      </form>
    );
  }


  const Form2 =() => {
    const [name, setName] = useState("")
    const [inputName, setinputName] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault();
        setinputName(name);
    }
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <fieldset>
                    <div>
                        <label htmlFor="name">Name</label>
                        <input type="text"
                        id="name"
                        placeholder="Name"
                        value={name}
                        onChange={(e) => setName(e.target.value)} />
                    </div>
                    <button disabled={!name} type="Submit">Submit</button>
                    <p >{inputName}</p>
                </fieldset>
              

            </form>
        </div>
    )

}

export {Form, FormSurvey, MyForm, Form2}


