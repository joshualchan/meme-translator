import React, { Component } from 'react';
import { Header, Icon, Image, Button } from 'semantic-ui-react'
import logo from './logo.svg';
import './App.css';

// const app = () => (
//   <div>
//     <Header as='h1' icon textAlign='center'>
//       <Icon name='thumbs up outline' circular />
//       <Header.Content>Meme Translator</Header.Content>
//     </Header>
//     <Button basic color='black' content='Black'/>
//   </div>
 

// );

// export default app

class App extends Component {
  render() {
    return (
      <div className="App">
       <Header as='h1' icon textAlign='center'>
         <Icon name='thumbs up outline' circular />
         <Header.Content>Meme Translator</Header.Content>
     </Header>
     <Button class='button' basic color='black' content='Translate me!'/>
   </div>
    );
  }
}

export default App;
