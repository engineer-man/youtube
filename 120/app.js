const path = require('path');
const { app, BrowserWindow } = require('electron');

require('electron-reload')(__dirname);

app.once('ready', () => {
    const window = new BrowserWindow({
        width: 400,
        height: 300,
        webPreferences: {
            nodeIntegration: false,
            worldSafeExecuteJavaScript: true,
            contextIsolation: true,
            preload: path.join(__dirname, 'preload.js')
        }
    });

    window.loadFile('index.html');
    //window.webContents.openDevTools();
});
