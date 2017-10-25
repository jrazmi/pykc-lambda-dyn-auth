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
