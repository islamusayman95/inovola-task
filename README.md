# Inovola Task
A version of Restful API for coffee shop.

## Getting Started

### Installing Dependencies

#### Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Django](https://www.djangoproject.com/)  The web framework for perfectionists with deadlines.

- [Django REST framework ](https://www.django-rest-framework.org/) a powerful and flexible toolkit for building Web APIs.

- [MongoDB](https://www.mongodb.com/) a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public License.

## Running the server
From the project folder after installing all the requirements:


For the first time you need to run:
```bash
python manage.py makemigrations
```
then 
```bash
python manage.py migrate
```
Each time you open a new terminal session, run:
```bash
python manage.py runserver
```

## Available endpoints
### [api/v1/populate_data/](api/v1/populate_data)
An optional endpoint just to create initial data for both coffee machines and coffee pods.

### [api/v1/coffee_machines/](api/v1/coffee_machines/)
Retrieves coffee machines in the database.
returns: Json file contains the query coffee machines in the database and it can be filtered using andy parameter from the given example. 
```bash
[   
    {
        "pk": 1,
        "product_type": "CM0",
        "water_line_compatible": false,
        "model": 1,
        "sku": "CM001"
    },
    {
        "pk": 2,
        "product_type": "CM0",
        "water_line_compatible": false,
        "model": 2,
        "sku": "CM002"
    },
    ...
]
```

### [api/v1/coffee_pods/](api/v1/coffee_pods/)
Retrieves all the available coffee pods in the database.
returns: Json file contains the query coffee pods in the database and it can be filtered using andy parameter from the given example. 
```bash
[
  {
        "pk": 1,
        "product_type": "CP0",
        "coffee_flavor": 0,
        "pack_size": 1,
        "sku": "CP001"
    },
    {
        "pk": 2,
        "product_type": "CP0",
        "coffee_flavor": 0,
        "pack_size": 3,
        "sku": "CP003"
    },
    ...
]
```
## Filtering example:
### [api/v1/coffee_pods?sku=CP001](api/v1/coffee_pods?sku=CP001)

output:
```bash
[
    {
        "pk": 1,
        "product_type": "CP0",
        "coffee_flavor": 0,
        "pack_size": 1,
        "sku": "CP001"
    }
]
```
### Note 
To retrieve data with name of filds instead of values you need to remove all comments in [serializers.py](coffee_shop_api_v1/serializers.py).
