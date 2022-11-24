import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/Users";
import BookList from "./components/Book";
import axios from 'axios';
import {BrowserRouter, Route, Link, Navigate, Routes} from "react-router-dom";
import NotFound404 from "./components/NotFound404";
import Loginform from "./components/Auth";
import BooksUser from "./components/BooksUser";
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie";

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
        'users': [],
        'books': [],
    }
  }

  logout(){
      this.set_token('')
      this.setState({'books' : []})
      this.setState({'users' : []})

  }

  is_auth() {
      return !!this.state.token

  }

  set_token(token){
      console.log(token)
      const cookies = new Cookies()
      cookies.set('token',token)
      this.setState({'token':token},()=>this.load_data())

  }

  get_token_storage(){
      const cookies = new Cookies()
      const token = cookies.get('token')
      this.setState({'token':token},()=>this.load_data())

  }

  get_token(username,password){
      const data = {username:username,password:password}
      axios.post('http://127.0.0.1:8000/api-token',data).then(response => {
          this.set_token(response.data['token'])
      }).catch(error => alert('Неверный логин или пароль'))
  }

  get_headers(){
      let headers = {
          'Content-Type': 'application/json'
      }
      if (this.is_auth()){
          headers['Authorization'] = 'Token '+this.state.token
      }
      return headers

  }

  load_data(){
      const headers =this.get_headers()
      axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(response =>{
              this.setState(
                  {'users': response.data
                  }
              )
          }).catch(error => console.log(error))

      axios.get('http://127.0.0.1:8000/api/books/', {headers})
          .then(response =>{
              this.setState(
                  {'books': response.data
                  }
              )
          }).catch(error => console.log(error))

  }


  componentDidMount() {
      this.get_token_storage()
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
                    <li>{this.is_auth() ?<button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}</li>
                </nav>

                <Routes>
                    <Route exact path='/' element={<Navigate to='/users'/>}/>
                    <Route path='/users'>
                        <Route index element={<UserList users={this.state.users}/>}/>
                        <Route path=':userId' element={<BooksUser books={this.state.books}/>}/>
                    </Route>
                    <Route exact path='/books' element={<BookList books={this.state.books}/>}/>
                    <Route exact path='/login' element={<LoginForm get_token={(username,password) =>
                    this.get_token(username,password)} />}/>

                    <Route path='*' element={<NotFound404/>}/>
                </Routes>
            </BrowserRouter>
        </div>
    )
  }
}

export default App;
