import React, { Component, Fragment } from "react";
import Header from "./components/shared/header";
import NavBarHome from "./components/shared/navbar";

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <NavBarHome />
      </Fragment>
    );
  }
}

export default App;