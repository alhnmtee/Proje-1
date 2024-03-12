import React from 'react';
import { Outlet } from 'react-router-dom';
import { Link } from 'react-router-dom';

const Root = () => {
  return (
    <div className='Root'>
      {/* Boş sayfa içeriği */}
      <h1>Ara Bulursun</h1>
      
            <Link to="/">Home</Link>
            <Outlet></Outlet>
          </div>
  );
};

export default Root;