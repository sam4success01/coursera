const topDesserts = [
    {
        id: "1",
        title: "Tiramisu",
        description: "The best tiramisu in town",
        image: "https://picsum.photos/200/300/? random",
        price: "$5.00",
    },
    {
        id: "2",
        title: "Lemon Ice Cream",
        description: "Mind blowing taste",
        image: "https://picsum.photos/200/300/? random",
        price: "$4.50",
    },
    {
        id: "3",
        title: "Chocolate mousse",
        description: "Unexplored flavour",
        image: "https://picsum.photos/200/300/? random",
        price: "$6.00"
    }
]

function Desserts (props){
    const littleLemon = topDesserts.map(dessert => {
        const items = `${dessert.title} - ${dessert.price}`
        return <li>{items}</li>
        
    })
    return <p>{littleLemon}</p>
}

export default Desserts;