Online Document Scanning with Django and Dynamic Web TWAIN
===============================================================

The sample shows how to combine [Dynamic Web TWAIN](https://www.dynamsoft.com/web-twain/overview/) and [Django](https://docs.djangoproject.com/en/3.2/) to implement a simple online document scanning application with a few lines of code. 

## About Dynamic Web TWAIN
- [![](https://img.shields.io/badge/Download-Offline%20SDK-orange)](https://www.dynamsoft.com/web-twain/downloads)
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

## Usage
1. Download and instal [Dynamic Web TWAIN](https://www.dynamsoft.com/web-twain/downloads).
2. Create folder `static/dwt` under the project root directory.
3. Copy and paste `Dynamic Web TWAIN SDK version/Resources` folder to `static/dwt/`.
4. Run the project:

    ```bash
    python manage.py makemigrations
    python manage.py migrate --run-syncdb
    python manage.py runserver
    ``` 
    
5. visit `127.0.0.1:8000` in a web browser.

    ![Web document scan by Python Django](https://www.dynamsoft.com/codepool/img/2020/09/django-working-2-1000x579.png)

## Blog 
[Online Document Scanning Apps with Django and Dynamic Web TWAIN](https://www.dynamsoft.com/codepool/online-document-scanning-django-webtwain.html)





