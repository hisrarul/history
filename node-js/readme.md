## Core Modules
+ http => launch a server, send requests
+ https => launch a ssl server


## NPM
+ Create a package.json file using `npm init`
+ Under the script section of package.json file, add following
```javascript
"scripts": {
    "start": "node app.js",
    "start-server": "node app.js"
}
```
+ `npm start` to run start script.

+ `npm run start-server` to run custom script.

#### Instal 3rd Party dependency using npm
+ `npm install nodemon --save` for production dependency
+ `npm install nodemon --save-dev` for dev dependency
+ `npm install nodemon -g` for global so that use it anywhere.
+ One more example, `npm install --save express-session` 
+ And we can import it using
```
const session = require('express-session');
```


#### Using nodemon for autorestart
+ Install nodemon using `npm install nodemon -g`.
+ In package.json file, we have to update the script.
```javascript
"scripts": {
    "start": "nodemon 7-assignment.js"
}
```

## Template Engine
+ Install template engine such ejs, pug, express-handlebars
```
npm install --save ejs pug express-handlebars
```