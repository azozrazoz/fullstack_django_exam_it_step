import React from "react";

import NavBar from '../../components/Navbar'
import Students from '../../components/Students'

import s from './StudentsPage.module.scss'

function StudentsPage() {
    return (
        <div className={s.StudentsPage}>
            <NavBar />
            <Students />
        </div>
    )
}

export default StudentsPage;