import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src="/assets/logo.jpg"
          alt="logo"
          width="300"
        />
        <h3>Dipartimento</h3>
      </div>
    );
  }
}

export default Header;