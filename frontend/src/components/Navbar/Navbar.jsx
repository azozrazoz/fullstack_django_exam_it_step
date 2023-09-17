import './Navbar.module.scss'
import React from 'react';

function Navbar() {
 state = { details: [], }

  return (
    <div>
      <nav>
        <a href="/youtube_test">Youtube_test</a> |
        <a href="/students">Students</a> |
        <a href="/achievements">Achievements</a>
      </nav>
    </div>
  )
}

export default Navbar;
