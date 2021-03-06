import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import Header from './layouts/Header';
import Dashboard from './dailies/Dashboard';

import { Provider } from 'react-redux';
import store from '../store';

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Header />
        <Dashboard />
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('my-maple'));
