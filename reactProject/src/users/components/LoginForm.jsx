import '../styles/Login.css'
import { useState } from "react"
import { userLogin } from '../api'
import { useNavigate  } from "react-router-dom"

export default function LoginForm(){
    // const [<상태 값 저장 변수>, <상태 값 갱신 함수>] = useState(<상태 초기 값>);
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
            
            localStorage.setItem("loginUser", JSON.stringify(res.data))
            alert(`로컬스토리지에 저장된 정보: ${localStorage.getItem("loginUser")}`)
            navigate("/home")
        })
        .catch((err)=>{
            console.log(err)
            alert('아이디와 비밀번호를 다시')
        })

    }

    return (
    <>
        <h2>로그인</h2>
        EMAIL: <input type="text" name="user_email" onChange={onChange} /><br/>
        PASSWORD: <input type="text" name="password" onChange={onChange} /><br/>
        <button onClick={onClick}> 로그인 </button>

    
    </>
)}
