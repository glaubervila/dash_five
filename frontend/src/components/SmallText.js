import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import numeral from 'numeral';

const styles = theme => ({
  paper: {
    padding: theme.spacing.unit * 2,
    backgroundColor: '#039BE5',   
    textAlign: 'center',
  },
  title: {
    color: theme.palette.primary.contrastText,
  },
  text: {
    color: theme.palette.primary.contrastText,
    fontWeight: theme.typography.fontWeightMedium
  },
});

class SmallText extends Component {
  static propTypes = {
    classes: PropTypes.object.isRequired,
    title: PropTypes.string,
    currency: PropTypes.string,
  };

  render() {
    const { classes, title, currency } = this.props;

    numeral.locale('pt-br');

    let content = ''
    if (currency) {
      content =  Math.trunc(currency).toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
    }

    return (
      <Paper className={classes.paper}>            
          <Typography variant="subtitle1" className={classes.title} gutterBottom>
            {title}
          </Typography>
          <Typography variant="h5" className={classes.text} gutterBottom>
            {content}
          </Typography>
      </Paper>
    );
  }     
}

export default withStyles(styles)(SmallText);