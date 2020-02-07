import React from 'react';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import Login from "./pages/login";
import SignUp from "./pages/signup";
import Otp from './pages/otp';
import Home from './pages/home';


function App() {
  return (<Router>
    

    <Switch>
            <Route exact path='/' component={Login} />
            <Route path="/sign-in" component={Login} />
            <Route path="/sign-up" component={SignUp} />
            <Route path="/otp" component={Otp} />
            <Route path="/home" component={Home} />
            
            
    </Switch>   
    

    </Router>
  );
}

export default App;