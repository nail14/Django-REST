import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/Users";
import BookList from "./components/Books";
import axios from 'axios';
import {BrowserRouter, Route, Link, Navigate, Routes, useLocation} from "react-router-dom";
import NotFound404 from "./components/NotFound404";
import Loginform from "./components/Auth";
import BooksUser from "./components/BooksUser";
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie";
import books from "./components/Books";
import BookForm from "./components/BookForm";

class App extends React.Component {
  constructor(props) {
      super(props)
      this.state = {
          'users': [],
          'books': [],
      }
  }

  create_book(name, users) {
      const headers = this.get_headers()
      const data = {name: name, users: users}
      axios.post(`http://127.0.0.1:8000/api/books/`,data, {headers}).then(response => {
          this.load_data()
      }).catch(error => {
          console.log(error)
          this.setState({books:[]})})
  }

  delete_book(id) {

      const headers = this.get_headers()
      axios.delete(`http://127.0.0.1:8000/api/books/${id}`, {headers}).then(response => {
          this.load_data()
      }).catch(error => {
          console.log(error)
          this.setState({books:[]})})
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

  load_data() {
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



  render() {
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
                    <Route exact path='/books' element={<BookList books={this.state.books} delete_book={(id)=>this.delete_book(id)}/>}/>
                    <Route exact path='/books/create' element={<BookForm users={this.state.users} create_book={(name,users)=>this.create_book(name,users)}/>}/>
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
