import React, { useEffect, useState } from 'react'
import { Link, useLocation } from 'react-router-dom';


export default function NavigationCMP() {
    const location = useLocation()
    const [home, setHome] = useState('')
    const [uploadVideo, setUploadVideo] = useState('')
    useEffect(()=>{
        if(location.pathname.includes('upload')){
        setUploadVideo('active');
        setHome('')
    }else{
        setUploadVideo('')
        setHome('active')
    }
    },[location])
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="container">
                <Link className="navbar-brand" to="/app">App</Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item ">
                            <Link className={`nav-link ${home}`} aria-current="page" to="/app">All Videos</Link>
                        </li>
                        <li className="nav-item">
                            <Link className={`nav-link ${uploadVideo}`} to="upload">Upload Video</Link>
                        </li>
                    </ul>
                    <div className="d-flex">
                        <a className="btn btn-outline-danger" href="/logout">Logout</a>
                    </div>
                </div>
            </div>
        </nav>
    )
}
