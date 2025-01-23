# Install Dependencies

Run the following commands in a terminal to create a docker image with a volume mounting the current directory.
Then install dependencies which would be kept on your local drive.
Later, this whole directory would be mounted in other services to be used.

```
docker run -it --rm -v $(pwd):/app --name ot_service node:22 npm install
docker container remove ot_service
```
