import React from 'react';
import { Outlet } from 'react-router-dom';
import { Link } from 'react-router-dom';

const Root = () => {
  return (
    <div className='Root'>
      {/* Boş sayfa içeriği */}
      <h1 className='h1'>
      
      <Link className='link' to="/">Ara Bulursun Akademik</Link>
    </h1>
            
            <Outlet></Outlet>
          </div>
  );
};

export default Root;