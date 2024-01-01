import { useState } from "react";

const desserts = [
    {
      name: "Chocolate Cake",
      calories: 400,
      createdAt: "2022-09-01",
    },
    {
      name: "Ice Cream",
      calories: 200,
      createdAt: "2022-01-02",
    },
    {
      name: "Tiramisu",
      calories: 300,
      createdAt: "2021-10-03",
    },
    {
      name: "Cheesecake",
      calories: 600,
      createdAt: "2022-01-04",
    },
  ];

  function Carlory(props){

    const [data, setData] = useState(desserts)

    const [level, setLevel] = useState(700)

    const handleSubmit = (e) =>{
      e.preventDefault();
      if (!lowCarloriesDesserts){
        return data
      }
    }

      
    const lowCarloriesDesserts = data
      .filter((dessert) => {
        return dessert.calories <= level;
      })
      .sort((a,b) => {
        return a.calories - b.calories
      })
      .map((dessert) => {
        return(
          <li>{dessert.name} - {dessert.calories} cal</li>
        )
      })


    return(
      <div>
        <form action="" onSubmit={handleSubmit}>
          <label htmlFor="">
            <select name="" id="" onChange={(e)=> setLevel(e.target.value)}>
              <option value="100">{Number(100)}</option>
              <option value="200">{Number(200)}</option>
              <option value="300">{Number(300)}</option>
              <option value="400">{Number(400)}</option>
              <option value="500">{Number(500)}</option>
              <option value="600">{Number(600)}</option>
            </select>
            <ul>{lowCarloriesDesserts}</ul> 
          </label>
          
        </form>

      
      </div>

    ) 
  }

  export default Carlory;