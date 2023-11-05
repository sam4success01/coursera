// Declearing Variables
var person ;
var greeting;
person = "Samuel";
greeting = "Hello"

console.log(greeting,person)

person += "Babe";
greeting = "Hi"

console.log(greeting, person)

// If Statement
var result;
result = 80;

if(result > 50){
    console.log("You passed the test")
} else if(result == 50){
    console.log("You got an average pass")
} else{
    console.log("You need to try again")
}


// Switch Statement
var colour;
colour = "Yellow"

switch(colour) {
    case "Blue" :
        console.log("Eligible for US citizenship");
        break;
    case "Green" :
        console.log("Eligible for Nigeria citizenship")
        break;
    case "Yellow" :
        console.log("Eligible for Canada citizenship")
        break;
    default:
        console.log("Not Eligible")
}


// for loop and while loop

for(i=3; i<=8; i++){
    console.log("This is line " + i)
}

for(i=9; i>0; i--){
    console.log("This is line " + i)
}

var myname = "Samuel";
for(i=0; i < myname.length; i++){
    console.log(myname[i])
}

var i = 3;

while(i<=9){
    console.log(i);
    i+=1;
}

//Nested Loop
for(i=2021; i<=2023; i++){
    for(j=1; j<13; j++){
        console.log("Month"+j, i)
    }
}

//Functions
function addSum(a,b){
    var c = a+b;
    console.log(c)
};
addSum(5,7)
addSum(25,17)

//
var car ={}
car.name = "Toyota"
car.start = function (){
    console.log("Start the engine")
}
console.log(car)
car.start()

//Array and Iteration
var train = ["wheat", "amala", "Iyan"]
console.log(train[2])

for(var trains of train){
    console.log(trains)
}

for(i=0; i<train.length; i++){
    console.log(train[i])
}

//Array Function

function myArray(arr){
    for(i=0; i<arr.length; i++){
        if(arr[i]=="Samuel"){
            console.log("He is", " Samuel")
        } else{
            console.log("others are ", arr[i])
        }
    }
}

var names = ["Samuel", "Joy", "Matthew", "Dara"]
myArray(names)


//Object: Using Dot Notation and Delimiter key-value pairs
var manager = {};
manager.age = 21;
manager.height = "1.5cm";
manager.sex = "male";
console.log(manager)

var manager = {};
manager["age"] = 21;
manager["height"] = "1.5cm";
manager["sex"] = "male";
console.log(manager)

var manager = {"age":21, "height":"1.5cm", "sex":"male"};
manager.marrital= "married"
console.log(manager)

var managerData = ["age", "height", "sex"];
var manager = {"age":21, "height":"1.5cm", "sex":"male"};
managerData.pop();
managerData.push("Birth");
manager["Birth"]="Ogun";
for(i=0; i<managerData.length; i++){
    console.log(manager[managerData[i]])
}


//Strings
var parting = "Goodbye";
var name = "Robin";
console.log(parting.concat(name))
console.log(parting.indexOf("b"))

//Match a letter in a string
console.log(parting.match(/o/))

// try error and throw new error
try{
    console.log(a+b)
} catch(err){
    // console.log(err)
    console.log("Code continue")
}

try {
    throw new Error();
    console.log('Hello');
  } catch(err) {
    console.log('Goodbye');
  }


//Function Programming

 var baseNumber = 100;
 var baseMultiplier = 12;
 var bases = 0;
 function base(number, multiplier){
    return (number * multiplier)
 }
 bases = base(baseNumber,baseMultiplier)
 console.log(bases)

 //Example 2
 function getTotal(a,b) {
    console.log(a + b)
}
var num1 = 2;
var num2 = 3;
getTotal(num1, num2);

//Example 3
function doubleIt(num){
    return num * 2
 }
 console.log(doubleIt(100))

 function objectMaker(val){
    return {
        prop:val
    }
 }
 console.log(objectMaker(100))
 console.log(doubleIt(10).toString())
 console.log(objectMaker(doubleIt(30)))

//RECURSSION
function example (){
    console.log("I am Sam")
    console.log("I am a boy")
    example()
 }
example()

let counter = 3
example = function (){
    console.log(counter)
    counter-=1
    if(counter == 0) return;
    example()
 }
example()

//Use of let in a block space
let color = "red";
function man(){
    let color = "blue";
    console.log(color);
}
console.log(color);
man();

//Object Oriented Programming OOP
EmployeeTaxes = {
    income: 200,
    tax: 0.1,
    taxDue: function(){
        var totalTax = this.income * this.tax
        console.log(totalTax)
    } 
}
console.log(EmployeeTaxes.income)
console.log(EmployeeTaxes.tax)
EmployeeTaxes.taxDue()

