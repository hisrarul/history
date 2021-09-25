## Nodejs with Sequelize

#### Create docker volume
```bash
docker volume create --name=postgres-vol
```

#### Start postgres container
```bash
docker-compose up
```

#### Initilize the project
```bash
npm init
npm install express body-parser sequelize pg pg-hstore express-handlebars

# dev dependencies to restart the project automatically
npm install -D nodemon
```

#### Start the project in dev env
```bash
npm run dev
```

#### Referred
https://www.youtube.com/watch?v=6jbrWF3BWM0
https://github.com/bradtraversy/codegig