import '../styles/SignUp.css'
import { useState } from "react"
import BlogService from '../api'
// import { useNavigate  } from "react-router-dom"


const SignUp = () => {

    const onClick = e => {
        e.preventDefault()
       
        
    }
    return (<>
        <h2>회원가입</h2>
        <button onClick={onClick}>사용자 등록</button>
        <p>버튼을 클릭하시면, 더미 사용자 100명이 등록됩니다.</p>
        </>)
}
export default SignUp




// const SignUp = () => {

//     const [inputs, setInputs] = useState({})
//     const {email, nickname, password} = inputs;

//     const onChange = e => {
//         e.preventDefault()
//         const {value, name} = e.target 
//         setInputs({...inputs, [name]: value})
//     }

//     const onClick = e => {
//         e.preventDefault()
//         // userSinup(email, nickname, password)
//         // .then(data => JSON.stringify(data))

//         BlogService.blogPost(email, nickname, password)
//         let arr = document.getElementsByClassName('box')
//         // for(let i=0; i<arr.length; i++) arr[i].value = ""
        
//     }
//     return (<>
//         <h2>회원가입</h2>

//         E-MAIL: <input type="text" name="email" onChange={onChange}/><br/>
//         NICKNAME: <input type="text" name="nickname" onChange={onChange}/><br/>
//         PASSWORD: <input type="text" name="password" onChange={onChange}/><br/>

//         <button onClick={onClick}>사용자 등록</button>
//         <p>버튼을 클릭하시면, 더미 사용자 100명이 등록됩니다.</p>
//         </>)
// }
// export default SignUp


