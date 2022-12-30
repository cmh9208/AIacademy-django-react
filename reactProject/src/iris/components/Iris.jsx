
// import { stroke } from '/blog/api'
import { useState } from "react"
import { iris } from '../api'
//sdsdsdsds

const Iris = () => {
  const [inputs, setInputs] = useState({})
  const {petal_width, petal_length, sepal_width, sepal_length} = inputs;

  const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target 
      setInputs({...inputs, [name]: value})
  }
  const onClick = e => {
      e.preventDefault()
      const request = {petal_width, petal_length, sepal_width, sepal_length}
      alert(`사용자 이름: ${JSON.stringify(request)}`)
      iris(request)
      .then((res)=>{
        console.log(`Response is ${res.data.result}`)
        localStorage.setItem('token', JSON.stringify(res.data.result))
        alert(`찾는 품종 : ${JSON.stringify(res.data.resp)}`)

      })
      .catch((err)=>{
          console.log(err)
          alert('다시 입력')
      })
  }
  return (
  <>  
      petal_width: <input type="text" name="petal_width" onChange={onChange} /><br/>
      petal_length: <input type="text" name="petal_length" onChange={onChange} /><br/>
      sepal_width: <input type="text" name="sepal_width" onChange={onChange} /><br/>
      sepal_length: <input type="text" name="sepal_length" onChange={onChange} /><br/>
      <button onClick={onClick}> 확인 </button>
  </>
)}
export default Iris

