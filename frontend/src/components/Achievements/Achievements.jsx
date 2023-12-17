import React, { useEffect, useState } from "react";=

import { getAchievements_data } from "../../api/achievements";

function Achievements() {
  const [details, setDetails] = useState([]);

  useEffect(() => {
    getAchievements_data(setDetails)
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
