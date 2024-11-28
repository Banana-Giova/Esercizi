import './NavBar.css'
const img = "vite";
const x = 47;

function NavBar() {
    return (
        <>
        <nav>{x}</nav>
        <img src={`/${img}.svg`}></img>
        <ul>
        <li><a href="#"> Ciao </a></li>
        <li><a href="#"> Ciao </a></li>
        <li><a href="#"> Ciao </a></li>
        <li><a href="#"> Ciao </a></li>
        <li><a href="#"> Ciao </a></li>
       </ul>
       </>
    )

}

export default NavBar