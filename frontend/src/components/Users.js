import React from 'react'
import {Link} from "react-router-dom";


const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                <Link to={`/users/${user.id}`}>{user.first_name}</Link>
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.birthday_year}
            </td>
        </tr>
    )
}
const UserList = ({users}) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Birthday year
            </th>
            {users.map((user_) => <UserItem user={user_} />)}
        </table>
    )
}


export default UserList