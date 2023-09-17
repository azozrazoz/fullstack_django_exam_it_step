import React, { useState, useEffect } from "react";
import axios from "axios";

function Students() {
  const [details, setDetails] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/students")
      .then((res) => {
        setDetails(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  return (
    <div>
      <header>Students c Django</header>
      <hr></hr>
      {details.map((output, id) => (
        <div key={id}>
          <div>
            <h2>{output.first_name}</h2>
            <p>{output.last_name}</p>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Students;
