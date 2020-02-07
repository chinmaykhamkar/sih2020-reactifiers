import React, { Component } from "react";
import { BrowserRouter , Switch, Route, Link } from "react-router-dom";
import '../styles/home.css';
import FixedLeft from '../components/fixedLeft';
import Market from '../pages/market';
import AddProduct from '../pages/addProduct';
import Blogs from '../pages/blogs';
import Profile from '../pages/profile';
import Dashboard from '../pages/dashboard';
import Schemes from '../pages/schemes';
import QualityIndex from '../pages/qualityIndex';
import Orders from '../pages/orders';
import Analysis from '../pages/analysis';

const Home = ({match}) => {
    const submitColor = { 
        color: 'white',
   }
        return (
            <BrowserRouter>
            
            <div className="main">
                <div className='navBar'>
                    
                </div>
                <div className='mainArea'>
                    <div className='fixedLeft'>
                        <div className='leftList mt-4 mb-4'><Link style={submitColor} className="nav-link" to={`${match.url}/Market`}>Market</Link></div>
                        <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={`${match.url}/AddProduct`}>Add Product</Link></div>
                        <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={`${match.url}/QualityIndex`}>Quality Index</Link></div>
                        <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={`${match.url}/Analysis`}>Analysis</Link></div>
                        <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={`${match.url}/Dashboard`}>Dashboard</Link></div>
                        <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={`${match.url}/Orders`}>Orders</Link></div>
                        <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={`${match.url}/Schemes`}>Schemes</Link></div>
                        <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={`${match.url}/blogs`}>Blogs</Link></div>
                        <div className='leftList mb-4'><Link style={submitColor} className="nav-link" to={`${match.url}/Profile`}>Profile</Link></div>

                    </div>
                    <div className='rightContent'>                        
                    {/* <Route path={`${match.path}/:name`} component={match.name} /> */}
                     <Switch>                        
                        {/* <Route exact path='/' component={Market} /> */}
                        <Route path="home/Market" component={Market} />
                        <Route path="home/AddProduct" component={AddProduct} />
                        <Route path="home/QualityIndex" component={QualityIndex} />
                        <Route path="home/Analysis" component={Analysis} />  
                        <Route path="home/Dashboard" component={Dashboard} />            
                        <Route path="home/Orders" component={Orders} />            
                        <Route path="home/Shemes" component={Schemes} />
                        <Route path="home/Blogs" component={Blogs} />            
                        <Route path="home/Profile" component={Profile} />            
            
                    </Switch> 
          
                    
                    </div>
                </div>

            </div>
        </BrowserRouter>
        );
    
}

export default Home;

