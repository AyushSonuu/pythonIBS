## Docker Commands and Usage

**Pulling an Image**
```
docker pull nginx
```
- Pulls the Nginx image from the Docker Hub registry.

**Running a Container**
```
docker run --name docker-nginx -p 80:80 nginx #Expose Nginx 80 Port
```
- Creates and runs an Nginx container with the name `docker-nginx`.
- Exposes port 80 from the container to the host machine, allowing access to the Nginx server.

```
docker run --name docker-nginx -p 8080:80 -d nginx #Expose 8080
```
- Same as above, but exposes port 8080 instead of 80.
- Runs the container in the background (`-d` flag).

```
docker run -P nginx
```
- Automatically maps all exposed ports in the container to random ports on the host machine.

**Running a Container Detached**
```
docker run -d -P nginx
```
- Runs the container in the background, detached from the terminal session.

**Building an Image**
```
docker build -t friendlyname . #Create image using this directory's Dockerfile
```
- Builds an image using the Dockerfile in the current directory, tagging it with the name `friendlyname`.

**Running a Custom Image**
```
docker run -p 4000:80 friendlyname #Run "friendlyname" mapping port 4000 to 80
```
- Runs the `friendlyname` image, mapping port 4000 on the host to port 80 inside the container.

```
docker run -d -p 4000:80 friendlyname #Same thing, but in detached mode
```
- Same as above, but runs the container in detached mode.

**Entering a Container**
```
docker run --name test-ubuntu -it ubuntu:16.04 ./bin/bash
```
- Creates and runs an Ubuntu container named `test-ubuntu`.
- Attaches a terminal to the container, allowing interactive commands (`-it` flag).

**Accessing a Running Container**
```
docker exec -it [container-id] bash #Enter a running container
```
- Attaches a terminal to an already running container.

**Listing Containers**
```
docker ps #See a list of all running containers
```
- Lists all running containers.

```
docker ps -a #See a list of all containers, even the ones not running
```
- Lists all containers, including those that are stopped.

**Stopping and Removing Containers**
```
docker stop <hash> #Gracefully stop the specified container
```
- Gracefully stops the container with the given hash.

```
docker kill <hash> #Force shutdown of the specified container
```
- Forcefully stops the container with the given hash.

```
docker rm <hash> #Remove the specified container from this machine
```
- Removes the specified container from the machine.

```
docker rm $(docker ps -a -q) #Remove all containers from this machine
```
- Removes all containers from the machine.

**Managing Images**
```
docker images -a #Show all images on this machine
```
- Lists all images stored on the machine.

```
docker rmi <imagename> #Remove the specified image from this machine
```
- Removes the specified image from the machine.

```
docker rmi $(docker images -q) #Remove all images from this machine
```
- Removes all images from the machine.

**Viewing Logs**
```
docker logs <container-id> -f #Live tail a container's logs
```
- Continuously streams the logs of the specified container.

**Docker Login and Tagging**
```
docker login #Log in this CLI session using your Docker credentials
```
- Logs in to Docker Hub using your credentials.

```
docker tag <image> username/repository:tag #Tag <image> for upload to registry
```
- Tags the specified image with the given username, repository, and tag.

**Pushing and Running from a Registry**
```
docker push username/repository:tag #Upload tagged image to registry
```
- Pushes the tagged image to the specified Docker Hub registry.

```
docker run username/repository:tag #Run image from a registry
```
- Runs the specified image from the Docker Hub registry.

**System Maintenance**
```
docker system prune #Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes. (Docker 17.06.1-ce and superior)
```
- Removes all unused Docker objects.

```
docker system prune -a #Remove all unused containers, networks, images not just dangling ones (Docker 17.06.1-ce and superior)
```
- Removes all unused Docker objects, including those that are not dangling.

**Managing Volumes**
```
cd usr/share/nginx/html/ #Navigate to Nginx's default document root
```

```
docker volume create my_vol #Create a volume
```
- Creates a new Docker volume named `my_vol`.

```
docker volume ls #List all volumes
```
- Lists all volumes on the machine.

```
docker volume inspect my_vol #Inspect a volume
```
- Shows detailed information about the specified volume.

```
docker volume rm my_vol #Remove a volume
```
- Removes the specified volume from the machine.


## Additional Docker Commands for EC2

**Allowing HTTP Access**
```sudo yum update -y # Update the system
sudo yum install -y docker # Install Docker
sudo service docker start # Start Docker
sudo usermod -aG docker ec2-user # Add the current user to the docker group
```
- These commands are necessary to allow access to port 80 (HTTP) from anywhere on an EC2 instance.