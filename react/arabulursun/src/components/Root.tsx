import React from 'react';
import { Outlet } from 'react-router-dom';
import { Link } from 'react-router-dom';
import 'animate.css';

const Root = () => {

  
  return (
    <div className='Root'>
   
    
      <h1 className='h1'>
      
     <div className="animate__animated animate__bounce animate__infinite"><Link className='link'  to="/">Ara Bulursun Akademik</Link></div> 
      <div className="book-animation">
      <img src="../../public/pikachu.png" alt="Left Book" className="animate__animated animate__slideInLeft" />
      <img src="../../public/gotcha.png" alt="Right Book" className="animate__animated animate__slideInRight" />
    </div>
    </h1>

            
            <Outlet></Outlet>
          </div>
  );
};

export default Root;