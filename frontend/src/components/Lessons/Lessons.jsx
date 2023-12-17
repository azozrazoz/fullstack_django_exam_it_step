import React, { useEffect, useState } from "react";
import { getLessons_data } from "../../api/lessons";

import s from './Lessons.module.scss'

function Lessons() {
    const [details, setDetails] = useState([]);

    useEffect(() => {
        getLessons_data(setDetails)
    }, [])

    return (
        <div className={s.Lessons}>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Date</th>
                        <th>Type</th>
                        <th>Title</th>
                        <th>Group</th>
                        <th>Online</th>
                        <th>Start time</th>
                        <th>End time</th>
                    </tr>
                </thead>
                <tbody>
                    {details.map((output, id) => (
                        <tr key={id}>
                            <td>{output.name}</td>
                            <td>{output.date}</td>
                            <td>{output.lesson_type}</td>
                            <td>{output.title}</td>
                            <td>{output.group}</td>
                            <td>{output.online}</td>
                            <td>{output.start_time}</td>
                            <td>{output.end_time}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default Lessons