from flask import Flask
from flask import render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import pymysql
import secrets

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app)


class ewestby_animalsapp(db.Model):
    animalID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Country = db.Column(db.String(255))
    Weight = db.Column(db.Integer)
    Quantity = db.Column(db.Integer)
    
    def __repr__(self):
        return "id: {0} | Name: {1} | Country: {2} | Weight: {3} | Quantity: {4}".format(self.id, self.Name, self.Country, self.Weight, self.Quantity)


class AnimalForm(FlaskForm):
    Name = StringField('Animal Name:', validators=[DataRequired()])
    Country = StringField('Country:', validators = [DataRequired()])
    Weight = IntegerField('Weight:', validators = [DataRequired()])
    Quantity = IntegerField('Quantity:', validators = [DataRequired()])
    

@app.route('/')
def index():
    all_animals = ewestby_animalsapp.query.all()
    return render_template('index.html', animals = all_animals, pageTitle = 'Eric\'s Animals')

@app.route('/add_animal', methods =['GET', 'POST'])
def add_animal():
    form = AnimalForm()
    if form.validate_on_submit():
        animal = ewestby_animalsapp(Name = form.Name.data, Country = form.Country.data, Weight = form.Weight.data, Quantity = form.Quantity.data)
        db.session.add(animal)
        db.session.commit()
        return redirect('/')
    
    return render_template('add_animal.html', form=form, pageTitle='Add a New Animal')


if __name__ == '__main__':
    app.run(debug=True)