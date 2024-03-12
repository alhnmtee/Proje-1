import React, { useState, useEffect } from 'react';

function App() {
  interface SearchResult {
    id: number; // Ensure 'id' is also included in the interface
    title: string;
    link: string;
  }
  interface Filter {
    type: string;
    title: string;
    date: string;
    keywords: string;
    link: string;
  }

  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);
  const [typeFilter, setTypeFilter] = useState<string | null>(null);
  const [titleFilter, setTitleFilter] = useState<string>('');
  const [dateFilter, setDateFilter] = useState<string | null>(null);
  const [keywordsFilter, setKeywordsFilter] = useState<string>('');
  const [authorFilter, setAuthorFilter] = useState<string>('');
  const [jsonData, setJsonData] = useState<Filter[]>([]);
  const [inputText, setInputText] = useState<string>('');

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
        console.log('Response from server:1', data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

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

  const handleFilter = () => {
    const filters = {
      type: typeFilter,
      title: titleFilter,
      date: dateFilter,
      keywords: keywordsFilter
    };

    const jsonData = JSON.stringify(filters);
    fetch('/api/filters', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: jsonData,
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(jsonData => {
        // Veriyi işle ve uygun yapıya dönüştür
        const searchResultObjects = jsonData.map((item, index) => ({
          id: index,
          title: item.title,
          link: item.title
        }));
      
        // Arayüzü güncelle
        setSearchResults(searchResultObjects);
        console.log('Response from server:', jsonData);
      })
      
      .catch(error => {
        console.error('Error sending data:', error);
      });

    setTypeFilter("");
    setTitleFilter("");
    setDateFilter("");
    setKeywordsFilter("");
    setAuthorFilter("");
  };

  return (
    <div >
      <div >
        <select value={typeFilter} onChange={(e) => setTypeFilter(e.target.value)}>
          <option value="">Type</option>
          <option value="Araştırma Makalesi">Araştırma Makalesi</option>
          <option value="Derleme">Derleme</option>
          <option value="Diğer">Diğer</option>
        </select>
        <input type="text" value={titleFilter} onChange={(e) => setTitleFilter(e.target.value)} placeholder="Title" />
        <input type="text" value={dateFilter} onChange={(e) => setDateFilter(e.target.value)} placeholder="Date" />
        <input type="text" value={keywordsFilter} onChange={(e) => setKeywordsFilter(e.target.value)} placeholder="Keywords" />
        <input type="text" value={authorFilter} onChange={(e) => setAuthorFilter(e.target.value)} placeholder="Author" />
        <button onClick={handleFilter}>Filtrele</button>
      </div>

      <div >
        <input type="text" value={inputText} onChange={handleInputChange} />
        <button onClick={sendDataToServer}>Send Data</button>
      </div>

      <h1 >Search Results</h1>
      <ul >
        {searchResults.map((item, index) => (
          <li key={index}>
            <a href={'article/' + item.link} target="_blank">{item.link}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
