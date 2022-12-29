// import { stroke } from '/blog/api'
import { useState } from "react"

// import { stroke } from '/blog/api'
import { stroke } from '../api'


const Stroke = () => {
  const [inputs, setInputs] = useState({})
  const {petal_width} = inputs;

  const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target 
      setInputs({...inputs, [name]: value})
  }
  const onClick = e => {
      e.preventDefault()
      const request = {petal_width}
      alert(`사용자 이름: ${JSON.stringify(request)}`)
      stroke(request)
      .then((res)=>{
          console.log(`Response is ${res.config.data}`)
          localStorage.setItem('token', JSON.stringify(res.config.data))
      })
      .catch((err)=>{
          console.log(err)
          alert('다시 입력')
      })

  }

  return (
  <>  
      petal_width: <input type="text" name="petal_width" onChange={onChange} /><br/>

     
      <button onClick={onClick}> 확인 </button>
 
  </>
)}
export default Stroke


// const Stroke = () => {
//   const [count, setCount] = useState(0)
//   return (<>
//     <h3>카운터</h3>
//     <div> 클릭한 회수 : {count}</div>
//     <button onClick={() => {setCount(count + 1)}}>
//       +
//     </button>
//     <button onClick={() => {setCount(count - 1)}}>
//       -
//     </button>
//   </>)
// }
// export default Stroke
