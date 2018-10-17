

## Instalação 

## Instalation
### Clone Repository
```
git clone https://github.com/glaubervila/dash_five.git
```

```
cd dash_five
```

### Build and Run Containers 

Check the user id and change the docker-compose.yml if your id is different from 1000

```
id
```
the output is something like this:
```
uid=1000(glauber) gid=1000(glauber) grupos=1000(glauber),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lpadmin),126(sambashare),999(docker)
```

If your user does not have 1000 uid change all user: 1000: 1000 entries to their uid and gid values

```
  ... 
  #Backend Django
  backend:
    user: <uid>:<gid>
    build: ./backend
  ...

```

#### Build Containers 
```
docker-compose build
```

#### Runing Containers
```
docker-compose up
```

Note: At this point an error can occur with the backend when connecting to the database, this is because it takes a while to start at the first run of mysql. to solve, just stop the containers and try again.

### Create a superuser in Django
Make sure the containers are on, and see the name of the backend container.

in this case the name is: dash_five_backend_1
```
docker-compose ps
```


run createsuperuser to create a admin user in Django.
with the docker running open a new terminal and run this command.
```
 docker exec -it dash_five_backend_1 python manage.py createsuperuser
```

open a browser and try to access 
```
http://localhost:8081/admin/
```
this is the administration interface

### Load Initial Data
```
docker exec -it dash_five_backend_1 python manage.py loaddata common/fixtures/initial_data.json
```

## Frontend
To develop or access the frontend follow the steps below.

```
cd frontend/
```
Run the yarn command to install the dependencies.
```
yarn
```
Start the development server
```
yarn run start
```

## Instalation Complete
At this moment the installation is complete, and it is possible to access the following services:

App: http://localhost:8080

Django Admin: http://localhost:8081/admin/

Django REST API: http://localhost:8081/api/    (need to be logged in on admin)

PhpMyAdmin: http://localhost:8082/ (user: root password: adminadmin)

