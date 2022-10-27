import React from 'react'


const FooterItem = ({footer}) => {
    return (
        <tr>
            <td>
                {footer.first_name}
            </td>
            <td>
                {footer.last_name}
            </td>
            <td>
                {footer.birthday_year}
            </td>
        </tr>
    )
}
const FooterList = ({footers}) => {
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
            {footers.map((footer) => <FooterItem footer={footer} />)}
        </table>
    )
}


export default FooterList