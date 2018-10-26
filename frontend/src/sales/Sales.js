import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import { 
  Sparklines, 
  SparklinesBars, 
  // SparklinesReferenceLine 
} from 'react-sparklines';

import SalesApi from 'sales/Api'


const styles = theme => ({
  card: {
    padding: theme.spacing.unit,
    minheight: '200px',
    height: '200px',
    backgroundColor: '#039BE5',
    paddingBottom: 'unset',
  },
  amounttile: {
    color: theme.palette.primary.contrastText,
  },
  amount: {
    color: theme.palette.primary.contrastText,
    fontWeight: theme.typography.fontWeightMedium
  },
  paperchart: {
    padding: theme.spacing.unit *2,
    paddingBottom: 'unset',
    color: theme.palette.text.secondary,
    backgroundColor: '#039BE5',
    minheight: '200px',
    height: '200px',    
  },

  paper: {
    padding: theme.spacing.unit * 2,
  },

  chart: {

  }

});

class Sales extends Component {

  state = this.initialState;
  api = new SalesApi();

  static propTypes = {
    classes: PropTypes.object.isRequired,
  };

  get initialState() {
    return {
      loading: false,
      today_summary: {}
    };
  }

  componentDidMount() {
    this.fetchData();
  }


  fetchData = () => {
    this.setState({ loading: true });

    this.api
      .today_summary()
      .then(res => {
        const data = res.data;

        console.log(data)
        this.setState({
          today_summary: data,
          loading: false,
        });
      });
  };

  render() {
    const { classes } = this.props;

    let net_sale = '';
    if (this.state.today_summary.net_sale) {
      net_sale = 'R$ ' + this.state.today_summary.net_sale;
    }

    return (
      <div className={classes.root}>
        <Grid container spacing={24}>
          <Grid item xs={12} sm={6} lg={4}>
            <Card className={classes.card}>
              <CardContent>
                <Typography variant="subtitle1" className={classes.amounttile} gutterBottom>
                  Venda Liquida
                </Typography>
                {/* TODO: Usar alguma biblioteca para converter float para moeda local */}
                <Typography variant="h5" className={classes.amount} gutterBottom>
                  {net_sale}
                </Typography>
                <div> 
                  <Sparklines data={[99, 80, 75, 94, 10, 5, 15, 20, 50, 55, 45, 70, 80]}>
                    <SparklinesBars style={{ fill: '#80D8FF', fillOpacity: ".5" }} />
                    {/* <SparklinesReferenceLine /> */}
                  </Sparklines>                
                </div>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} lg={4}>
            <Paper className={classes.paper}>            
            </Paper>
          </Grid>          
          {/* <Grid item xs={12} sm={6} lg={4}>
            <Paper className={classes.paperchart}>            
                <Typography variant="subtitle1" className={classes.amounttile} gutterBottom>
                  Venda Liquida
                </Typography>
                <Typography variant="h5" className={classes.amount} gutterBottom>
                  R$ 150.000
                </Typography>
                <div className={classes.chart}>
                <Sparklines data={[99, 80, 75, 94, 10, 5, 15, 20, 50, 55, 45, 70, 80]}>
                  <SparklinesBars style={{ fill: '#80D8FF', fillOpacity: ".5" }} />
                  <SparklinesReferenceLine /> 
                </Sparklines>
                </div>
            </Paper>
          </Grid> */}
          <Grid item xs={12} sm={6} lg={4}>
            <Paper className={classes.paper}>            
            </Paper>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Paper className={classes.paper}>xs=12 sm=6</Paper>
          </Grid>
          <Grid item xs={6} sm={3}>
            <Paper className={classes.paper}>xs=6 sm=3</Paper>
          </Grid>
          <Grid item xs={6} sm={3}>
            <Paper className={classes.paper}>xs=6 sm=3</Paper>
          </Grid>
          <Grid item xs={6} sm={3}>
            <Paper className={classes.paper}>xs=6 sm=3</Paper>
          </Grid>
          <Grid item xs={6} sm={3}>
            <Paper className={classes.paper}>xs=6 sm=3</Paper>
          </Grid>
        </Grid>
      </div>
    );
  }
}


export default withStyles(styles)(Sales);