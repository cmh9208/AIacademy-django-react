// import { useState } from "react"
// import dlearnService from "../api"

// const Imdb = () => {
//     const [inputs, setInputs] = useState({})
//     const {id} = inputs
//     const onChange = e => {
//       e.preventDefault()
//       const {value, name} = e.target
//       setInputs({...inputs, [name]: value})
//     }
//     const onGetClick = e => {
//         e.preventDefault()
//         dlearnService.getImdb(id)
//         let arr = document.getElementsByClassName('box')
//         for(let i=0; i<arr.length; i++) arr[i].value = ""
//     }
//     const onPostClick = e => {
//         e.preventDefault()
//         dlearnService.postImdb(id)
//         let arr = document.getElementsByClassName('box')
//         for(let i=0; i<arr.length; i++) arr[i].value = ""
//     }
//     return(<>
//     <form method="post">
//     <h1>IMDB POST방식</h1>
//     <p>리뷰를 등록해 주세요.</p>
//     <input type="text" className="box" placeholder="등록할 리뷰" name="id" onChange={onChange}/>
//     <button onClick={onPostClick}>리뷰 긍정, 부정 분류하기</button>
//     </form>

//     <form method="get">
//     <h1>IMDB GET방식</h1>
//     <p>리뷰를 등록해 주세요.</p>
//     <input type="text" className="box" placeholder="등록할 리뷰" name="id" onChange={onChange}/>
//     <button onClick={onGetClick}>리뷰 긍정, 부정 분류하기</button>
//     </form>
//     </>)
// }
// export default Imdb
import naverMovieReviewService from "../api"
import { useState } from "react"

const Korean = ()=> {
    const [inputs, setInputs] = useState({})
    const [positive, setPositive] = useState('')
    const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target
      setInputs({...inputs, [name]: value})
    }

    const onClick = e =>{
        e.preventDefault()
        naverMovieReviewService.classifyPositiveAboutReview(inputs).then(res => {
            const json = JSON.parse(res)
            setPositive(json["result"])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (<>
    <h5>네이버 Imdb</h5>
    <form method="post">확인할 리뷰 : 
    <input type="text" className="box" placeholder="리뷰" name="inputs" onChange={onChange}
    />
    <button type="submit" onClick={onClick}>리뷰 긍정도 확인</button></form>
    <table>
        <thead>
            <tr>
                <th>감지된 언어</th>
            </tr>
        </thead>
        <tbody>
        {positive && 
            <tr ><td>{positive} </td></tr>
        }    
        </tbody>
    </table>     
    </>)
}
export default Korean