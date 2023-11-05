const target = document.querySelector("body")
function handle(){
    console.log("This is the body of the page")
}
target.addEventListener("click", handle())

const target2 = document.querySelector("p")
function handle2 (){
    console.log("This is the header")
}

//Text Example
const craig = document.createElement("h2")
craig.innerText = "I love Jesus"

document.body.innerText = ""
document.body.appendChild(craig)

//Prompt Example
// const names = prompt("What is your name")

// const test = document.createElement("h1")
// test.innerText = names

// document.body.innerText = ""
// document.body.appendChild(test)

//Input Example
const type = document.createElement("input")

const data = document.createElement("h2")
data.innerText = "Type in the box to change the text here"

document.body.innerText = ""
document.body.appendChild(data)
document.body.appendChild(type)

function sam(){
    data.innerText = type.value
}

type.addEventListener("change", sam)





