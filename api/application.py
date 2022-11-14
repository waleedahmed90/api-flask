# creating a basic flask application 

from flask import Flask, request
from flask import json
from flask_sqlalchemy import SQLAlchemy
import json

# assigning the name to the flask app
app = Flask(__name__)

# configuring a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# Create a Database object and pass in the app object
db = SQLAlchemy(app)

app.app_context().push()

# Making a Database to connect to
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    description = db.Column(db.String(120))
    
    # override the representation method
    def __repr__(self):
        return f"{self.name} - {self.description}"


# simple route or an end-point
@app.route('/')
# Now a method that will be called once someone hits this route

def index():
    #return 'Hello From the Drinks API'
    return 'TUR JAO'


# get all drinks link
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    
    # this drinks object isn't JSON serializable so we do the following workaround
    output = []
    
    for drink in drinks:
        drink_data = {"name": drink.name, "description": drink.description}
        output.append(drink_data)
    
    
    return {"drinks": output}
#     return {"drinks": json.dumps(drinks)}

#GET
@app.route('/drinks/<id>')
def get_drink(id):
    # querying a single drink from database based on the id
    drink = Drink.query.get_or_404(id)
    
    return {"name": drink.name, "description": drink.description}


# post method to add a drink
@app.route('/drinks', methods = ['POST'])
def add_drink():
    drink = Drink(name = request.json['name'], description = request.json['description'])
    db.session.add(drink)
    db.session.commit()
    
    return {"id": drink.id}

# deleting a drink
@app.route('/drinks/<id>', methods = ['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    
    if drink is None:
        return {"error": "drink does not exist"}
    
    db.session.delete(drink)
    db.session.commit()
    
    return {"status": "successfully deleted", "item_id": drink.id}


# # updating a drink
## PUT
@app.route('/drinks/<id>', methods = ['PUT'])
def update_drink(id):
    drink = Drink.query.get(id)
    
    if drink is not None:
        if 'name' in request.json.keys():
            drink.name = request.json['name']
            db.session.add(drink)
            db.session.commit()
        if 'description' in request.json.keys():
            drink.description = request.json['description']
            db.session.add(drink)
            db.session.commit()
        if 'name' not in request.json.keys():
            return {"warning_name": "name value not given"}
        if 'description' not in request.json.keys():
            return {"warning_description": "description value not given" }
    else:
        return {"error": "item not found"}
    
    return {"message": "drink added successfully", "id": id}
    