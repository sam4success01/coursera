import React from "react";
import './Feedback.css'

function Feedback({onSubmit}){
    const [score, setScore] = React.useState("10")
    const [comment, setComment] = React.useState("")
    const [list, setList] = React.useState([])
    const [edit, setEdit] = React.useState([false])
    const isDisabled = Number(score) < 5 && comment.length <= 10
    const textAreaPlaceholder = isDisabled
    ? "Please provide a comment explaining why the experience was not good. Minimum length is 10 characters."
    : "Optional Feedback"

    const handleSubmit = (e) => {
        e.preventDefault();
        const data = {score,comment}
        if(score&&comment){
            setList((ls)=>[...ls, data])
            setComment("")
        }
    }
    const handleDelete=(forms)=>{
        const newList = list.filter((a) => a !== forms)
        setList(newList)
    }
    return(
        <div className="view">
            <form onSubmit={handleSubmit}>
                <fieldset>
                    <h2>Feedback Form</h2>
                    <div className="Field">
                        <label htmlFor="score">
                            Score: {score} ⭐
                        </label>
                        <input id="score" value={score} onChange={(e)=>{setScore(e.target.value)}}
                        type="range" min='0' max='10' />
                    </div>
                    <div className="Field">
                        <label htmlFor="comment">Comments:</label>
                        <textarea name="comment" id="comment" placeholder={textAreaPlaceholder} value={comment}
                        onChange={(e)=> {setComment(e.target.value)}}></textarea>
                    </div>
                    <button type="submit" disabled={isDisabled}>Submit</button>
                </fieldset>
            
            </form>
            
            {
                list.map((a)=>
                    <div>
                        <ul>
                            <li>
                                The customer rating is {a.score} and comment is {a.comment}
                                <button onClick={()=>handleDelete(a)}>Delete</button>
                            </li>
                        </ul>
                    </div>
                )
            }

        </div>
    )
}

const FeedbackForm = () => {

    return(
        <div className="view">
            <Feedback />
        </div>
    )

}
export default FeedbackForm