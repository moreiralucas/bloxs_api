# Bloxs

Full-Stack Developer (Python/Flask) - Bloxs Challenge


First of all, create an environment with ```python3 -m venv .venv```, active with ```source .venv/bin/activate``` then install the dependencies ```pip install -r requirements.txt```

Start the container with database:
```docker-compose up -d```

To acess the container, run:
```docker exec -it flask_app bash```


# Database

To migrate the database, run this command:
```
flask db upgrade
```

If there are new changes in models, run again:
```
flask db migrate -m "Another migration."
flask db upgrade
```

To add dummy data, access the flask shell:
```flask shell``` then run:
```python
from scripts import insert_dummy_data
insert_dummy_data()
```

This will add the dummy data in database.

# Tests

To run all tests, access the container and run: ```pytests tests/```.
