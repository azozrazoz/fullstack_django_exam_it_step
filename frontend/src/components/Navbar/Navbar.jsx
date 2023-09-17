import React from "react";

import { Link } from "react-router-dom";

import s from "./Navbar.module.scss";

function Navbar() {
  return (
    <div className={s.container}>
      <Link className={s.h2} to="/">
        {process.env.REACT_APP_LOGO_NAME}
      </Link>
      <nav>
        <Link className={s.h2} to="/youtube_test">
          Youtube_test
        </Link>
        <Link className={s.h2} to="/students">
          Students
        </Link>
        <Link className={s.h2} to="/achievements">
          Achievements
        </Link>
      </nav>
      <Link className={s.h2} to="/profile">
        Profile
      </Link>
    </div>
  );
}

export default Navbar;
