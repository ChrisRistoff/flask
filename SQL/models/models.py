from main import db, Users, Tech, Brand

kra = Users("Kris")
puf = Users("Puffie")

db.session.add_all([kra, puf])


kra = Users.query.filter_by(name="Kris").first()
puf = Users.query.filter_by(name="Puffie").first()

# create brand object
samsung = Brand("Samsung", kra.id)

# create tech object
tech1 = Tech("Samsung Galaxy", kra.id)
tech2 = Tech("Samsung Galaxy G", kra.id)

db.session.add_all([samsung, tech1, tech2])
db.session.commit()

# add

kra = Users.query.filter_by(name="Kris").first()
print(kra)

print(kra.report_tech())
