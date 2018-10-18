import React, { Component } from 'react';
import { Router, Route, Switch, Redirect } from 'react-router-dom';

// Material-UI
import CssBaseline from '@material-ui/core/CssBaseline';

// Theme
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';

// import { deepOrange500 } from 'material-ui/styles/colors'
// import getMuiTheme from 'material-ui/styles/getMuiTheme'
// import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

// Font
import 'typeface-roboto';

// Pages 
import { isAuthenticated } from './auth';
import history from './history';
import Login from './Login';
import Home from './Home';


// Theme
const theme = createMuiTheme({
  typography: {
    useNextVariants: true,
  },
});

const PrivateRoute = ({ component: Component, ...rest }) => (
  <Route
    {...rest}
    render={props =>
      isAuthenticated() ? (
        <Component {...props} />
      ) : (
        <Redirect
          to={{
            pathname: '/login',
            state: { from: props.location },
          }}
        />
      )
    }
  />
);


class App extends Component {
  render() {
    return (
      <React.Fragment>
        <CssBaseline />
        <MuiThemeProvider theme={theme}>
          <Router history={history}>
            <Switch>
              <Route path="/login" name="Login" component={Login} />
              <PrivateRoute path="/" name="Home" component={Home} />
            </Switch>
          </Router>
        </MuiThemeProvider>
      </React.Fragment>
    );
  }
}

export default App;
