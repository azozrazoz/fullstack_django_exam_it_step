import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import { Achievements } from './components/Achievements'
import { Students } from './components/Students';
import YoutubeTest from './components/YoutubeTest';
 
class App extends React.Component {

 render() {
  return (
    <Router>      
      <div>       
        <Switch>
          <Route path='/youtube_test'>
            <YoutubeTest />
          </Route>
        </Switch>
        <Switch>
          <Route path='/achievements'>
            <Achievements></Achievements>
          </Route>
        </Switch>
        <Switch>
          <Route path='/students'>
            <Students></Students>
          </Route>
        </Switch>
      </div>
    </Router>
  )
 }
}

export default App;
