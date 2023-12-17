import React from "react";

import s from './AchievementsPage.module.scss'
import Navbar from "../../components/Navbar";
import Achievements from "../../components/Achievements/Achievements";

function AchievemetsPage() {
    return (
        <div className={s.AchievemetsPage}>
            <Navbar />
            <Achievements />
        </div>
    )
}

export default AchievemetsPage;