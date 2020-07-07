import React from 'react';
import logo from './logo.svg';
import './App.css';

import StarRating from './components/StarRating'
import Topic from './components/Topic'
import SurveyThankYou from "./components/SurveyThankYou";
import {Route,Link} from "react-router-dom"


function App() {
  return (
    <div className="App">

      <div class="inner">
        <Route path="/" exact component={Topic}/>
         <Route path='/thank_you' exact component={SurveyThankYou}/>
      </div>
    </div>
  );
}

export default App;
