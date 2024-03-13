import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import './App.css'
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import Newpage from './components/Newpage.tsx';
import Root from './components/Root.tsx';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    children: [
      {
        path: "/",
        element: <App />,
        index:true,
      },
      {
        path:"/article/:id",
        element:<Newpage/>,
      }
    ],
    
  },
  {
    
  }
]);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);