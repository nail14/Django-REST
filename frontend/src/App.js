import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/Users";
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
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


  render () {
    return (
        <div>
          <addEventListener users={this.state.users}/>
          <UserList users={this.state.users}/>

        </div>
    )
  }
}

export default App;
