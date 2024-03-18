import React, { useState, useEffect } from 'react';


function App() {
  interface SearchResult {
    date: string | number | Date;
    id: number; 
    title: string;
    link: string;
  }
  interface Filter {
    type: string;
    title: string;
    date: string;
    keywords: string;
    link: string;
    url: string;
    sortOrder: string;
  }

  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);
  const [typeFilter, setTypeFilter] = useState<string | null>(null);
  const [titleFilter, setTitleFilter] = useState<string>('');
  const [dateFilter, setDateFilter] = useState<string | null>(null);
  const [keywordsFilter, setKeywordsFilter] = useState<string>('');
  const [authorFilter, setAuthorFilter] = useState<string>('');
  const [jsonData, setJsonData] = useState<Filter[]>([]);
  const [inputText, setInputText] = useState<string>('');
  const [pages,setpages] = useState<number>(1);
  const [filterSuccess, setFilterSuccess] = useState(false); 
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc');
  

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
  
  const handlePageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setpages(parseInt(event.target.value));
  };
  const sendDataToServer = () => {
    fetch('/api/searchwords', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: inputText , pages : pages }),
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        
        return response.json();
      })
      .then(data => { 
        console.log('Response from server:2', data);
        setTitleFilter(inputText);
        handleFilter();

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
      keywords: keywordsFilter,
      authors: authorFilter,
      sortOrder: sortOrder
      
      
    }
    setFilterSuccess(true); 
    setTimeout(() => {
      setFilterSuccess(false);
    }, 3000);
    ;
    

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
        const searchResultObjects = jsonData.map((item, index) => ({
          id: index,
          title: item.title,
          link: item.title,
          url: item.url
        }));
      
        setSearchResults(searchResultObjects);
        console.log('Response from server:3', jsonData);
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
  const handleSortToggle = () => {
    // Toggle sort order
    const newSortOrder = sortOrder === 'asc' ? 'desc' : 'asc';
    setSortOrder(newSortOrder);

  };

  return (
    <div className='App' >
      <div >
      {filterSuccess && (
        <div>
          <p>Filtreleme başarıyla uygulandı!</p>
        </div>
      )}
        <select value={typeFilter || ""} onChange={(e) => setTypeFilter(e.target.value)}>
          <option value="">Type</option>
          <option value="Araştırma Makalesi">Araştırma Makalesi</option>
          <option value="Derleme">Derleme</option>
          <option value="Diğer">Diğer</option>
        </select>
        <input type="text" value={titleFilter} onChange={(e) => setTitleFilter(e.target.value)} placeholder="Title" />
        <input type="text" value={dateFilter || ""} onChange={(e) => setDateFilter(e.target.value)} placeholder="Date" />
        <input type="text" value={keywordsFilter} onChange={(e) => setKeywordsFilter(e.target.value)} placeholder="Keywords" />
        <input type="text" value={authorFilter} onChange={(e) => setAuthorFilter(e.target.value)} placeholder="Author" />
        <button onClick={handleSortToggle}>
          {sortOrder === 'asc' ? 'Artan Sırala' : 'Azalan Sırala'}
          {sortOrder === 'asc' ? <span>&uarr;</span> : <span>&darr;</span>}
        </button>
        <button onClick={handleFilter}>Filtrele</button>
       
        
        
      </div>

      <div >
        <input type="text" value={inputText} onChange={handleInputChange} />
        <input type="number" value = {pages} min={1} onChange={handlePageChange}/>
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
