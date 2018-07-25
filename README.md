$ docker build -f Dockerfile -t sladowsk/microphone_grpc .

$ docker run -t -d -i --device=/dev/ttyS2 --name=m1 sladowsk/microphone_grpc bash



$ docker exec -it microphone_listener bash