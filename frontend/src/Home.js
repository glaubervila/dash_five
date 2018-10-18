import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import PropTypes from 'prop-types';

import  Header from './Header';
const styles = theme => ({
  root: {
    display: 'flex',
  },
});

class Home extends Component {

  static propTypes = {
    classes: PropTypes.object.isRequired,
  };


  render() {
    const { classes } = this.props;
    return (
      <React.Fragment>
        <CssBaseline />      
        <div className={classes.root}>
          <Header />
        </div>
      </React.Fragment>
    );
  }
}


export default withStyles(styles)(Home);