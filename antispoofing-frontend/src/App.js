import React, { useState } from "react";
import logo from './logo.svg';
import './App.css';
import { Login } from "./Login";
import { Signup } from "./Signup";
import UploadImageToS3WithNativeSdk from "./UploadImageToS3WithNativeSdk";

function App() {
  const [currentForm, setCurrentForm] = useState('login');

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }

  return (
    <div className="App">
      {
        currentForm === "login" ? <Login onFormSwitch={toggleForm} /> : <Signup onFormSwitch={toggleForm} />
        //<UploadImageToS3WithNativeSdk/>
      }
    </div>
  );
}

export default App;
