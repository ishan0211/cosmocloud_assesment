# Service

This is an Service built in Python 3.10 using the FastAPI framework. the service contains the api's provided in the problem statement and also some extra apis and fuctionalities.

## Components

- **FastAPI**: Utilizes the FastAPI framework for building high-performance APIs with Python 3.10.
- **MongoDB**: Stores events in a MongoDB database for efficient and scalable data storage.
- **Beanie ODM**: Implements Beanie, an async ODM (Object Document Mapper), on top of the Motor driver for MongoDB.
- **pipenv**: Handles Python dependencies and virtual environment management.

## Prerequisites

Before running the Service, make sure you have the following installed:

- Python 3.10 or later
- MongoDB (with connection details available)
- 'uvicorn[standard]'
- beanie

## Getting Started

* Clone the repository:

```bash
git clone https://github.com/ishan0211/cosmocloud_assesment.git
cd app
```

* Install `pipenv` if you don't have it:

```bash
pip install pipenv
```

* Create a virtual environment and install the required dependencies:

```bash
pipenv install --python 3.10
```

* Activate the virtual environment:

```bash
pipenv shell
```

* Configure the environment variables:

```ini
MONGODB_URL=mongodb://root:root@localhost:27017
```

* Run the FastAPI server:

```bash
uvicorn src.server:app --port 8001 --reload
```

The server will start running at `http://localhost:8001`. You can access the interactive API documentation at `http://localhost:8001/docs`.

## Get Started

just create the necessary product data by API endpoint:
- `POST /service/products/bulk'`

to list all the products in system use API endpoint:
here i have also added pagination just give the page limit 100 to get the whole list i have set the maximum limit of the query parameter 100 but it can adjusted accordingly.
- `GET /service/products/`
i have also added the filter of minimum and max prize.

to update the product avaibility use API endpoint:
- `PUT /service/product/`

to create order use API endpoint:
- `POST /service/orders/`
use the object_id you get while creating the product as these the product_id in input
it will also decrease the bought quantity from the available products 
it will raise error of the bought quantity is greater than available

to list orders use API endpoint:
- `GET /service/orders`

to cancel a order use API endpoint:
- `DELETE /service/orders`
it is additional
just the object_id of the order you want to cancel

to get aa order by id user API endpoint:
- `GET /service/orders/{order_id}`
order_id is the object_id of the order you want to get

## Structure

actions - it has all the main code logic 

api/endpoints - it contains all the endpoints

api/schema - it contains all pre-defined model so that tha input format of api's can be genralized

constants - it has contants as enums

models - it has the schema for the model which i have used 


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

