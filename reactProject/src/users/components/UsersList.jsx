// import {useState} from 'react'
// import usersService from "../api"

// const Users = () => {
//     const [movies, setMovies] = useState([])

//     const onClick = e => {
//         e.preventDefault()
//         usersService.users().then(res => {
//             const json = JSON.parse(res)
//             setMovies(json['result'])
//         })
//         let arr = document.getElementsByClassName('box')
//         for(let i=0; i<arr.length; i++) arr[i].value = ""
//     }

//     return (<>
//     <h2>유저</h2>
//     <button onClick={onClick}>유저 검색</button>
//     <p>버튼을 클릭하시면, 유저검색.</p>
//     <table>
//         <thead>
//             <tr>
//             <th>순위</th><th>영화 제목</th>
//             </tr>
//         </thead>
//         <tbody>
//         {movies && movies.map(([rank, title])=>(
//             <tr key={rank}><td>{rank}</td><td>{title}</td></tr>
//         ))}
//         </tbody>
//     </table>
//     </>)
// }
// export default Users
import usersService from "../api"

import {useState, useEffect} from 'react'
import axios from 'axios'

export default function UserList(){
    const [list, setList] = useState([])

    useEffect(()=>{
        // alert('2')
        axios
        .get('http://localhost:8000/users/user-list')
        .then(res => {
            console.log(" 회원목록 들어옴 ")
            console.log(res.data)
            setList(res.data)
        })
        .catch(err => {
            console.log(err)
        })
    }, [])

    // const onClick = e => {
    //     e.preventDefault()
    //     usersService.users().then(res => {
    //         const json = JSON.parse(res)
    //         setList(json['result'])
    //     })
    //     let arr = document.getElementsByClassName('box')
    //     for(let i=0; i<arr.length; i++) arr[i].value = ""
    // }

    return (<>
        <table style={{ width: "100%", textAlign: "center", margin: "0 auto"}}>
        <h2>유저 정보</h2>
        </table>
        <table style={{ width: "100%", height: "700px", textAlign: "center", margin: "0 auto"}}>
            <thead>
                <tr>
                <th>아이디</th><th>이메일</th><th>비밀번호</th><th>이름</th><th>전화번호</th>
                <th>생년월일</th><th>주소</th><th>직업</th><th>관심사</th>
                </tr>
            </thead >
            <tbody >
            {list && list.map(({id, user_email, password, user_name, phone, birth, address,
             job, user_interests})=>(
                <tr key={id}>
                <td style={{ textAlign: "center"}}>{id}</td>
                <td style={{ textAlign: "center"}}>{user_email}</td>
                <td style={{ textAlign: "center"}}>{password}</td>
                <td style={{ textAlign: "center"}}>{user_name}</td>
                <td style={{ textAlign: "center"}}>{phone}</td>
                <td style={{ textAlign: "center"}}>{birth}</td>
                <td style={{ textAlign: "center"}}>{address}</td>
                <td style={{ textAlign: "center"}}>{job}</td>
                <td style={{ textAlign: "center"}}>{user_interests}</td>
                </tr>
            ))}
            </tbody>
        </table>
        </>)
}


// import {useState} from 'react'
// import webcrawlerService from "../api"

// const NaverMovie = () => {
//     const [movies, setMovies] = useState([])

//     const onClick = e => {
//         e.preventDefault()
//         webcrawlerService.naverMovie().then(res => {
//             const json = JSON.parse(res)
//             setMovies(json['result'])
//         })
//         let arr = document.getElementsByClassName('box')
//         for(let i=0; i<arr.length; i++) arr[i].value = ""
//     }

//     return (<>
//     <h2>네이버 영화 크롤러</h2>
//     <button onClick={onClick}>네이버 영화 크롤링</button>
//     <p>버튼을 클릭하시면, 네이버 영화 목록이 출력됩니다.</p>
//     <table>
//         <thead>
//             <tr>
//             <th>순위</th><th>영화 제목</th>
//             </tr>
//         </thead>
//         <tbody>
//         {movies && movies.map(({rank, title})=>(
//             <tr key={rank}><td>{rank}</td><td>{title}</td></tr>
//         ))}
//         </tbody>
//     </table>
//     </>)
// }
// export default NaverMovie