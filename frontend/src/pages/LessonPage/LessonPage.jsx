import React from "react";

import s from './LessonPage.module.scss'
import Navbar from "../../components/Navbar/Navbar";
import Lessons from "../../components/Lessons/Lessons";

function LessonPage() {
    return (
        <div className={s.LessonsPage}>
            <Navbar />
            <Lessons />
        </div>
    )
}

export default LessonPage;