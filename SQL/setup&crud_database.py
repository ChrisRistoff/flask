from main import database, Main

# this will create all the tables
database.create_all()

user1 = Main("Kris", "krsnhrstv@gmail.com ")
user2 = Main("Puffie", "poffee@gmail.com")

# database.session.add(user1) to add a single user
database.session.add_all([user1, user2])

database.session.commit()

# reading the whole database
users = Main.query.all()

# selecting data by id
selected_user = Main.query.get(2)


# filter by data
# .all() will return a list of all the data that matches the filter
# .first() will return the first data that matches the filter
selected_user_by_name = Main.query.filter_by(name="Kris")
print(selected_user_by_name.all())


# updating data
first_user = Main.query.get(1)
first_user.name = "Kristopher"
database.session.add(first_user)
database.session.commit()

# deleting data
second_user = Main.query.get(2)
database.session.delete(second_user)
database.session.commit()
