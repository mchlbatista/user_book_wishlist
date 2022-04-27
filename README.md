# User Wishlist App
---
User Book Wishlist Management API

This service will allow the user to list, add, update or delete books for an owned wishlist.

## Local Setup
---
1. Create in the project's folder your `virtual env`
2. Activate your `virtual env`
3. Install project's dependencies `pip install -r requirements`

### Run Locally
---
The Project uses Docker to run locally and can be ran by using the command `make run`

Due the nature of "example" type of project, the DB will be seeded with users(10), books(10) and wishlists(10). Also a pre-relationship between the created wishlists and the users will be generated. Is expected after the DB seeding each user to have one wishlist. The assignment of books to any wishlist will be done using the implemented API endpoints.

To access to the API Swagger navigate to the [project root url](http://localhost)

![swagger_img](https://github.com/mchlbatista/user_book_wishlist/blob/master/Swagger.png)


### Run Test
___
From your `virtual env` execute `make tests`

## Used Tech

1. **Flask**. For simple implementation.
2. **Flask-Restx**. Allows to have Swagger out of the box. Also adds tools for API development like input validation.
3. **SQLAlchemy**. ORM. Interacts with the DB as code.
4. **Flask-Migrate**. Uses SQLAlchemy and Alembic to automate DB Migration.
5. **Docker**. Allows to run locally the application like it will be ran in production.

