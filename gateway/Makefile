TAG ?= dev

# docker

build-image:
	docker build -t docker.pro4.es/example-gateway:$(TAG) -f docker.run .;

run-gateway:
	 docker run -d -p 5000:5000 docker.pro4.es/example-gateway:$(TAG)

push-image:
	docker push docker.pro4.es/example-gateway:$(TAG)

run-image:
	docker run 	docker.pro4.es/example-gateway:$(TAG)	