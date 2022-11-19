import React from 'react'
import {useParams} from "react-router-dom";
import book from "./Book";


const BookItem = ({book}) => {
    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name}
            </td>
            <td>
                {book.user}
            </td>
        </tr>
    )
}
const BooksUser = ({books}) => {
    let {userId} = useParams()
    console.log(userId)
    let filter_books = books.filter((book)=> book.users.includes(parseInt(userId)))
    return (
        <table>
            <th>
                Id
            </th>
            <th>
                Name
            </th>
            <th>
                User
            </th>
            {filter_books.map((book_) => <BookItem book={book_} />)}
        </table>
    )
}


export default BooksUser