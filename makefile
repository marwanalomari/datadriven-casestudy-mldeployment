train:
	docker build -t docker-ml-model -f train.Dockerfile .
	docker run -d --name con-ml-model -it docker-ml-model

api:
	docker cp con-ml-model:/app/model_lr.pkl /home/
	docker cp con-ml-model:/app/vectorizer.pickle /home/
	docker build -t docker-ml-api -f api.Dockerfile .
	docker run -d --name ml-model -it -p 4002:4002 docker-ml-api
	docker cp /home/model_lr.pkl ml-model:/app/
	docker cp /home/vectorizer.pickle ml-model:/app/
