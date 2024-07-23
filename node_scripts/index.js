const SerialPort = require('serialport').SerialPort;
const CryptoJS = require('crypto-js');
const { platform } = require('os');
const { exec } = require('child_process');

const WINDOWS_PLATFORM = 'win32';
const MAC_PLATFORM = 'darwin';

const osPlatform = platform();

SerialPort.list().then(ports => {
    ports.forEach(({ path }) => {
        const port = new SerialPort({ path, baudRate: 9600 });

        port.on('data', (data) => {
            const hashedId = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(data.toString().trim()));
            const url = `http://localhost:5000/sync/${hashedId}/`;

            let command;

            if (osPlatform === WINDOWS_PLATFORM) {
                command = `start microsoft-edge:${url}`;
            } else if (osPlatform === MAC_PLATFORM) {
                command = `open -a "Google Chrome" ${url}`;
            } else {
                command = `google-chrome --no-sandbox ${url}`;
            }

            console.log(`Executing command: ${command}`);
            exec(command);
        });
    });
}).catch(error => {
    console.error(error);
});
