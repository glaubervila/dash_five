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
import SmallText from 'components/SmallText'

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
      net_sale: null,
      amount: null,
      discount: null,
      canceled: null, 
      average: null, 
      highest: null, 
      lower: null,
      count: null,
      count_canceled: null,
      datetime: null,
      pct_change: null,
      yesterday_net_sale: null,

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

        this.setState({
          net_sale: data.net_sale,
          amount: data.amount,
          discounts: data.discounts, 
          canceled: data.canceled, 
          average: data.average, 
          highest: data.highest,
          lower: data.lower,
          count: data.count, 
          count_canceled: data.count_canceled,
          datetime: data.datetime,
          pct_change: data.pct_change,
          yesterday_net_sale: data.yesterday_net_sale,
          loading: false,
        });
      });
  };

  render() {
    const { classes } = this.props;

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
                  {this.state.net_sale}
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
            <SmallText title="Vendas Canceladas" currency={this.state.canceled}></SmallText>
          </Grid>
          <Grid item xs={12} sm={6} lg={4}>
            <SmallText title="Descontos" currency={this.state.discounts}></SmallText>
          </Grid>
          <Grid item xs={12} sm={6} lg={4}>
            <SmallText title="Ticket Médio" currency={this.state.average}></SmallText>
          </Grid>
          <Grid item xs={12} sm={6} lg={4}>
            <SmallText title="Maior Ticket" currency={this.state.highest}></SmallText>
          </Grid>
        </Grid>
      </div>
    );
  }
}


export default withStyles(styles)(Sales);