import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import Header from "./layouts/Header";
import Dashboard from "./dailies/Dashboard";

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <Dashboard />
      </Fragment>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("my-maple"));
