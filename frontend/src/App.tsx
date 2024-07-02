import Header from "./components/Header/Header"

function App() {
  return (
    <>
      <Header/>
      <section className="">
        <div className="bg-primary-color w-full py-14 relative flex flex-col items-center">
            <h1 className="text-2xl font-bold text-center text-light-color">Observatório de Projetos - POLI/UPE</h1>
            <input 
              type="search" 
              name="searchbar" 
              id="searchbar" 
              className="rounded-full w-[70%] h-[5vh] border border-light-color indent-2 mt-8"
              placeholder="Pesquise por nome, tema, palavra-chave"
            />
        </div>
        <svg className="bottom-0 w-full" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
          <path fill="#1F7A8C" fill-opacity="1" d="M0,96L60,90.7C120,85,240,75,360,64C480,53,600,43,720,58.7C840,75,960,117,1080,128C1200,139,1320,117,1380,106.7L1440,96L1440,0L1380,0C1320,0,1200,0,1080,0C960,0,840,0,720,0C600,0,480,0,360,0C240,0,120,0,60,0L0,0Z"></path>
        </svg>
      </section>  

      <section className="projectsect grid grid-cols-4 grid-rows-2">
        <div className=" ml-[15vw] bg-gray-500 h-[20vh] w-[25vw]">
        </div>
      </section>
    </>
  )
}

export default App
