import { Link } from "react-router-dom"

const Navigation = () => <nav>
    <ul>
        <li><Link to="/home">Home</Link></li>
        <li><Link to="/counter">Counter</Link></li>
        <li><Link to="/todos">Todos</Link></li>
        <li><Link to="/signup">Sign UP</Link></li>
        <li><Link to="/login">Login</Link></li>
    </ul>
</nav>

export default Navigation