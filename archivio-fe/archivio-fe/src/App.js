import React, { Component, Fragment } from "react";
import Header from "./components/shared/header";
import NavBarHome from "./components/shared/navbar";
import Home from "./components/shared/home";

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <NavBarHome />
        <Home />
      </Fragment>
    );
  }
}

export default App;