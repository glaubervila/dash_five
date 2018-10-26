import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import PropTypes from 'prop-types';
import { 
  Switch, 
  Route, 
  // Redirect 
} from "react-router-dom";

import  Header from './Header';
import Sales from './sales/Sales';

const styles = theme => ({
  root: {
    display: 'flex',
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing.unit * 3,
    height: '100vh',
    overflow: 'auto',
  },  
  appBarSpacer: theme.mixins.toolbar,
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

          <main className={classes.content}>
            <div className={classes.appBarSpacer} />
            <Switch>
                <Route path="/" exact={true} component={Sales} />
                {/* <Route path="/sobre" component={Sobre} /> */}
            </Switch>
          </main>
        </div>
      </React.Fragment>
    );
  }
}


export default withStyles(styles)(Home);