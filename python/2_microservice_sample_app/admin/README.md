## Microservice

#### Create Django project
```bash
pip3 install django

django-admin startproject admin

cd admin

python3 manage.py runserver
```

#### To rebuild this image you must use 

```bash
docker-compose build or docker-compose up --build
```

#### Create products 
```bash
1. Login to backend container of product
python manage.py startapp products

-or-

python manage.py makemigrations

python manage.py migrate
```

#### Create Table products_product
```sql
CREATE TABLE `products_product` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `title` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `likes` varchar(255) NOT NULL
);

CREATE TABLE `products_user` (
  `id` int NOT NULL
);
```
