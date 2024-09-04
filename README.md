### Food Delivery Web API
#### How to run this project
<hr>


<br>
Fist clone the repository using the following command

```bash
git clone https://github.com/0rakib0/Food-delivery-API.git
# After cloning, move into the directory having the project files using the change directory command
cd Food-delivery-API
```
Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python3 -m venv env
```
Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```
Install all the project Requirements
```bash
pip install -r requirements.txt
```
-Apply migrations and create your superuser (follow the prompts)
```bash
# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser
```

Run the development server

```bash
# run django development server
python manage.py runserver
```

### Project Documentation
<hr>

- In this project, there are 2 types of user roles: **Employee** and **Owner**.
- Only authorized users can access all APIs.
- Only the **Owner** and **Employee** can manage menus, categories, and modifiers.
- There is an API for placing orders and receiving payments.


### All API Routs
<hr>

- Add Category- `http://localhost/add-category/`
- Add Menu Item- `http://localhost/add-menu-item/`
- Add Modifier Item- `http://localhost/add-modifier-item/`
- Order Place- `http://localhost/order-place/`
- Receive Payment- `http://localhost/receive-payment/`
- Menu List- `http://localhost/menus/resturent_id/` ID must be integer
- Category List- `http://localhost/category/resturent_id/` ID must be integer
- Modifier Item List- `http://localhost/modifier/item_id/` ID must be integer
