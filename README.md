# Undesired effect when placing URL encoded strings in uwsgi ini files (such as encoded passwords)

## Setup and requirements
* Python v2.7
* uwsgi v2.0.18
* any web framework wsgi compatible (such as flask or django)

** Installing minimum requirements: **  
```shell
# cd into this repository directory
python -m venv
./venv/bin/activate
pip install -r requirements.txt
# run application
uwsgi --ini uwsgi.ini
```

