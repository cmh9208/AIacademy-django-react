// import axios from "axios";
// import {server, dlearn, vision} from 'context'

// export const server = "http://127.0.0.1:8000/"
// export const dlearn = "imdb/"

// JSON.parse() : json형식의 데이터를 그대로 문자열을 풀어 사용할 수 있게함, 정보를

// && : state에 정보가 있는지 여부를 
// 체크해 렌더링 전 값의 유무를 미리 파악

// fetch : 비동기함수 -> API호출하는 과정이 안끝나도 자동 다음 코드로 넘어감. url을가짐
// then : 받아온 정보를 사용할 필요가 있을때 자동 넘어가지 않게

//전체 함수
// const dlearnService = {
//     getImdb, postImdb
// }
// // 
// function handleResponse(response){ 
//     return response.text()
//         .then(text =>{
//             const data = text && JSON.parse(text)
//             if(!response.ok){
//                 if(response.status === 401){
//                     window.location.reload()
//                 }
//                 const error = (data && data.message) ||
//                     response.statusText
//                 return Promise.reject(error)
//             }
//             return data
//         })
//     }


// // POST 순환
// async function postImdb(id){
//     const requestOption = {
//         method: "POST",
//         headers: {"Content-Type": "application/json"},
//         body: JSON.stringify(id)
//     }
//     fetch(`${server}${dlearn}imdb`, requestOption)
//     .then(handleResponse)
//     .then(data => {
//         alert('결과: '+JSON.stringify(data))
//     })
//     .catch((error) => {
//         alert('error :::: '+error);
//     });
// }

// // GET 순환
// async function getImdb(id){
//     fetch(`${server}${dlearn}imdb?id=${id}`)
//     .then(handleResponse)
//     .then(data => {
//         alert('결과: '+JSON.stringify(data))
//     })
//     .catch((error) => {
//         alert('error :::: '+error);
//     });
// } 

// // 전체 함수 내보내기
// export default dlearnService






/**import axios from "axios";
const server = `http://127.0.0.1:8000`
export const postfashion = id => axios.post(`${server}/shop/fashion/img`, id)  
export const getfashion = id => axios.get(`${server}/shop/fashion/img?id=${id}`)
**/




/**import axios from "axios";
const server = `http://127.0.0.1:8000`
export const postfashion = id => axios.post(`${server}/shop/fashion/img`, id)  
export const getfashion = id => axios.get(`${server}/shop/fashion/img?id=${id}`)
**/

export const server = "http://127.0.0.1:8000/"
export const dlearn = "imdb/"

const naverMovieReviewService = {classifyPositiveAboutReview}

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
async function classifyPositiveAboutReview(review){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(review)
    }
    const url = `${server}${dlearn}imdb`
    const res = await fetch(url, requestOption)
    
    .then(handleResponse)
    .then(data => (JSON.stringify(data)))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
}
export default naverMovieReviewService