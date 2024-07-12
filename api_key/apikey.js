import fetch from 'node-fetch';
import fs from 'fs'
import path from 'path'
import os from 'os'

const api_key = '79fWD7OC8t6l1usTOZcvX3mD1H94jNAs8AUnhTjs'

const payload = {
    symbol: 'BINANCE:ETHUSDT',
    interval: '4h',
    studies: [{name: 'Volume', forceOverlay: true}, { name: 'MACD' }]
}

const requestOptions = {
    method: 'POST',
    headers : {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
}

const endpoint = 'https://api.chart-img.com/v2/tradingview/advanced-chart';

const fetchImage = async () => {
    try {
      const response = await fetch(endpoint, requestOptions);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const buffer = await response.buffer();
      const desktopPath = path.join(os.homedir(), 'Desktop', 'chart-img.png');
      fs.writeFileSync(desktopPath, buffer);
      console.log(`Image saved to ${desktopPath}`);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  
  // Execute the function
  fetchImage();


