import React, { useState, useEffect } from "react";

import s from './ProfilePage.module.scss'
import Navbar from "../../components/Navbar/Navbar";
import { getStudent_data } from '../../api/student'

function ProfilePage() {
    const [details, setDetails] = useState([]);

    useEffect(() => {
        getStudent_data(setDetails);
    }, []);

    return (
        <div className={s.ProfilePage}>
            <Navbar />
            
            {details.map((output, id) => (
                <div key={id}>
                    <div>
                        <h2>Name: {output.name}</h2>
                        <h2>Surname: {output.surname}</h2>
                    </div>
                    <div>
                        <h2>Age: {output.age}</h2>
                        <h2>Email: {output.email}</h2>
                        <button>Change password</button>
                        <h2>Group: {output.group}</h2>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default ProfilePage;