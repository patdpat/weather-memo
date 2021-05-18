## 01219325 Software Development Security 

# Project Description 

This application is about the weather forecast and pm2.5 that can tell you what today's weather looks like and you should go out or not, and lastly what's the current air quality is. The data source contains the weather forecast, temperature, current air quality, current weather.

The project is a group project with 4 - 6 members, but we only do it with 2 people

- [x] Develop a web application that is secured.  

- [x] The application should store data in a database.  

- [x] The application should connect to an API. 

- [x] The application can be written in any programming language and framework.  

# The application should follow OWASP security requirements as much as possible. 

##### AUTHENTICATION SYSTEMS (Signup/Signin/2 Factor/Password reset) 
- [ ] Use HTTPS everywhere.
- [ ] Destroy the session identifier after `session close`.  
- [ ] Destroy all active sessions.  
- [ ] Must have the `state` parameter in OAuth2.
- [ ] No open redirects after successful lquery or in any other intermediate luanch.
- [ ] When parsing input, sanitize for javascript://, data://, CRLF characters. 
- [ ] Set secure, httpOnly cookies.


##### USER DATA & AUTHORIZATION
- [ ] Any resource access like, `weather`, `my city data` should check the logged in user's ownership of the resource using session id.
- [ ] Serially iterable resource id should be avoided. Use `/city/weather` instead of `/city/37153/orders`.
- [ ] Use JWT if required for single page app/APIs.

##### Database
- [ ]  Use encryption for data identifying users and sensitive data like access tokens, email addresses or billing details.
 - [ ] Fully prevent SQL injection by only using SQL prepared statements. For example: if using NPM, don’t use npm-mysql, use npm-mysql2 which supports prepared statements.

##### SANITIZATION OF INPUT
- [ ] `Sanitize` all user inputs or any input parameters exposed to user to prevent [XSS]
- [ ] Sanitize Outputs before displaying to users.

##### Cloud Configuration
 - [ ] Ensure all services have minimum ports open. While security through obscurity is no protection, using non-standard ports will make it a little bit harder for attackers.
 - [ ] Host backend database and services on private VPCs that are not visible on any public network. Be very careful when configuring AWS security groups and peering VPCs which can inadvertently make services visible to the public.
  - [ ] Isolate logical services in separate VPCs and peer VPCs to provide inter-service communication.
  - [ ] Ensure all services only accept data from a minimal set of IP addresses.


##### PEOPLE
- [ ] limit access to user databases.
 

## Members

Apipark Withedvorrakit 6110546429
Sidtipat Kietchai 6110546046

Natthaphon Rakprakobkij 6110546402


# The overview of Weather-memo


# How to run our project
1. Clone the repository.

```
  $ git clone https://github.com/patdpat/weather-memo.git
```

2. Create virtualenv in the directory and activate virtualenv.
if you do not have virtualenv, install it with this command

```
  $ python3 -m pip install --user virtualenv
```
then 

```
  $ virtualenv venv
```

3. Activate the venv

    On MacOS and Linux:

    ```
      $ source venv/bin/activate
    ```

    On Windows:

    ```
      $ venv\Scripts\activate
    ```

5. Install all required packages and then run database migrations.

```
  pip3 install -r requirements.txt
  python3 manage.py makemigrations
  python3 manage.py migrate
```

6. Run the server.

```
  python3 manage.py runserver
```
api from application database is provided on `localhost:8000/myapi`


OWASP security