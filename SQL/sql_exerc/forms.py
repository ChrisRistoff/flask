from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class AddForm(FlaskForm):
    name = StringField("Item Model")
    submit = SubmitField("Add Item")


class DeleteForm(FlaskForm):
    id = IntegerField("Id Number of Item to Delete")
    submit = SubmitField("Delete Item")
