import Header from "./components/Header/Header"
import './App.css'

function App() {

  return (
    <>
      <Header/>
      <section className="mainsect">
        <h1>Observatório de Projetos - POLI/UPE</h1>
        <input type="search" name="searchbar" id="searchbar" placeholder="Pesquise por nome, tema, palavra-chave"/>
        <div className="curve"></div>
      </section>
      <section className="projectsect">
        <div>
            
        </div>
      </section>
    </>
  )
}

export default App
