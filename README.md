# Encoded strings and uwsgi magic variables

URL encoded strings (AKA [URL Quoting](https://docs.python.org/3/library/urllib.parse.html#url-quoting) in python) don't well play inside configuration files (*.ini files).  
The issues lies in strings containing sequences chars matching to chars in the [magic table of configuration placeholders](The magic table of configuration placeholders).  
It leads to issues like urlencoded strings (i.g.: passwords) being modified by uwsgi process.
Real (and common usage) exemple:  
Given a environmwent varible like `DSN=amqp://admin:ABC_%3F@localhost:5972` and placed at `uwsgi.ini`, when I run the application it's expected to 
get (i.g.: `os.environ['DSN']`) the string `amqp://admin:ABC_%3F@localhost:5972`.   
However, the returned string is something like this: `amqp://admin:ABC_tmpF@localhost:5972`  
Because `%3` (from string `ABC_%3F`) is a reserved placeholder (see magic vars), it  corresponds to a specific component of the full path of the directory containing the config file - in my case, `tmp/` dir.


## Setup and requirements
* Python v2.7
* uwsgi v2.0.18
* any web framework wsgi compatible (such as flask or django)

**Installing minimum requirements:**  
```shell
# cd into this repository directory
python -m venv
./venv/bin/activate
pip install -r requirements.txt
# run application
uwsgi --ini uwsgi.ini
```

