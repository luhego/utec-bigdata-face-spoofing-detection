import React, { useState } from "react";
import './Login.css';
import logo from './logo_UTEC.svg';
import Webcam from "react-webcam";



// Funcion principal Login
export const Login = (props) => {
  const [username, setUserName] = useState('');
  const [password, setPassword] = useState('');

  const [video, setVideo] = useState('');

  // para grabar la webcam
  const [progress, setProgress] = useState(0);//
  const webcamRef = React.useRef(null);
  const mediaRecorderRef = React.useRef(null);
  const [capturing, setCapturing] = React.useState(false);
  const [recordedChunks, setRecordedChunks] = React.useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(video);

    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password)
    formData.append("video", video);

    fetch("http://localhost:1337/api/auth/login", {
      method: "POST",
      body: formData
    })
      .then((response) => response.json())
      .then((data) => console.log(data));

  }

  //Boton de Start, Stop, Download de la cámara 

  const handleStartCaptureClick = React.useCallback(() => {
    setCapturing(true);
    mediaRecorderRef.current = new MediaRecorder(webcamRef.current.stream, {
      mimeType: "video/webm"
    });
    mediaRecorderRef.current.addEventListener(
      "dataavailable",
      handleDataAvailable
    );
    mediaRecorderRef.current.start();
  }, [webcamRef, setCapturing, mediaRecorderRef]);

  const handleDataAvailable = React.useCallback(
    ({ data }) => {
      if (data.size > 0) {
        setRecordedChunks((prev) => prev.concat(data));

      }
    },
    [setRecordedChunks]
  );

  const handleStopCaptureClick = React.useCallback(() => {
    mediaRecorderRef.current.stop();
    setCapturing(false);
  }, [recordedChunks, mediaRecorderRef, webcamRef, setCapturing]);

  const handleDownload = React.useCallback(() => {
    if (recordedChunks.length) {
      const blob = new Blob(recordedChunks, {
        type: "video/webm"
      });

      setVideo(blob);
      console.log(video);

      const url = URL.createObjectURL(blob);

      const a = document.createElement("a");
      document.body.appendChild(a);
      a.style = "display: none";
      a.href = url;
      a.download = "react-webcam-stream-capture.webm";
      a.click();
      window.URL.revokeObjectURL(url);


      setRecordedChunks([]);
    }
  }, [recordedChunks]);

  return (
    <div className="auth-form-container">
      <div className="auth-form-logo">
        <img src={logo}></img>
      </div>
      <h2>Login</h2>
      <form className="login-form" onSubmit={handleSubmit}>
        <label htmlFor="username">Usuario:</label>
        <input value={username} onChange={(e) => setUserName(e.target.value)} type="text" placeholder="Mi usuario" id="username" name="username" required />
        <label htmlFor="password">Contraseña:</label>
        <input value={password} onChange={(e) => setPassword(e.target.value)} type="password" placeholder="********" id="password" name="password" required />

        <label htmlFor="Grabación">Grabación:</label>

        <Webcam audio={false} ref={webcamRef} />
        {capturing ? (
          <button type="button" className='botonStop' onClick={handleStopCaptureClick}>Stop Capture</button>
        ) : (
          <button type="button" className='botonStart' onClick={handleStartCaptureClick}>Start Capture</button>
        )}
        {recordedChunks.length > 0 && (
          <button type="button" className='botonDownload' onClick={handleDownload}>Download</button>
          //<h2> Video Grabado!</h2>
        )}

        <button type="submit">Log In</button>
      </form>
      <button className="link-btn" onClick={() => props.onFormSwitch('signup')}>¿Todavía no tienes una cuenta? Registrate aqui.</button>

    </div>
  )
}