# first time database addition

from application import db
from application import Drink

#creating a table
db.create_all()

# making drink objects

drink1 = Drink(name = "grape", description = "tastes like grape" )
drink2 = Drink(name = "cherry", description = "colour is red" )
drink3 = Drink(name = "lemon", description = "tastes like 7up" )

# to add them to the table
db.session.add(drink1)
db.session.add(drink2)
db.session.add(drink3)

# to commit them to the database
db.session.commit()



#testing to retrieve all records
print(Drink.query.all())