import React, { Component } from "react";
import {Redirect,Link} from 'react-router-dom';

const Login = () => {
    
    const submitColor = { 
        color: 'white',
   }    
        return (

            <div className="App">
      <nav className="navbar navbar-expand-lg navbar-light fixed-top">
        <div className="container">
          <Link className="navbar-brand" to={"/sign-in"}>REACTifiers</Link>
          <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
            <ul className="navbar-nav ml-auto">
              <li className="nav-item">
                <Link className="nav-link" to={"/sign-in"}>Login</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to={"/sign-up"}>Sign up</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="auth-wrapper">
        <div className="auth-inner">
        <form>
                <h3>Sign In</h3>

                <div className="form-group">
                    <label>Email address</label>
                    <input type="email" className="form-control" placeholder="Enter email" required />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" required />
                </div>

                

                <button type="submit" className="btn btn-primary btn-block"><Link style={submitColor} to="/home">Submit</Link></button>
                <p className="forgot-password text-right">
                    Don't have a account? <Link to="/sign-up">sign up?</Link>
                </p>
            </form>
        </div>
      </div>
    </div>
           
        );
    
}

export default Login;