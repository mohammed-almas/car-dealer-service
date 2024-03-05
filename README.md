# Car Dealer RESTful API Service

## Overview
This project is a simple POC written in python with the help of FastAPI framework. It has implementations for CRUD operations for two models Dealer and Car which uses sqlite as the database and sqlalchemy as the ORM.

## Getting Started

### Prerequisites
- Python 3.9+
- Virtualenv

### Installation Steps
1. Create a virtual environment.
    ```sh
    virtualenv venv
    ```
    
2. Activate virtual env.

    For MacOS:
    ```sh
    source venv/bin/activate
    ```

    For Windows:
    ```sh
    venv/Scripts/activate
    ```

3. Install python modules from requirements.txt file using pip.
    ```sh
    pip install -r requirements.txt
    ```

### Running the project
To run the project, start the uvicorn server using the following command.
```sh
uvicorn main:app --reload
```

## API Docs
To see the Swagger documentation for the project, go to the following address in browser after running the project local server.
```sh
http://localhost:8000/docs
```

To see Redoc documentation for the project, go to following address:
```sh
http://localhost:8000/redoc
```

### API Routes for Dealer
        POST - http://localhost:8000/dealer/
        GET - http://localhost:8000/dealer/
        GET - http://localhost:8000/dealer/{id}
        PUT - http://localhost:8000/dealer/{id}
        DELETE - http://localhost:8000/dealer/{id}

### API Routes for Car
        POST - http://localhost:8000/car/
        GET - http://localhost:8000/car/
        GET - http://localhost:8000/car/{id}
        PUT - http://localhost:8000/car/{id}
        DELETE - http://localhost:8000/car/{id}

#### Example Request
API Endpoint for fetching list of all dealers:
```
GET - /dealer
```

Command for calling the endpoint with request url:
```sh
curl http://localhost:8000/dealer/ -H "Accept: application/json"
```

Response:
```sh
{
    "status": "success",
    "dealers": [
        {
            "address": "Delhi",
            "contact_no": "9876543210",
            "name": "Raja Hyundai",
            "id": 1
        },
        {
            "address": "Kota",
            "contact_no": "9876098760",
            "name": "Volkswagen Kota",
            "id": 2
        },
        {
            "address": "Mumbai",
            "contact_no": "9012390123",
            "name": "LMJ Honda",
            "id": 3
        }
    ]
}
```

## Notes
- I have chosen FastAPI as the framework for this project because on a simple project level it provides the best features that any other framework which can be extended further based on complexity of requirements.
- FastAPI provides asynchronous execution for APIs and type annotations along with good support for data validation.
- It also provides documentation such as swagger without any external implementation.
- I have used Pydantic because it provides default schema validation and used SQLAlchemy as the ORM.
- A pre-populated sample database file with name sampleDatabase.db has been added to the project directory for taking reference on database values.