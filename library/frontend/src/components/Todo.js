import React from 'react'
import {Link} from 'react-router-dom'


const TodoItem = ({item}) => {
    return (
        <tr>
            <td><Link to={`todo/${item.id}`}>{item.id}</Link></td>
            <td>{item.title}</td>
            <td>{item.content}</td>
        </tr>
    )
}
const TodoList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>CONTENT</th>
                <th>CREATED</th>
            </tr>
            {items.map((item) => <TodoItem item={item}/>)}
        </table>
    )
}
export default TodoList