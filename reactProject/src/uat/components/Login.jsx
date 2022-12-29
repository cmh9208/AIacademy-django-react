// import { userLogin } from '../api'
// import { useState } from "react"
// import '../styles/Login.css'
// // import iii from 'uat/styles/iii.png';
// // import is from 'uat/styles/is.jpg';


// // const logo = <img src={iii} alt="로고" width={250} height={200}></img>;
// // const logo2 = <img src={is} alt="로고" width={500} height={500}></img>;

// const Login = () => {
//     const [inputs, setInputs] = useState({})
//     const {user_email, password} = inputs;
    
//     const onChange = e => {
//         e.preventDefault()
//         const {value, name} = e.target 
//         setInputs({...inputs, [name]: value})
//     }

//     const onClick = e => {
//         e.preventDefault()
//         const request = {user_email, password}
//         alert(`사용자 이름: ${JSON.stringify(request)}`)
//         userLogin(request)
//         .then((res)=>{
//             alert(`Response is ${res.config.data}`)
//             console.log(`Response is ${res.config.data}`)
//             localStorage.setItem('token', JSON.stringify(res.config.data))
//         })
//         .catch((err)=>{
//             console.log(err)
//             alert('아이디와 비밀번호를 다시')
//         })

//     }

//     return (
//     <>  
//         {/* <div class="imgcontainer">
//             {logo}
//             {logo2}
//         </div> */}

//         user_email: <input type="text" name="user_email" onChange={onChange} /><br/>
//         password: <input type="text" name="password" onChange={onChange} /><br/>
//         <button onClick={onClick}> 로그인 </button>

//         {/* <div class="container" style={{backgroundcolor:"#f1f1f1"}}>
//                 <button type="button" class="cancelbtn">Cancel</button>
//         <span class="psw">Forgot <a href="#">password?</a></span>
//         </div> */}

//         {/* <h2>로그인 화면</h2>
//         <form action="/action_page.php" method="post">
//             <div class="imgcontainer">
//                 {logo}
//             </div>
//             <div class="imgcontainer">
//             </div>

//                 <div class="container">
//                     <label for="uname"><b>Username</b></label>
//                     <input type="text" placeholder="Enter Username" name="uname" required/>

//                     <label for="psw"><b>Password</b></label>
//                     <input type="password" placeholder="Enter Password" name="psw" required/>
                        
//                     <button type="submit">Login</button>
//                     <label>
//                     <input type="checkbox" checked="checked" name="remember"/> Remember me
//                     </label>
//                 </div>

//             <div class="container" style={{backgroundcolor:"#f1f1f1"}}>
//                 <button type="button" class="cancelbtn">Cancel</button>
//                 <span class="psw">Forgot <a href="#">password?</a></span>
//             </div>
//         </form> */}

    
//     </>
// )}
// export default Login









import '../styles/Login.css'
import { useState } from "react"
import { userLogin } from '../api'
// useHistory 방문한 경로를 모두 기억
import { useNavigate } from "react-router-dom"

export default function LoginForm(){
    const [inputs, setInputs] = useState({})
    const {user_email, password} = inputs;
    const navigate = useNavigate()

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        const request = {user_email, password}
        alert(`사용자 이름: ${JSON.stringify(request)}`)
        userLogin(request)
        .then((res)=>{

            
            // 들어온 값 저장 키,벨류 구조 여기선 스트링 값으로 저장
            localStorage.setItem("loginUser", JSON.stringify(res.data))
            alert(`로컬스토리지에 저장된 정보: ${localStorage.getItem("loginUser")}`)
            // root경로"/" 로그인 하면 홈으로 가도록
            navigate("/home")
            
        })
        .catch((err)=>{
            console.log(err)
            alert('아이디와 비밀번호를 다시')
        })
    }

    return (
    <>
        EMAIL: <input type="text" name="user_email" onChange={onChange} /><br/>
        PASSWORD: <input type="text" name="password" onChange={onChange} /><br/>
        <button onClick={onClick}> 로그인 </button>
    </>
)}