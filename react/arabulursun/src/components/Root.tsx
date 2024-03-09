import React from 'react';
import { Outlet } from 'react-router-dom';


const Root = () => {
  return (
    <div className='Root'>
      {/* Boş sayfa içeriği */}
      <h1>Root</h1>
      <Outlet></Outlet>
    </div>
  );
};

export default Root;