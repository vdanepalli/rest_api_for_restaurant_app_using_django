# Restaurant App REST API

This repository contains a practice project for building a REST API for a restaurant application using Django. The project demonstrates the implementation of CRUD operations, user authentication, and other essential functionalities for managing a restaurant application backend.

## Features

- **CRUD Operations**:
  - Manage menu items
  - Manage orders
  - Manage customers
- **User Authentication**:
  - Registration
  - Login
  - Token-based authentication
- **Django Framework**:
  - Leveraging Django's robust ORM
  - Modular app structure
- **RESTful API**:
  - Built using Django REST Framework (DRF)
  - API endpoints for various operations

## Requirements

To run this project locally, ensure you have the following installed:

- Python (>= 3.8)
- Django (>= 4.0)
- Django REST Framework (DRF)
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vdanepalli/rest_api_for_restaurant_app_using_django.git
   cd rest_api_for_restaurant_app_using_django
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate     # For Windows
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the API at `http://127.0.0.1:8000/`
- Use tools like Postman or cURL to interact with the API endpoints.


