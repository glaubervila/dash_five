import axios from 'axios';

class SalesApi {
  constructor() {
    this.api = process.env.REACT_APP_API;
  }

  today_summary = () =>
    axios.get(`${this.api}/sale/ticket/today_summary/`);  

}

export default SalesApi;