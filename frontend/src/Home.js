import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import PropTypes from 'prop-types';

const styles = theme => ({})

class Home extends Component {

  static propTypes = {
    classes: PropTypes.object.isRequired,
  };


  render() {

    return (
      <React.Fragment>
        <CssBaseline />      
          <div>
              <h1>Home</h1>
          </div>
      </React.Fragment>
    );
  }
}


export default withStyles(styles)(Home);