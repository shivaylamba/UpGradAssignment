# UpGradAssignment
Product Showing Webpage using FLASK

## Assignment:
Product Showing Webpage using FLASK :

## Overview
You have to create a Flask based product showing web app where user can see different products and can search products according to the name.

## Objectives -
1. Create a database in sqlite
2. Store dummy details of products and show them on the main page
3. Create a working search bar
4. Create a user interface
5. Mail the details of the product in which the user is interested

## Steps to run locally

> Step 1 : create a virtual environment

> Step 2 : clone this repo
```
git clone https://github.com/shubham-chhimpa/UpGradAssignment.git
```
> Step 3 : edit config.py
 edit the following code according to your gmail username and gmail app password 

```python
    # change this to your gmail username and password
    MAIL_USERNAME='your_gmail',
    MAIL_PASSWORD='your_gmail_apps_password_key'
```

NOTE : The mail function only works when your have done [two-step verification to your gmail account](https://support.google.com/accounts/answer/185839?co=GENIE.Platform%3DDesktop&hl=en) and then you can get your [app password](https://myaccount.google.com/apppasswords
)

> Step 4 : go to the terminal and go to /UpGradAssignment/ directory using cd command and then run virtual environment
(skip this step if you already in done)

> Step 5 : run the following command to install required libs

```
pip install -r requirements.txt

```
> step 6 : now run app.py that will run your app locally

> step 7 : open following url in your browser
```
http://127.0.0.1:5000/
```

