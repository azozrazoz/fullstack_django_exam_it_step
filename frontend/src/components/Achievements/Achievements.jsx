import React, { useEffect, useState } from "react";
import axios from 'axios';

function Achievements() {
  const [details, setDetails] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/achievements")
      .then((res) => {
        setDetails(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  return (
    <div>
      <header>Achievements c Django</header>
      <hr></hr>
      {details.map((output, id) => (
        <div key={id}>
          <div>
            <h2>{output.name}</h2>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Achievements;
