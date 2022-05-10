# SHOP-REST
## This project is simple REST API for shop which allows users to do CRUD operations on their own products. They are also able to retrieve information about specific user and his sale offers.

---
# Setup:
Requirements:
  + docker

Make .env file which should contain:
  + SECRET_KEY
  + POSTGRES_PASSWORD
    
## Start:
Run command inside project directory: docker-compose up

## Stop:
Press CTRL + C or in another window run command: docker-compose down

---
# ENDPOINTS :
## Authentication:
  + **/auth/register/** [POST] - register user

Content:

    {
    "username": "",
    "password": ""
    }

  + **/auth/obtain-token/** [POST} - get token for token authentication 

  Content: 

    {
    "username": "",
    "password": ""
    }

  + **/auth/account/{account_id}/** [GET] - get information about particular user
## Category:
  + **/categories/** [GET] - list of all categories (order by name ASC)

Example response:

    [
    {
        "id": 2,
        "name": "art",
        "slug": "art"
    },
    {
        "id": 1,
        "name": "electronics",
        "slug": "electronics"
    }
    ]
## Products:
+ **/products/** - [GET] Retrieve all products (paginated - 8 products per page)
  + Parameters [optional]:
    + search - search inside 'name' and 'description' for given string (not case sensitive)
    + ordering - fields [name, price, created, province] for ASC "=field" name, for DESC "=-field_name"
    + price__gt - Price must be higher than given number
    + price__lt - Price must be less than given number
    + created__gt - Created date must be higher than given number
    + created__lt - Created date must be less than given number 

Example:

Request [GET]: 
/products/?search=Apparat&price__gt=10&price__lt=200&created__gt=2000-01-01&created__lt=2022-05-10&ordering=-created

Response: 

    {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "apparat",
            "price": "12.00",
            "created": "2022-04-27T10:52:38.538319Z",
            "province": "Lower Silesia"
        }
    ]
    }
count - total number of retrieved products (not on the page)

next - link to next page

previous - link to previous page

results - list of products for current page

+  **/{category_slug/products/** [GET] - filter products for particular category, all parameters above are available

+ **/products/** [POST] - Post a product, takes current user as an author 


Headers : 
  + KEY: Authorization
  + VALUE: Token {user_token}

Content: 

    {
    "name": "",
    "price": null,
    "description": "",
    "province": "",
    "phone_number": "",
    "category": primary_key_of_category
    }

name - string, max length = 50

price = decimal, max digits = 8, decimal places = 2

description - text field

province - string - one of:
  + Lower Silesia
  + Kuyavia-Pomerania
  + Lodzkie
  + Lublin
  + Lubusz
  + Lesser Poland
  + Masovia
  + Subcarpathia
  + Pomerania
  + Silesia
  + Warmia-Masuria
  + Greater Poland
  + West Pomerania

phone_number - string - 9 digits inside

category - primary key - one of categories (**check Category endpoint**)

+ **/product/{product_id}/** [GET] - retrieve particular product

Example request: /products/1/

Example response:

    {
    "id": 1,
    "author": {
        "id": 3,
        "username": "newUser1234",
        "date_joined": "2022-04-27T10:30:51.241520Z",
        "last_login": "2022-04-27T10:48:32.563488Z"
    },
    "name": "apparat",
    "price": "12.00",
    "description": "Factory new apparat",
    "created": "2022-04-27T10:52:38.538319Z",
    "province": "Lower Silesia",
    "phone_number": "987654321",
    "category": "electronics"
    }

+ **/product/{product_id}/** [PUT, PATCH] - update particular product (must be author)

Headers : 
  + KEY: Authorization
  + VALUE: Token {user_token}

Content: 
    
    {
    "name": "",
    "price": null,
    "description": "",
    "province": "",
    "phone_number": "",
    "category": null
    }

province - one of provinces, which are listed above

category - primary key of category (check Category endpoint)

+ **/product/{product_id}/** [DELETE] - delete particular product (must be author)

Headers : 
  + KEY: Authorization
  + VALUE: Token {user_token}