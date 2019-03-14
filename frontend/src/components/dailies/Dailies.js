import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import { getDailies } from './dailies.duck';

export class Dailies extends Component {
  componentDidMount() {
    this.props.getDailies();
  }

  render() {
    return (
      <div>
        <h1>Dailies List</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Title</th>
              <th>Description</th>
              <th>Completed At</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {
              this.props.dailies.map(daily => (
                <tr key={ daily.id }>
                  <td>{ daily.title }</td>
                  <td>{ daily.desc }</td>
                  <td>{ daily.completed_at }</td>
                  <td>
                    { daily.completed ? 'Completed' : null }
                  </td>
                </tr>
              ))
            }
          </tbody>
        </table>
      </div>
    );
  }
}

const mapStateToProps = ({ dailies }) => ({
  dailies: dailies.data
});

export default connect(mapStateToProps, { getDailies })(Dailies);
