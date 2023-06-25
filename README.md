create .env file on top level with following content
```
DB_USER=...
DB_USER_PASSWORD=...
DB_SERVER=...
DB_NAME=...
```
create virtual environment
```console
python -m venv env
```

activate virtual environment
```console
. ./env/bin/activate
```

install requirements
```console
pip install -r requirements.txt
```
just a VERY USEFUL TIP for vscode on ubuntu using, need to automate process for each new project

import just not work without this
```
export PYTHONPATH="/home/user_name/projects/this_proj_name:$PYTHONPATH"
```