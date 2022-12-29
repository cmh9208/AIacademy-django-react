import 'cop/styles/TodoList.css'
import { useSelector } from 'react-redux'
import { Todo } from 'cop'

const TodoList = () => {
    const todos = useSelector((state) => state.todos) // 게터
    return (<>
    <ul>
        {todos.map( todo => (
            <Todo key={todo.id} title={todo.text} />
        ))} 
    </ul>
    </>)
}
export default TodoList