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
*boto3 gets is a dependency of zappa if you are using it outside of zappa just pip install boto3*  

Create a dynamoDB table in your AWS console.

Create a new item in your table.  

Make sure your email endpoint is working locally.
```$(venv) zappa update ```
