import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import "bootstrap/dist/css/bootstrap.min.css";
import ErrorPage from './components/shared/errorpage';
import Caso from './components/caso/caso';
import Fascicolo from './components/caso/fascicolo';
import Archivio from './components/archivio/archivio';
import Annotazione from './components/archivio/annotazione';

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />
  }, 
  {
    path: "/casi/",
    element: <Caso />
  }, 
  {
    path: "/fascicoli/",
    element: <Fascicolo />
  }, 
  {
    path: "/archivi/",
    element: <Archivio />
  }, 
  {
    path: "/annotazioni/",
    element: <Annotazione />
  }
])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
