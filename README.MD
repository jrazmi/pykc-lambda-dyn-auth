# Lambda, Python, DyanmoDB - Authentication Service
### NOTE: Not Production Checked

Setup your [virtualenv](https://virtualenv.pypa.io/en/stable/)

Install: [Flask](http://flask.pocoo.org/), [Zappa](https://github.com/Miserlou/Zappa)

``` $(venv) pip install flask zappa ```

Run your app and make sure local host is returning hello world.

``` $(venv) python app.py ```

### Chapter 01 - Initializing Zappa
``` $ git checkout ch-01 ```

Make sure you have your aws account/creds [setup](http://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html)

```$(venv) zappa init ```

Follow the setup instructions.

```$(venv) zappa deploy```

Assuming no errors zappa will give you a amazon api endpoint.
Verify that your hello world app is up and running!


### Chapter 02 - Boto3 and DynamoDB
``` $ git checkout ch-02 ```

Checkout [boto3](https://boto3.readthedocs.io/en/latest/) docs.

*boto3 is a dependency of zappa and automatically installed if you are using it outside of zappa just $ pip install boto3 where you need it*  

Create a dynamoDB table in your AWS console.

Create a new item in your table.  

Make sure your email endpoint is working locally.
```$(venv) zappa update ```

### Chapter 03 - Lambda Packages and Registration
```$ git checkout ch-03```

There are a number of python packages that need to be pre-compiled in order to run on Lambda.
Our friend Misserlou, creator of zappa, created an external [lambda-packages](https://github.com/Miserlou/lambda-packages) python repo.

```$(venv) pip install -r requirements.txt ```

Review the register app route in app.py

Test it locally with the bash scripts in cmds.

```$(venv) zappa update ```


### Chapter 04 - JWTs and Password hashing.
```$(venv) git checkout ch-04 ```
```$(venv) pip install -r requirements.txt```

Review the login endpoint.

Test it locally

Update Zappa!


### Chapter 05 - Protected Routes
```$(venv) git checkout ch-05 ```
