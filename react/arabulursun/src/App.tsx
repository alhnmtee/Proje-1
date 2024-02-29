import { useEffect } from 'react'
import './App.css'

function App() {
  useEffect(()=>{
    fetch('api/anani')
    .then(res=> console.log(res))
  },[])
  return (
    <>
      <h1>ananı</h1>
    </>
  )
}

export default App
