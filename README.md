Example of very simple project with Flask, Nameko, Flasgger and RabbitMQ 

We have two parts of the project
 - gateway - as Flask with flasgger API 
 - workers - are services that are connected by nameco and RabbitMQ

To start

```
docker-compose build
docker-compose up
```

access to Flasgger thru http://127.0.0.1:8080/apidocs/
