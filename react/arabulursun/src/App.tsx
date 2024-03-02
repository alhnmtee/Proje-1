import { useInsertionEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { useEffect } from 'react'
import './App.css'



function App() {
  
  useEffect(() => {
    fetch('/api/searchresults')
      .then(response => response.json())
       .then(data => {
        console.log(data);
       })
       .catch(error => {
         console.error('Error fetching data:', error);
       });
  }, []);

  const [inputText, setInputText] = useState('');

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(event.target.value);
  };

  const sendDataToServer = () => {
    fetch('/api/searchwords', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: inputText }),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('Response from server:', data);
    })
    .catch(error => {
      console.error('Error sending data:', error);
    });
  };

  return (
    <div>
      <input type="text" value={inputText} onChange={handleInputChange} />
      <button onClick={sendDataToServer}>Send Data</button>
    </div>
  );
}

export default App


