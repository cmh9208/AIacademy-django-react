// import axios from "axios";
// import {server, dlearn, vision} from 'context'

export const server = "http://127.0.0.1:8000/"
export const dlearn = "number/"

// JSON.parse() : json형식의 데이터를 그대로 문자열을 풀어 사용할 수 있게함

// && : state에 정보가 있는지 여부를 
// 체크해 렌더링 전 값의 유무를 미리 파악

// fetch : 비동기함수 -> API호출하는 과정이 안끝나도 자동 다음 코드로 넘어감. 
// then : 받아온 정보를 사용할 필요가 있을때 자동 넘어가지 않게

//전체 함수
const dlearnService = {
    getNumber, postNumber
}
// 
function handleResponse(response){ 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
    }


// 아이리스 
// async function iris(id){
//     const requestOption = {
//         method: "POST",
//         headers: {"Content-Type": "application/json"},
//         body: JSON.stringify(id)
//     }
//     fetch(`${server}${dlearn}iris`, requestOption)
//     .then(handleResponse)
//     .then(data => {
//         alert(JSON.stringify(data))
//     })
//     .catch((error) => {
//         alert('error :::: '+error);
//     });
// }

// POST 패션
async function postNumber(id){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(id)
    }
    fetch(`${server}${dlearn}number`, requestOption)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
}

// GET 패션
async function getNumber(id){
    fetch(`${server}${dlearn}number?id=${id}`)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
} 

// 전체 함수 내보내기
export default dlearnService