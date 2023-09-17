import React from "react";

import s from './LessonPage.module.scss'
import Navbar from "../../components/Navbar/Navbar";

function LessonPage() {
    return (
        <div className={s.homePage}>
            <Navbar />
        </div>
    )
}

export default LessonPage;