import { useState } from "react"
import { useDispatch } from 'react-redux'
import { addTodo } from '../reducers/todo.reducer'

const AddTodo = () => {

    const [value, setValue] = useState('')
    const dispatch = useDispatch() //스토어에 바로 가기위해 디스패치
    const onChange = e => setValue(e.target.value) //2점타깃의 밸류
    const onSubmit = e => {
        e.preventDefault() // 이벤트 드리븐 중요!
        if(!value.trim()) {
            alert('입력창이 비었습니다.')
        }else{
            alert(`입력값: ${value}`)
        }
        dispatch(addTodo({text: value}))
        setValue('')
    }

    return (<>
    <h2>스케줄러</h2>
    <form onSubmit={onSubmit} method='POST'> 
        <label htmlFor="todo">할 일 :</label><br/>
        <input 
        //2점타깃
            type="text" 
            id="todo" 
            name="todo"
            placeholder="할일 입력"
            value={value} //밸류가 입력되는 값
            onChange={onChange} /><br/><br/>
        
    </form> 
    <p>할 일을 등록하시면, 스케줄 목록에 출력됩니다.</p>
    </>)
}
export default AddTodo //addtodo를 액션으로 보냄