train:
	dockebuild -t docker-ml-model -f train.Dockerfile .
	docker run docker-ml-model
api:
	docker build -t docker-ml-api -f api.Dockerfile .
	docker run -it -p 4002:4002 docker-ml-api