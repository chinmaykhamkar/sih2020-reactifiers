import React, { Component } from "react";
import {Link} from 'react-router-dom';
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../styles/fixedLeft.css';

const FixedLeft =  (props) => {      
   
    const submitColor = { 
        color: 'white',
   }
  

        return(
        <React.Fragment> 
            <div className='leftList mt-4 mb-4'><Link style={submitColor} className="nav-link" to={props+"/market"}>Market</Link></div>
            <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={"home/addProduct"}>Add Product</Link></div>
            <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={"home/qualityIndex"}>Quality Index</Link></div>
            <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={"home/analysis"}>Analysis</Link></div>
            <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={"home/Dashboard"}>Dashboard</Link></div>
            <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={"home/orders"}>Orders</Link></div>
            <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={"home/schemes"}>Schemes</Link></div>
            <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={"home/blogs"}>Blogs</Link></div>
            <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={"home/profile"}>Profile</Link></div>

        </React.Fragment>
        );
    
}

export default FixedLeft;