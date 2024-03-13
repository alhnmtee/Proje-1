import React from 'react';
import { Outlet } from 'react-router-dom';
import { Link } from 'react-router-dom';

const Root = () => {
  return (
    <div className='Root'>
      {/* Boş sayfa içeriği */}
      <h1>Ara Bulursun
      <Link className='link' to="/">Home</Link>
      </h1>
            
            <Outlet></Outlet>
          </div>
  );
};

export default Root;