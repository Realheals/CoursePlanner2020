const electron = require('electron');
const url = require('url');
const path = require('path');

const {app, BrowserWindow, Menu} = electron;

let mainWindow;

app.on('ready', function(){
	mainWindow = new BrowserWindow({
		webPreferences: {

            nodeIntegration: true

        }
	});

	// Loads html into window
	mainWindow.loadURL(url.format({
		pathname: path.join(__dirname, 'index.html'),
		protocol: 'file:',
		slashes: true


	}));


	// Creates menu from the template
	//const mainMenu = Menu.buildFromTemplate(mainMenuTemp);
	//Menu.setApplicationMenu(mainMenu);
});

// Add a new course
function newFunction(){
	console.log("Test");

}

// New menu
const mainMenuTemp = [
	{
		label:'Test'
	}
];