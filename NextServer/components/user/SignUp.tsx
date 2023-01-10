import '../styles/SignUp.css'
import { useState } from "react"


export default function SignUp() {
    const [inputs, setInputs] = useState({})


   
    return (<>
        <h2>회원가입</h2>
        <button >사용자 등록</button>
        <p>버튼을 클릭하시면, 더미 사용자 100명이 등록됩니다.</p>
        </>)
}
