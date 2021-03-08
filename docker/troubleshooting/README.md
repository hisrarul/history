## Docker Troubleshooting

#### COPY failed: Forbidden path outside the build context
```
Copy failed when tried to copy files from a directory other than a directory where Dockerfile is present

Solution: Define context
docker build -t <your_tag> -f <path_where_your_dockerfile_is> .

Note:
Your current path should be the folder where the source folder or file exist. For e.g.
vi Dockerfile
COPY <source_folder> .
```
