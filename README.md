## Commands for intial setup <br>

&ensp;__Enabling the Python Virtual env [ In Linux Env ]__ <br>

    1. cd cloned_repo_folder
    2. source venv/bin/activate  
    3. sudo apt-get install xvfb



## Install

    pip install -r requirements.txt 

## Run the app

    python3 main.py

## SignUp to RestAPI

### Request

`POST /signup`

    curl --location --request POST 'http://localhost:8000/signup' \
    --header 'content-type:  application/json ' \
    --data-raw '{
        "username":"username",
        "password":"password",
        "retype_password":"password"

    }'

### Response

    {
        "code": 200,
        "status": "Successfully Signed up"
    }

## Login to RestAPI

`POST /login`

### Request

    curl --location --request POST 'http://localhost:8000/login' \
    --header 'content-type:  application/json ' \
    --data-raw '{
        "username":"username",
        "password":"password"

    }'

## Response

    {
        "code": 200,
        "status": "Logged In",
        "token": "b64c2948aa27f52f495c335c773b02072088896e"
    }

## Login to LinkedIn

`POST /login/linkedin`

### Request

    curl --location --request POST 'http://localhost:8000/login/linkedin' \
    --header 'content-type:  application/json ' \
    --data-raw '{
        "api_username":"username",
        "auth_token":"b64c2948aa27f52f495c335c773b02072088896e",
        "linkedin_username":"linkedin_username",
        "linkedin_password":"linkedin_password"

    }'

### Response

    {
        "code": 200,
        "status": "LoggedIn",
        "authenticated": "Yes"
    }

## Getting profile info from linkedin

`POST /profile`

### Request

    curl --location --request POST 'http://localhost:8000/profile' \
    --header 'content-type:  application/json ' \
    --data-raw '{
        "api_username":"username",
        "auth_token":"b64c2948aa27f52f495c335c773b02072088896e",
        "linkedin_username":"linkedin_username",
        "public_id":"test"

    }'

### Response 

    {
      "code":200,"response":linkedin_profile_data
      }

## Getting his/her connection details

`POST /connections`
### Request

    curl --location --request POST 'http://localhost:8000/connections' \
    --header 'content-type:  application/json ' \
    --data-raw '{
        "api_username":"username",
        "auth_token":"b64c2948aa27f52f495c335c773b02072088896e",
        "linkedin_username":"linkedin_username",
        "public_id":"test"

    }'

### Response
    {
      "code":200,
      "response":linkedin_connection_info
    }

