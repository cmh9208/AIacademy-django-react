// import '../styles/Login.css'

import { useState } from "react"
import BlogService from "../api"

const SignUp = () => {
    const [inputs, setInputs] = useState({})
    const {email, nickname, password} = inputs;

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }

    const onClick = e => {
        e.preventDefault()
        BlogService.blogPost(email, nickname, password)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (<>
        <h2> 회원가입 </h2>
        E-MAIL: <input type="text" name="email" onChange={onChange}/><br/>
        NICKNAME: <input type="text" name="nickname" onChange={onChange}/><br/>
        PASSWORD: <input type="text" name="password" onChange={onChange}/><br/>
        <button onClick={onClick}>사용자 등록</button><br/>
        <p>버튼을 클릭하시면, 더미 사용자 100명이 등록됩니다.</p>
        <table>
        </table>
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
//         const request = {email, nickname, password}
//         alert(`사용자 이름: ${JSON.stringify(request)}`)
//         userLogin(request)
//         .then((res)=>{
//             console.log(`Response is ${res}`)
//             localStorage.setItem('token', JSON.stringify(res.config.data))
//         }) //성공 후 다시 리스판스 됨 (책임연쇄 패턴)
//         .catch((err)=>{
//             console.log(err) 
//             alert('아이디와 비밀번호를 다시')
//         })
//     }
//     return(
//         <>
//         email: <input type="text" name="email" onChange={onChange} style={{color:"dodgerblue"}}/><br/>
//         nickname: <input type="text" name="nickname" onChange={onChange} style={{color:"dodgerblue"}}/><br/>
//         password: <input type="text" name="password" onChange={onChange} style={{color:"dodgerblue"}}/><br/>
//         <button onClick={onClick}> 회원가입 </button>
//         </>
//     )
// }
// export default SignUp







