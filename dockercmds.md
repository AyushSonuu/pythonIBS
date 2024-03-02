**Docker Commands Notes**

**Pulling an Image**

- `docker pull nginx`: Pulls the official Nginx image from Docker Hub.

**Running a Container**

- `docker run --name docker-nginx -p 80:80 nginx`: Runs an Nginx container with the following settings:
  - Name: `docker-nginx`
  - Port mapping: Exposes port 80 on the host machine to port 80 inside the container
- `docker run --name docker-nginx -p 8080:80 -d nginx`: Same as above, but exposes port 8080 to 80 and runs the container in detached mode (background).
- `docker run -P nginx`: Runs an Nginx container and automatically maps exposed ports to host ports.
- `docker run -d -P nginx`: Same as above, but runs the container in detached mode.

**Building an Image**

- `docker build -t friendlyname .`: Builds an image from the Dockerfile in the current directory and tags it with the name `friendlyname`.

**Running a Custom Image**

- `docker run -p 4000:80 friendlyname`: Runs the `friendlyname` image and maps port 4000 on the host to port 80 inside the container.
- `docker run -d -p 4000:80 friendlyname`: Same as above, but runs the container in detached mode.

**Accessing a Container**

- `docker exec -it [container-id] bash`: Enters an interactive shell within a running container.

**Managing Containers**

- `docker ps`: Lists all running containers.
- `docker ps -a`: Lists all containers, including those not running.
- `docker stop <hash>`: Gracefully stops a running container.
- `docker kill <hash>`: Forcefully stops a running container.
- `docker rm <hash>`: Removes a container from the machine.
- `docker rm $(docker ps -a -q)`: Removes all containers from the machine.

**Managing Images**

- `docker images -a`: Lists all images on the machine.
- `docker rmi <imagename>`: Removes a specific image from the machine.
- `docker rmi $(docker images -q)`: Removes all images from the machine.

**Monitoring Logs**

- `docker logs <container-id> -f`: Continuously prints the logs for a running container.

**Accessing Docker Hub**

- `docker login`: Logs in to Docker Hub using the user's credentials.

**Tagging and Pushing Images to Docker Hub**

- `docker tag <image> username/repository:tag`: Tags an image with a username, repository, and tag.
- `docker push username/repository:tag`: Pushes a tagged image to Docker Hub.

**System Pruning**

- `docker system prune`: Removes unused containers, networks, and images.
- `docker system prune -a`: Removes all unused resources, including dangling images.

**Volume Management**

- `cd usr/share/nginx/html/`: Changes the working directory to the default Nginx webroot.
- `docker volume create my_vol`: Creates a new Docker volume named `my_vol`.
- `docker volume ls`: Lists all Docker volumes.
- `docker volume inspect my_vol`: Inspects the details of a Docker volume.
- `docker volume rm my_vol`: Removes a Docker volume.

**EC2 Setup**

- `sudo yum update -y`: Updates the system's packages.
- `sudo yum install -y docker`: Installs Docker.
- `sudo service docker start`: Starts the Docker service.
- `sudo usermod -aG docker ec2-user`: Adds the current user to the docker group.