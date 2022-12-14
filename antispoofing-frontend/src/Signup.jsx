import React, { useState, useEffect } from "react";

import './Signup.css';
import logo from './logo_UTEC.svg';
import Webcam from "react-webcam";
import AWS from 'aws-sdk'

const S3_BUCKET = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;
const REGION = process.env.REACT_APP_AWS_S3_REGION_NAME;


AWS.config.update({
  accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY
})

const bucket = new AWS.S3({
  params: { Bucket: S3_BUCKET },
  region: REGION,
})

// Funcion principal SignUP
export const Signup = (props) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [username, setUserName] = useState('');
  const [genre, setGender] = useState('');

  const [video, setVideo] = useState('');

  // para grabar la webcam
  const webcamRef = React.useRef(null);
  const mediaRecorderRef = React.useRef(null);
  const [capturing, setCapturing] = React.useState(false);
  const [recordedChunks, setRecordedChunks] = React.useState([]);

  const updateVideo = async () => {
    console.log("Setting video")
    console.log(recordedChunks)
    if (recordedChunks.length) {
      const blob = new Blob(recordedChunks, {
        type: "video/webm"
      });

      setVideo(blob);
    } else {
      console.log("No video recorded")
    }
  }

  useEffect(() => {
    if (video !== "") {
      // Generate hexadecimal code for video
      const videoHexCode = Array.from(crypto.getRandomValues(new Uint8Array(32)))
        .map(b => b.toString(16).padStart(2, '0')).join('');
      const filename = `${videoHexCode}.webm`;
      const params = {
        Body: video,
        Bucket: S3_BUCKET,
        Key: filename
      };

      const videoURL = `s3://${S3_BUCKET}/${filename}`

      // Upload video to S3
      bucket.putObject(params).promise().then((d) => {
        console.log(d)

        const data = {
          username: username,
          email: email,
          genre: genre,
          password: password,
          video_s3_url: videoURL,
        }

        fetch("http://localhost:1337/api/auth/signup", {
          method: "POST",
          mode: "cors",
          cache: "no-cache",
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data)
        })
          .then((response) => response.json())
          .then((data) => console.log(data));
      }).catch((err) => {
        console.log(err)
      })
    }
  }, [video]);

  const handleSubmit = (e) => {
    e.preventDefault();

    updateVideo();
  }

  //Boton de Start, Stop, Download de la c??mara 
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
      <h2>Signup</h2>
      <form className="register-form" onSubmit={handleSubmit}>
        <label htmlFor="name">Nombre Completo:</label>
        <input value={name} onChange={(e) => setName(e.target.value)} type="text" name="name" id="name" placeholder="Nombre Completo" required />
        <label htmlFor="genre">G??nero:</label>
        <input value={genre} onChange={(e) => setGender(e.target.value)} type="text" name="genre" id="genre" placeholder="G??nero" />
        <label htmlFor="email">Correo:</label>
        <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="ejemplodecorreo@gmail.com" id="email" name="email" required />
        <label htmlFor="nick">Usuario:</label>
        <input value={username} onChange={(e) => setUserName(e.target.value)} type="text" name="username" id="username" placeholder="Usuario" required />
        <label htmlFor="user">Contrase??a:</label>
        <input value={password} onChange={(e) => setPassword(e.target.value)} type="password" placeholder="********" id="password" name="password" required />

        <label htmlFor="user">Grabaci??n:</label>

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

        <button type="submit">Registrar</button>

      </form>
      <button className="link-btn" onClick={() => props.onFormSwitch('login')}>??Ya tienes una cuenta? Ingresa aqui.</button>

    </div>


  )
}