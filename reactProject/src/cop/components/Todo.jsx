import React from 'react';
import { useDispatch } from "react-redux";
import { deleteTodo } from "../reducers/todo.reducer";

const Todo = ({ id, title }) => {

	const dispatch = useDispatch();

	const onClick=()=>{
		dispatch(
			deleteTodo({
				id: id
			})
		)
	}

	return (
		<li className="task-item">
				{title}
				<button className="remove-task-button" onClick={onClick}>Delete</button>
		</li>
	);
};

export default Todo;