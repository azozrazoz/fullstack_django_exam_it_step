import React from "react";
import { BrowserRouter, Route, Routes } from 'react-router-dom'

import HomePage from "./pages/HomePage";
import LessonPage from "./pages/LessonPage";
import ProfilePage from "./pages/ProfilePage";
import YoutubePage from './pages/YoutubePage';
import StudentPage from './pages/StudentPage';

function Router() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage />}/>
                <Route path="/lessons" element={<LessonPage />}/>
                <Route path="/achievements" element={<ProfilePage />}/>
                <Route path="/students" element={<StudentPage />}/>
                <Route path="/profile" element={<ProfilePage />}/>
                <Route path="/youtube" element={<YoutubePage />}/>
            </Routes>
        </BrowserRouter>
    )
}

export default Router;