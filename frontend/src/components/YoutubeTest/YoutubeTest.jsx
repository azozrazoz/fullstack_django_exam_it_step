import React, { useEffect, useState } from 'react';
import { getYoutubeTestData } from '../../api/youtube';

function YoutubeTest() {
    const [details, setDetails] = useState([]);
 
    useEffect(() => {
        getYoutubeTestData(setDetails);
      }, []);

  return (
    <div>
        <header>{process.env.DJANGO_APP_API_URL}</header>
        <hr></hr>
        {details.map((output, id) => (
        <div key={id}>
            <div>
            <h2>Title: {output.title}</h2>
            <p>Channel: {output.channel}</p>
            </div>
        </div>
        ))}
    </div>
  )
}

export default YoutubeTest;
