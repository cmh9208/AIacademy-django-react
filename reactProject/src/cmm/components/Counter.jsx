import { useState } from "react"

const Counter = () => {
  const [count, setCount] = useState(0)
  return (<>
    <h3>카운터</h3>
    <div> 클릭한 회수 : {count}</div>
    <button onClick={() => {setCount(count + 1)}}>
      +
    </button>
    <button onClick={() => {setCount(count - 1)}}>
      -
    </button>
  </>)
}
export default Counter