import { useInsertionEffect, useState } from 'react'
import { useEffect } from 'react'
import './App.css'
import { json } from 'react-router-dom';



function App() {
  interface SearchResult {
    id: number; // Ensure 'id' is also included in the interface
    link: string;
  }

  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);
  useEffect(() => {
    fetch('/api/searchresults')
      .then(response => response.json())
      .then(data => {
        const searchResultObjects = data.map((link, index) => ({
          id: index,
          title: `Title ${index + 1}`,
          link: link
        }));
        setSearchResults(searchResultObjects);
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

      <h1>Search Results</h1>
      <ul>
      {searchResults.map((item, index) => (
  <li key={index}>
    {item.link ? (
      <a href={item.link}>{item.link}</a>
    ) : (
      <span>{item.link}</span>
    )}
  </li>
))}



</ul>

      
    </div>
    
  );
}

export default App
