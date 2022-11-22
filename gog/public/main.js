const {app, BrowserWindow} = require('electron');
const path = require('path');
// const url = require('url');

/*
Reference :
https://medium.com/withj-kr/react와-electronjs로-데스크톱-앱-만들어보기-1-프로젝트-세팅하기-6f83562de839
*/
// function client() {
//     const win = new BrowserWindow({
//         width:1920,
//         height:1080,
//         webPreferences: {
//             nodeIntegration: true,
//         }
//     });

//     const startUrl = process.env.ELECTRON_START_URL || url.format({
//         pathname: path.join(__dirname, '/../build/index.html'),
//         protocol: 'file:',
//         slashes: true
//     });

//     win.loadURL(startUrl);
// }


// app.on('ready', client);

function createWindow() {
    const mainWindow = new BrowserWindow({ width: 1920, height: 1080 });
    // mainWindow.loadURL('http://localhost:3001');
    mainWindow.loadFile(path.join(__dirname, '/../../build/index.html'));
}

app.whenReady().then(() => {
    createWindow();

    app.on('activate', () => {
        if(BrowserWindow.getAllWindows().length === 0){
            createWindow();
        }
    });

    app.on('window-all-closed', () => {
        if(process.platform !== 'darwin'){ // macOS
            app.quit();
        }
    });
});
