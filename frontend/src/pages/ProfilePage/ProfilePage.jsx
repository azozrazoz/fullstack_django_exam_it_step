import React from "react";

import s from './ProfilePage.module.scss'
import Navbar from "../../components/Navbar/Navbar";

function ProfilePage() {
    return (
        <div className={s.homePage}>
            <Navbar />
            Profile
        </div>
    )
}

export default ProfilePage;