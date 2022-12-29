import {useState} from 'react'
import samsungService from "../api"

const Samsung = () => {
    const [movies, setMovies] = useState([])

    const onClick = e => {
        e.preventDefault()
        samsungService.sam().then(res => {
            const json = JSON.parse(res)
            setMovies(json['result'])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (<>
    <h2>삼성 리포트</h2>
    <button onClick={onClick}>삼성 리포트 크롤링</button>
    <p>버튼을 클릭하시면, 삼성리포트의 가장 높은 빈도수의 단어가 출력됩니다.</p>
    <table>
        <thead>
            <tr>
            <th>순위</th><th>단어</th>
            </tr>
        </thead>
        <tbody>
        {movies && movies.map(({rank, title})=>(
            <tr key={rank}><td>{rank}</td><td>{title}</td></tr>
        ))}
        </tbody>
    </table>
    </>)
}
export default Samsung



// const Login = () => {
//     const [inputs, setInputs] = useState({})
//     const {email, password} = inputs;

//     const onChange = e => {
//         e.preventDefault()
//         const {value, name} = e.target 
//         setInputs({...inputs, [name]: value})
//     }

//     const onClick = e => {
//         e.preventDefault()
//         const request = {email, password}
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