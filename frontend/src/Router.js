import React from "react";
import { BrowserRouter, Route, Routes } from 'react-router-dom'

import HomePage from "./pages/HomePage";
import LessonPage from "./pages/LessonPage";
import ProfilePage from "./pages/ProfilePage";

import YoutubeTest from './components/YoutubeTest'

function Router() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage />}/>
                <Route path="/lesson" element={<LessonPage />}/>
                <Route path="/profile" element={<ProfilePage />}/>
                <Route path="/youtube_test" element={<YoutubeTest />}/>
            </Routes>
        </BrowserRouter>
    )
}

export default Router;