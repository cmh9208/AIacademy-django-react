import { combineReducers} from "@reduxjs/toolkit"
import todoReducer from "cop/reducers/todo.reducer"

export default combineReducers({
    todos: todoReducer
})