const { contextBridge } = require('electron');

contextBridge.exposeInMainWorld('axios', require('axios'));
