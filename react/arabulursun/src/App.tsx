import { useInsertionEffect, useState } from 'react'
import { useEffect } from 'react'
import './App.css'



function App() {
<<<<<<< Updated upstream
<<<<<<< Updated upstream
  
=======
  interface SearchResult {
    id: number; // Ensure 'id' is also included in the interface
    title: string;
    link: string;
  }

  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);
  const [typeFilter, setTypeFilter] = useState<string | null>(null);
  const [titleFilter, setTitleFilter] = useState<string>('');
  const [dateFilter, setDateFilter] = useState<string | null>(null);
  const [keywordsFilter, setKeywordsFilter] = useState<string>('');


  useEffect(() => {
    // Fetch data and set search results here
  }, []); // useEffect dependency array

  // Filtered results based on filters
 
>>>>>>> Stashed changes
=======
  
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======

  
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
  //Filtre yapılan verilerin kaydedilmesi ve jsona çevrilmesi
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
      console.log('Response from server:', jsonData);
    })
    .catch(error => {
      console.error('Error sending data:', error);
    });
   
  
    // Filtre değerlerini temizle
    setTypeFilter("");
    setTitleFilter("");
    setDateFilter("");
    setKeywordsFilter("");
  };
  
  
  

  
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
  return (
    <div>
       {/* Filter inputs */}
       <div>
        <select value={typeFilter} onChange={(e) => setTypeFilter(e.target.value)}>
          <option value="">Type</option>
          <option value="Araştırma Makalesi">Araştırma Makalesi</option>
          <option value="Derleme">Derleme</option>
          <option value="Diğer">Diğer</option>
        </select>
        <input type="text" value={titleFilter} onChange={(e) => setTitleFilter(e.target.value)} placeholder="Title" />
        <input type="text" value={dateFilter} onChange={(e) => setDateFilter(e.target.value)} placeholder="Date" />
        <input type="text" value={keywordsFilter} onChange={(e) => setKeywordsFilter(e.target.value)} placeholder="Keywords" />
        <button onClick={handleFilter}>Filtrele</button>
      </div>
     
      <input type="text" value={inputText} onChange={handleInputChange} />
      <button onClick={sendDataToServer}>Send Data</button>
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======

      <h1>Search Results</h1>
      <ul>
      {searchResults.map((item, index) => (
  <li key={index}>
    {item.link ? (
      <a href={item.link} target="_blank">{item.link}</a>
    ) : (
      <span>{item.link}</span>
    )}
  </li>
))}




</ul>

      
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
    </div>
  );
}

export default App
