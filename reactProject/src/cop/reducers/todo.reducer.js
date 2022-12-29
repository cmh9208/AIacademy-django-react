import { createSlice } from "@reduxjs/toolkit"
import { v4 as uuid } from 'uuid'
/**
const initialState = {todos: [], todo: {}}
export const addTodoAction = todo => ({type: "ADD_TODO", payload: todo})
export const toggleTodoAction = todoId => ({type: "TOGGLE_TODE", payload: todoId})
export const deleteTodoAction = todoId => ({type: "DELETE_TODE", payload: todoId}) 
const todoReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'ADD_TODO':
        return {...state, todos: [...state.todos, action.payload]}
      case 'TOGGLE_TODE':
        return {...state, todos: state.todos.map(
            todo => (todo.id === action.payload) ? {...todo, complete: !todo.complete} 
                                                : todo)}
      case 'DELETE_TODE':
        return {...state, todos: state.todos.filter(todo => todo.id !== action.payload)}
      default:
        return state
    }
  }
 */
const todoSlice = createSlice({
  name: 'todos',
  initialState: [],
  reducers : {
    addTodo: (state, action) => {
      
      const newTodo = {
        id: uuid,
        text: action.payload.text,
        complete: false
      }
      state.push(newTodo) //람다의 리턴임
    }, 
    toggleTodo: (state, action) => {
      const todo = state.find(todo => todo.id === action.payload)
      if(todo) todo.complete = !todo.complete
    }, 
    deleteTodo: (state, action) => {
      alert(`addTodo 입력값: ${JSON.stringify(action)}`)
      return state.filter((todo) => todo.id !== action.payload.id)
    }
  }
})

export const { addTodo, toggleTodo, deleteTodo } = todoSlice.actions

export default todoSlice.reducer