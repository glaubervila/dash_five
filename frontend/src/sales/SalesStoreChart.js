import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import numeral from 'numeral';
import Plot from 'react-plotly.js';
import sizeMe from 'react-sizeme';
const styles = theme => ({
});

class SalesStoreChart extends Component {
  static propTypes = {
    classes: PropTypes.object.isRequired,
    data: PropTypes.array.isRequired,
  };

  render() {
    const { classes, data } = this.props;

    console.log(data)
    // let content = ''
    // if (currency) {
    //   content =  Math.trunc(currency).toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
    // }

    const store_summary = {
      type: 'bar', 
      orientation: 'h',
      x: [], 
      y: [],
    }
    data.map((store, i) => {
      console.log(store)
      store_summary['x'].push(store.amount);
      store_summary['y'].push(store.store_name);
    })

    return (
            <Plot
              data={[
                store_summary
              ]}
              layout={{
                autosize: false,
                width: this.props.size.width,
                height: this.props.size.height, 
                title: '',
                // responsive: true,
                // autosize: true,
                showlegend: false,
              }}
              config={{
                scrollZoom: true,
                displayModeBar: false
              }}
            />
    );
  }     
}

export default withStyles(styles)(sizeMe({ monitorHeight: true})(SalesStoreChart));