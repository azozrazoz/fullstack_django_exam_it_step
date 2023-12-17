import React, { useState, useEffect } from "react";
import { getStudent_data } from '../../api/student'

function Students() {
  const [details, setDetails] = useState([]);

  useEffect(() => {
    getStudent_data(setDetails);
  }, []);

  return (
    <div>
      <header>Students c Django</header>
      <hr></hr>
      {details.map((output, id) => (
        <div key={id}>
          <div>
            <h2>{output.name}</h2>
            <p>{output.email}</p>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Students;
