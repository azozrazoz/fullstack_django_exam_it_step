import React from "react";

import s from './HomePage.module.scss'
import Navbar from "../../components/Navbar/Navbar";

function HomePage() {
    return (
        <div className={s.homePage}>
            <Navbar />
        </div>
    )
}

export default HomePage;