import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import React from "react";

let movieData = [
  {
    id: "1",
    name: "The Shawshank Redemption",
    release_year: "1994",
    poster_url:
      "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
  },
  {
    id: "2",
    name: "The Godfather",
    release_year: "1972",
    poster_url:
      "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
  },
  {
    id: "3",
    name: "Schindler's List",
    release_year: "1993",
    poster_url:
      "https://image.tmdb.org/t/p/w500/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg",
  }
];
function MoviesTable(props) {
  const { list, onDismiss, searchTerm} = props;
  return (
      <table>
        <thead>
          <tr>
            <th>Id</th>
            <th>Título</th>
            <th>Ano</th>
            <th>URL do Poster</th>
          </tr>
        </thead>
        <tbody>
          {list.filter(movie => movie.name.toLowerCase().includes(searchTerm.toLowerCase()))
          .map((movie) => (
            <tr key={movie.id}>
              <td>{movie.id}</td>
              <td>{movie.name}</td>
              <td>{movie.release_year}</td>
              <td>{movie.poster_url}</td>
              <td>
                <button onClick={() => onDismiss(movie.id)}>Dismiss</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
  );
}
function Search(props) {
  const {searchTerm, handleInputChange} = props;
  return (
      <form>
        <input type="text" placeholder="Search by movie name"
          name="searchTerm"
          value={searchTerm} 
          onChange={(event) => handleInputChange(event)}/>
      </form>
    );
}
class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      list: null, 
      searchTerm: ''
    };
    this.onDismiss = this.onDismiss.bind(this);
    this.onSearchChange = this.onSearchChange.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
  }
  onSearchChange(event) {
    this.setState({ searchTerm: event.target.value });
  }
  handleInputChange(event) {
    const target = event.target;
    const value = 
      target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }
  componentDidMount() {
    fetch('http://127.0.0.1:8000/api/v1/movies/')
      .then((response) => response.json())
      .then((result) => this.setState({ list: result }))
      .catch((error) => console.log(error));
  }
  render() {
    const {list, searchTerm} = this.state;
    return (
      <div className="App">
        <Search
          searchTerm={searchTerm}
          handleInputChange={(e) => this.handleInputChange(e)}
        />
          <MoviesTable list={list} 
            onDismiss={(id) => this.onDismiss(id)}
            searchTerm={searchTerm}
            onSearchChange={(e) => this.onSearchChange(e)}
          />
      </div>
    );
  }
}
export default App;