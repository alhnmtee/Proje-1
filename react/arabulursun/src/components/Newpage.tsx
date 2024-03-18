import axios from 'axios';
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
    referances:Array<string>;
    article_url:string;
    pdf_url:string;
    showReferences: boolean;
    cites:number;
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
        setSearchResults(data); 
      } else if (typeof data === 'object' && data !== null) {
        const dataArray = Object.keys(data).map(key => data[key]);
        setSearchResults(dataArray);
        console.log('Response from server:', data);
      } else {
        console.error('Received data is not an array or object:', data);
      }
    })
   
    .catch(error => {
      console.error('Error sending data:', error);
    });
    
  };
  const handleReferencesClick = (data) => {
    data.showReferences = !data.showReferences;
    setSearchResults([...searchResults]);
  };

const downloadPDF = async (pdfUrl: string) => {
    try {
      const pdf_url  = "../public/"+pdfUrl+".pdf";
      const link = document.createElement('a');
      link.href = pdf_url;
      link.download = pdfUrl;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (error) {
      console.error('Error downloading PDF:', error);
    }
  };
 
  
  return (
    <div className="newpage">
      <ul>
        {searchResults.map((data) => (
          <li key={data.id} className="card">
            <p className="card-text journal_title">{data.journal_title}</p>
            <div className="card-body">
              <h2 className="card-title"><a href={data.link}>{data.title}</a></h2>
              <p className="card-text authors">{data.authors.join(", ")}</p> 
              <p className="card-text date">{data.date}</p>
            </div>
            <p className="card-text keywords">Keywords: {data.keywords.join(", ")}</p> 
            <p className="card-text cites">Cites: {data.cites}</p>
            <div className="card-body summary">
              {data.summary}
            </div>
            

            <p><a href={data.article_url} className="btn btn-primary">Article URL</a></p>
            <a href={data.pdf_url} className="btn btn-primary">PDF URL</a>
           
            <p><button className="btn btn-primary" onClick={() => downloadPDF(data.title)}>PDF indir</button></p>
            <p><button className="btn btn-primary" onClick={() => handleReferencesClick(data)}>References</button></p>
            {data.showReferences && ( // data.showReferences kontrolü
              <div className="card-body references">
                
                <ul>
                  {data.referances?.map((reference, index) => (
                    <li key={index}>{reference}</li>
                  ))}
                </ul>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Newpage;
