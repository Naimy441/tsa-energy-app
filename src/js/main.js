const { app, BrowserWindow, ipcMain } = require('electron');
const { PythonShell } = require('python-shell')
path = require('path')
fs = require('fs')
console = require('console')

const createWindow = () => {
    const win = new BrowserWindow({
        fullscreen: true,
        frame: false,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
        },
        icon: path.join(__dirname, '../', '../', 'images/LoveToLearn.ico')
    })

    win.loadFile('src/html/index.html')
} 

// Main Functions

//Credit: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
function random(event, min, max) {
    min = Math.ceil(min)
    max = Math.floor(max)
    event.returnValue = Math.floor(Math.random() * (max - min) + min)
}

function loadHTML(event, name) {
    const webContents = event.sender
    const win = BrowserWindow.fromWebContents(webContents)
    win.loadFile('src/html/' + name + '.html')
}

function loadUserData(event) {
    userDataFile = path.join(__dirname, '../', '../', 'user_data.json')
    rawData = fs.readFileSync(userDataFile)
    userData = JSON.parse(rawData)
    event.returnValue = userData
}

function print(event, message) {
    console.log(message)
}

function saveUserData(event, jsonData) {
    userDataFile = path.join(__dirname, '../', '../', 'user_data.json')
    fs.writeFileSync(userDataFile, jsonData)
}

// function getCurrentDate(event) {
//     event.returnValue = datetime.create().format('m/d/Y H:M:S')
// }

function getPythonData(event, filename, request, jsonData) {
    let pyshell = new PythonShell(path.join(__dirname, '../', 'algorithms/') + filename + '.py', {
        mode: 'json',
        args: [jsonData]
    })
    pyshell.on('message', function(message) {
        userDataFile = path.join(__dirname, '../', '../', 'user_data.json')
        rawData = fs.readFileSync(userDataFile)
        userData = JSON.parse(rawData)
        userData['ipcData'] = message[request]
        fs.writeFileSync(userDataFile, JSON.stringify(userData))
    })
}

app.whenReady().then(() => {
    ipcMain.on('load-html', loadHTML)
    ipcMain.on('load-user-data', loadUserData)
    ipcMain.on('save-user-data', saveUserData)
    // ipcMain.on('get-current-date', getCurrentDate)
    ipcMain.on('get-python-data', getPythonData)
    ipcMain.on('random', random)
    ipcMain.on('print', print)

    createWindow()
})
