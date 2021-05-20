
## Part I Solution

  1. Run docker container in backgroud using image `infracloudio/csvserver:latest`

    docker run --name csvserver -d infracloudio/csvserver:latest


  2. csvserver docker container failed to run because **inputdata** file is not available inside the container

  3. Placed a bash script `gencsv.sh` in solution dir to generate a file named `inputFile` whose content looks like:

      0, 180
      1, 367
      2, 867
      3, 189
      4, 168
      5, 604
      6, 483
      7, 422
      8, 255
      9, 380

  4. Ran the container using below cli where I have mount `inputFile` on `/csvserver/inputdata

    docker run --name csvserver -d -v $PWD/inputFile:/csvserver/inputdata infracloudio/csvserver:latest

  5. Accessed the shell of the container and check on which port container is listening
      
    docker exec -it csvserver /bin/bash
    netstat -tlnp
  - It is listening on port 9300.
    
  - Deleted the container
     
    ```
      docker container rm -f csvserver
    ```
  
  6. Run the container again
    
  - Bind container port 9300 to localhost 9393 and pass given env varaible
    
      ```
      docker run --name csvserver -e CSVSERVER_BORDER=Orange -p 9393:9300 -d -v $PWD/inputFile:/csvserver/inputdata infracloudio/csvserver:latest
      ```

  - check the output in browser or using curl
      ```
      curl http://localhost:9393
      ```

## Part II Solution
  0. Delete the container

    docker container rm -f csvserver

  1. Wrote docker-compose.yaml in solution dir. I am running it on docker engine 19.03.13
  
  2. Execute `docker-compose up` inside the solution dir. This will run the container in the foreground.

## Part III Solution
  0. Stopped last container ran with `docker-compose down`
  1. Added prometheus container using image `prom/prometheus:v2.22.0` in docker-compose.yaml
  3. Created `prometheus.yaml` file with scraped config
  4. Checked prometheus on browser using `http://localhost:9090`. Type csvserver_records in the query box of Prometheus. Click on Execute and then switch to the Graph tab.