import React from "react";
import { BrowserRouter, Route, Routes } from 'react-router-dom'

import HomePage from "./pages/HomePage";
import LessonPage from "./pages/LessonPage";
import ProfilePage from "./pages/ProfilePage";
import YoutubePage from './pages/YoutubePage'

function Router() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage />}/>
                <Route path="/lesson" element={<LessonPage />}/>
                <Route path="/profile" element={<ProfilePage />}/>
                <Route path="/youtube" element={<YoutubePage />}/>
            </Routes>
        </BrowserRouter>
    )
}

export default Router;