import React from 'react'


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
const BookList = ({books}) => {
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
            {books.map((book_) => <BookItem book={book_} />)}
        </table>
    )
}


export default BookList