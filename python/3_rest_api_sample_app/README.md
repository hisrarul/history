sudo apt-get install python3-venv

#### Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
export FLASK_APP=application.py
export FLASK_ENV=development
```


#### Create database
```bash
Open python3 interactive shell
from app import db
db.create_all()
```

#### Create object in object relational mapper
```python
from app import Drink
drink = Drink(name="Soda", description="Taste like soda")
db.session.add(drink)
db.session.commit()
```

#### Query data
```python
Drink.query.all()
```

#### Referred
+ [Caleb Curry Youtube's Video](https://www.youtube.com/watch?v=qbLc5a9jdXo)
