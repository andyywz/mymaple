import React, { Component } from 'react';
import Dailies from './Dailies';
import Form from './Form';

export class Dashboard extends Component {
  render() {
    return (
      <div>
        <Form />
        <Dailies />
      </div>
    )
  }
};

export default Dashboard;
