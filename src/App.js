import React, { Component } from 'react';
import { Button, Segment, Header } from 'semantic-ui-react'
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Segment clearing>
          <Header as='h1' color='blue' floated='left'>Meme</Header>
        </Segment>
      </div>
    );
  }
}

export default App;
