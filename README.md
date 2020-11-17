# SeleniumPrestashopTester
Bot created using Selenium with Python to test online shop created with PrestaShop for educational purposes.

Python version 3.7
Packages:
  - Faker
  - Unidecode
  - future
  - selenium

In order to run it u need to have chromedriver installed (appropriate to the chrome version u have installed), provide shop address and path to the driver in config.json.
To run it simply run main.py, bot will randomly choose categories and products (numbers provided in config), add random quantity of each of the chosen products from <1, max(stock_size, 20), go to cart, delete randomly selected products from the cart (number provided in config), create account for the randomly generated user, pick random shipping method, pick payment method (provided in config), confirm, go to account -> order history and check the details of order. 

