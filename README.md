# Python FastApi application using Celery, RabbitMQ and MySQL

### To run the application through docker you can use the command below in ./app directory
`docker-compose up -d`

### If you want to run the project locally in a traditional way, you have to setup MySQL, RabbitMQ as broker before starting to run the application. After setting up these, do not forget setting up environment variables and also renaming the .env.example file to .env
`uvicorn main:app --reload`

### To access the Swagger UI, you can go the route below
`localhost:8000/docs`
