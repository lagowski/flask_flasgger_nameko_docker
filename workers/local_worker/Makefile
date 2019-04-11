TAG ?= dev

# docker

build-image:
	docker build -t docker.pro4.es/nameko-example-gateway1:$(TAG) -f docker.run .;

push-image:
	docker push docker.pro4.es/nameko-example-gateway1:$(TAG)

run-image:
	docker run 	docker.pro4.es/nameko-example-gateway1:$(TAG)