//Class

class EmployeeTax{
    constructor(income,tax){
        this.income=income;
        this.tax=tax;
    }

    taxComputation(){
        var totalTax = this.income * this.tax
        console.log(`The accrued tax liability is ${totalTax}`)
    }
}

const Employee1 = new EmployeeTax(5000,0.1)
Employee1.taxComputation()

const Employee2 = new EmployeeTax(3000,0.1)
Employee2.taxComputation()
console.log(Employee1.income)


//class inheritance
class Animal {
    constructor(lg) {
        this.legs = lg;
    }
}
class Dog extends Animal {
    constructor() {
        super(4);
    }
}
var result = new Dog();
console.log(result.legs);


//Get date
var time = new Date()
console.log(time)
console.log(time.getFullYear())

//Prototype
var bird = {
    hasWings: "Wings to fly",
    canFly: "Fly with wings",
    hasFeathers: "Feathers for protection"
}

console.log(bird)

var eagle1 = Object.create(bird)
eagle1.canFly = "eagles can fly higher"
console.log(Object.keys(eagle1))
console.log(eagle1.hasWings)
for(birds in eagle1){
    console.log(birds + ":" + eagle1[birds])
}


// class Inheritance
class Person {
    sayHello() {
        console.log("Hello");
    }
}
class Friend extends Person {
    sayHello() {
        console.log("Hey");
    }
}
var result = new Friend();
result.sayHello();

//Loops and Objects

var car = ["toyota", "Honda", "Lexus"]

for(var cars of car){
    console.log(cars)
}

var car = {
    toyota: "corolla",
    Honde: "CRV-7",
    Lexus: "RX350"
}
console.log(Object.keys(car))
console.log(Object.values(car))
console.log(Object.entries(car))
for(var cars of Object.keys(car)){
    console.log(cars)
}
for(var cars of Object.values(car)){
    console.log(cars)
}
for(var cars of Object.entries(car)){
    console.log(cars)
}
for(var cars in car){
    console.log(cars)
}

//Inherited Objects
var vehicle = {
    toyota: "corolla",
    Honde: "CRV-7",
    Lexus: "RX350"
}

var car = Object.create(vehicle)
car.Mazda = "New model"

for(var cars of Object.keys(car)){
    console.log(cars + ":" + car[cars])
}
for(var cars of Object.values(car)){
    console.log(cars)
}

for(cars in car){
    console.log(cars +":" + car[cars])
}

//Average Grade
const grades = [75,30,50,40,80]

gradesum = 0;

for(i=0; i<grades.length; i++){
    gradesum+=grades[i]
}
console.log(gradesum)


//forEach()
fruits = ["orange", "apple", "grape", "mangoes"]

function array(num, index){
    console.log(index, num)
}
fruits.forEach(array)
//or 
fruits.forEach(function(num, index){
    console.log(index,num)
})

//filter()
num = [10,20,30,40,50,60]

function array (nums){
    return nums > 30
}
console.log(num.filter(array))
//OR
var numm= num.filter(function(nums){
    return nums > 30
})
console.log(numm)

//map()
var list = [10,20,30,40,50,60].map(function(num){
    return num/2
})
console.log(list)

//Map
const list = new Map ();
list.set("Item1", "Google")
list.set("Item2","Jiji")
list.set("Item3", "Yahoo")
console.log(list)
console.log(list.get("Item2"))

//SET
const repetitiveFruits = ['apple','pear','apple','pear','plum', 'apple'];
console.log(new Set(repetitiveFruits))

const fruits = new Set()
fruits.add("mangoes")
fruits.add("oranges")
fruits.add("banana")
console.log(fruits)
console.log(fruits.values())
fruits.values()

//SPREAD AND REST

const fruits = ['apple', 'pear', 'plum']
const berries = ['blueberry', 'strawberry']
const alFruits = [...fruits,...berries]
alFruits.push("blackberry")
console.log(alFruits)
const allFruits = [...fruits,'blueberry', 'strawberry']
console.log(allFruits)

const flying = { wings: 2 }
const car = { wheels: 4 }
const flyingcar = {...flying,...car}
console.log(flyingcar)
const word = "Hello"
console.log([...word])

const car1 = {
    speed: 200,
    color: 'yellow'
}
const car2 = {...car1}
car2.model = "Toyota"
console.log(car2)



document
document.querySelectorAll('p')
document.querySelector("p")
document.getElementById('heading') //get ids with heading
document.getElementsByClassName("txt")






var veggies = []
veggies.push('parsley')
veggies.push('carrot')
console.log(veggies[2])

