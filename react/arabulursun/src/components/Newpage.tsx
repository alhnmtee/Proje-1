import React, { useEffect } from 'react';
import { useState } from 'react';
import { useLocation } from 'react-router-dom'; 

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
    <div>
      {/* Boş sayfa içeriği */}
      <h2>Search results</h2>
      <ul>
        {searchResults.map((data) => (
          <li key={data.id}>
            <a href={data.link}>{data.title}</a>
            <p>Authors: {data.authors.join(', ')}</p>
            <p>Date: {data.date}</p>
            <p>Journal: {data.journal_title}</p>
            <p>Keywords: {data.keywords.join(', ')}</p>
            <p>Summary: {data.summary}</p>
            {/* <p>References: {data.references.join(', ')}</p> */}
            <p>URL: 
             <a href={data.url}>{data.url}</a> </p>

          </li>
        ))}
      </ul>

    </div>
  );
};

export default Newpage;
