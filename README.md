# PIMA Diabetes Modelling
Analyzing the pima dataset,build and deploying a prediction model. 


## Deployment
To run this app locally  
**!! Disclamer !!**

> This has only been tested in linux and unix environments
``` bash
# in flask setup
$ export FLASK_APP=wsgi
$ flask run
 * Running on http://127.0.0.1:5000/

# Using gunicorn
# install gunicorn using pip
$ pip3 install gunicorn
# run the app
$ gunicorn -w 4 wsgi:app
* running on http://127.0.0.1:8000
``` 

