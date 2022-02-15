Online Document Scanning with Django and Dynamic Web TWAIN
===============================================================

The sample shows how to combine [Dynamic Web TWAIN](https://www.dynamsoft.com/web-twain/overview/) and [Django](https://docs.djangoproject.com/en/3.2/) to implement a simple online document scanning application with a few lines of code. 

## About Dynamic Web TWAIN

- [![](https://img.shields.io/badge/Get-30--day%20FREE%20Trial%20License-blue)](https://www.dynamsoft.com/customer/license/trialLicense/?product=dwt)


## Python Development Environment

- Python 3.7.9

    ```bash
    python --version
    ```

- Django 3.2.7
    
    ```bash
    python -m pip install Django
    python -m django --version
    ```

## How to Run this Sample

1. Request a trial license of Dynamic Web TWAIN here: https://www.dynamsoft.com/customer/license/trialLicense/?product=dwt
2. Go to the file /static/dwt/Resources/dynamsoft.webtwain.config.js, set license key for Dynamic Web TWAIN.
    
    ```js
    Dynamsoft.DWT.ProductKey = 'LICENSE-KEY';
    ```
2. Run the project:

    ```bash
    python manage.py makemigrations
    python manage.py migrate --run-syncdb
    python manage.py runserver
    ``` 
    
3. Visit `127.0.0.1:8000` in a web browser.

    ![Web document scan by Python Django](https://www.dynamsoft.com/codepool/img/2020/09/django-scan-upload-document.jpg)

## Blog 
[Online Document Scanning Apps with Django and Dynamic Web TWAIN](https://www.dynamsoft.com/codepool/online-document-scanning-django-webtwain.html)





