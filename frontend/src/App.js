import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/Users";
import BookList from "./components/Book";
import axios from 'axios';
import {BrowserRouter, Route, Link, Navigate, Routes} from "react-router-dom";
import NotFound404 from "./components/NotFound404";
import BooksUser from "./components/BooksUser";

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
        'users': [],
        'books': [],
    }
  }

  componentDidMount() {
      axios.get('http://127.0.0.1:8000/api/users/')
          .then(response =>{
              this.setState(
                  {'users': response.data
                  }
              )
          }).catch(error => console.log(error))

      axios.get('http://127.0.0.1:8000/api/books/')
          .then(response =>{
              this.setState(
                  {'books': response.data
                  }
              )
          }).catch(error => console.log(error))

  }

      // const users = [
      //   {
      //     'first_name': 'Фёдор',
      //     'last_name': 'Достоевский',
      //     'birthday_year': 1821
      //   },
      //   {
      //     'first_name': 'Александр',
      //     'last_name': 'Грин',
      //     'birthday_year': 1880
      //   },
      // ]
    //   this.setState(
    //       {
    //                 'users': users
    //             }
    //   )
    // }
 // <div>
 //          <getElementById card={this.state.users}/>
 //          <UserList users={this.state.users}/>
 //          <FooterList footers={this.state.users}/>
 //        </div>
// <addEventListener users={this.state.users}/>

  render () {
    return (
        <div>
            <BrowserRouter>
                <nav>
                    <li><Link to='/users'>Users</Link></li>
                    <li><Link to='/books'>Books</Link></li>
                </nav>

                <Routes>
                    <Route exact path='/' element={<Navigate to='/users'/>}/>
                    <Route path='/users'>
                        <Route index element={<UserList users={this.state.users}/>}/>
                        <Route path=':userId' element={<BooksUser books={this.state.books}/>}/>
                    </Route>
                    <Route exact path='/books' element={<BookList books={this.state.books}/>}/>

                    <Route path='*' element={<NotFound404/>}/>
                </Routes>
            </BrowserRouter>
        </div>
    )
  }
}

export default App;
