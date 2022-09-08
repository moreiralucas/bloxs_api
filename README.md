# Bloxs

Full-Stack Developer (Python/Flask) - Bloxs Challenge


Start the containers:
```docker-compose up -d```

To acess the container, run:
```docker exec -it flask_app bash```

Then, inside the container, run ```flask db upgrade``` to apply the migrations.

After apply the migrations, it's necessary add dummy data in database. To do this, access the flask shell:

```flask shell``` then run:
```python
from scripts import insert_dummy_data
insert_dummy_data()
```


# Database


If there are new changes in models, run the following commands (inside the container flask_app):
```
flask db migrate -m "Another migration."
flask db upgrade
```


# Tests

To run all tests, access the container flask_app and run: ```pytest tests```.
