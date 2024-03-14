
import React, { useEffect } from 'react';
import { useState } from 'react';
import { useLocation } from 'react-router-dom'; 
import '../index.css';
import 'animate.css';


const Newpage = () => {

  interface SearchResult {
    id: number; 
    title: string;
    link: string;
    authors:Array<string>;
    date:string;
    journal_title:string;
    keywords:Array<string>;
    summary:string;
    references:Array<string>;
    url:string;
  }

  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);
  const location = useLocation(); 

  useEffect(() => {
    sendDataToServer(); 
  }, []); 

  const sendDataToServer = () => {
    fetch('/api/url', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: location.pathname }),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('Response from server:', data);
      if (Array.isArray(data)) {
        setSearchResults(data); // Gelen veri zaten bir dizi ise, direkt olarak kullanabiliriz
      } else if (typeof data === 'object' && data !== null) {
        // Gelen veri bir nesne ise, onu bir diziye dönüştürebiliriz
        const dataArray = Object.keys(data).map(key => data[key]);
        setSearchResults(dataArray);
      } else {
        console.error('Received data is not an array or object:', data);
      }
    })
   
    .catch(error => {
      console.error('Error sending data:', error);
    });
  };

  return (
    <div className="newpage">
      <div className="book-animation">
      <img src="../../public/pikachu.png"  className="animate__animated animate__slideInLeft" />
      <img src="../../public/gotcha.png"  className="animate__animated animate__slideInRight" />
    </div>
      <ul>
        {searchResults.map((data) => (
          <li key={data.id} className="card">
            <div className="card-body">
              <h2 className="card-title"><a href={data.link}>{data.title}</a></h2>
              <p className="card-text authors">Yazarlar: {data.authors.join(", ")}</p>
              <p className="card-text date">Tarih: {data.date}</p>
            </div>
            <p className="card-text journal_title">Dergi: {data.journal_title}</p>
            <div className="card-body summary">
              {data.summary}
            </div>
            <p className="card-text keywords">Keywords: 
              {data.keywords.map((keyword) => (
                <span key={keyword} className="badge badge-primary">{keyword}</span>
              ))}
            </p>
            <a href={data.url} className="btn btn-primary">PDF URL</a>
            
    
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Newpage;
