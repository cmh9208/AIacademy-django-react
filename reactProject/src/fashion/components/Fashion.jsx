import { useState } from "react"
import dlearnService from "../api"

const Fashion = () => {
    const [inputs, setInputs] = useState({})
    const {id} = inputs
    const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target
      setInputs({...inputs, [name]: value})
    }
    const onGetClick = e => {
        e.preventDefault()
        dlearnService.getFashion(id)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    const onPostClick = e => {
        e.preventDefault()
        dlearnService.postFashion(id)
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }
    return(<>
    <form method="post">
    <h1>FASHION POST방식</h1>
    <p>카테고리를 알고 싶은 옷의 번호를 입력해주세요.</p>
    <input type="text" className="box" placeholder="테스트할 옷 번호" name="id" onChange={onChange}/>
    <button onClick={onPostClick}>옷의 카테고리 찾기</button>
    </form>

    <form method="get">
    <h1>FASHION GET방식</h1>
    <p>카테고리를 알고 싶은 옷의 번호를 입력해주세요.</p>
    <input type="text" className="box" placeholder="테스트할 옷 번호" name="id" onChange={onChange}/>
    <button onClick={onGetClick}>옷의 카테고리 찾기</button>
    </form>
    </>)
}
export default Fashion