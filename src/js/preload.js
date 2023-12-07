const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    print: (message) => ipcRenderer.send('print', message),
    loadHTML: (filename) => ipcRenderer.send('load-html', filename),
    loadUserData: () => ipcRenderer.sendSync('load-user-data'),
    saveUserData: (jsonData) => ipcRenderer.send('save-user-data', jsonData),
    getCurrentDate: () => ipcRenderer.sendSync('get-current-date'),
    getPythonData: (filename, request, jsonData) => ipcRenderer.send('get-python-data', filename, request, jsonData),
    random: (min, max) => ipcRenderer.sendSync('random', min, max), 
});
