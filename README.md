create virtual environment
```bash
python -m venv env
```

activate virtual environment
```bash
. ./env/bin/activate
```

install requirements
```bash
pip install -r requirements.txt
```

create ".env" file with databse keys near "src" directory
```
DB_USER=...
DB_USER_PASSWORD=...
DB_SERVER=...
DB_NAME=...
```

run alembic migrations
```bash
cd ./src/db
alembic upgrade head
```