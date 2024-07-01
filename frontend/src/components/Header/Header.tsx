import React from 'react'

function Header() {
  return (
    <header>
        <nav className="navbar">
            <div>
                <ul className="navbar-nav">
                    <li className="nav-item">
                        <a className="nav-link" href="/">Página inicial</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">Navegar</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/inscricao">Publicar</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">Sobre</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/login">Entrar</a>
                    </li>
                </ul>
            </div>
        </nav>
    </header>
  )
}

export default Header