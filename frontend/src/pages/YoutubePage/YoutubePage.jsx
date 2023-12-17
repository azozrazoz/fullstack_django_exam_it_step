import React, { useState } from "react";
import { postYoutubeTestData } from "../../api/youtube";
import Navbar from "../../components/Navbar/Navbar";
import YoutubeTest from "../../components/YoutubeTest/YoutubeTest";

import s from './YoutubePage.module.scss'

function YoutubePage() {
  const [title, setTitle] = useState("");
  const [channel, setChannel] = useState("");

  return (
    <div>
      <Navbar />

      <form className={s.form} method="post">
        <input type="text" name="title" onClick={setTitle} />
        <input type="text" name="channel" onClick={setChannel} />
        <button type="button" onClick={() => postYoutubeTestData(title, channel)}>Create</button>
      </form>

      <YoutubeTest />
    </div>
  );
}

export default YoutubePage;
