DBNAME='crudd'
DBPASSWORD='example1234'

DOCKERIP=$(ifconfig | grep -A 2 docker | grep inet | awk -F' ' '{print $2}')

MYSQL_PWD=${DBPASSWORD} mysql -h ${DOCKERIP} -u root --execute "create database ${DBNAME}"

MYSQL_PWD=${DBPASSWORD}  mysql -h ${DOCKERIP} -u root \
    --database=${DBNAME} \
    --execute 'CREATE TABLE `data` ( \
        `id` int NOT NULL AUTO_INCREMENT, \
        `name` varchar(100) DEFAULT NULL, \
        `email` varchar(100) DEFAULT NULL, \
        `phone` varchar(100) DEFAULT NULL, \
        PRIMARY KEY (`id`) \
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;'

