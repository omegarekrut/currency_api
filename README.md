Currency Conversion API

This project provides an API to convert currencies using the apilayer service.
Project Structure

    currency_converter: This is the main Django app that handles currency conversion.
    Dockerfile: Contains instructions to build the Docker image for the project.
    docker-compose.yml: Configuration to manage the multi-container Docker application.

Setup & Running
Prerequisites

    Docker
    Docker Compose

Instructions

    Clone the Repository:

    bash

git clone <repository_url>
cd <repository_directory>

Build the Docker Image:

bash

docker-compose build

Run the Docker Containers:

bash

docker-compose up

Access the API:
Once the containers are up and running, you can access the API at http://0.0.0.0:8000/.

Run Tests:
To run tests, you can use the following command:

bash

docker-compose exec web python3 manage.py test currency_converter

Shutdown and Cleanup:
To stop and remove all containers, use:

bash

    docker-compose down

API Usage

To convert currencies, make a GET request to the endpoint /some_path/ with the following parameters:

    from: Source currency (e.g., 'USD')
    to: Target currency (e.g., 'RUB')
    value: Amount to convert (e.g., '1')

Example:

vbnet

http://0.0.0.0:8000/some_path/?from=USD&to=RUB&value=1

License

This project is licensed under the MIT License.