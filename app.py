from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SuperSecretKey'

class AnimalForm(FlaskForm):
    Name = StringField('Animal Name:', validators=[DataRequired()])
    Country = StringField('Country:', validators = [DataRequired()])
    

@app.route('/')
def index():
    return render_template('base.html', pageTitle = 'Eric\'s Animals')

@app.route('/add_animal', methods =['GET', 'POST'])
def add_animal():
    form = AnimalForm()
    if form.validate_on_submit():
        return "<h2> The animal is {0} from {1}".format(form.Name.data, form.Country.data)
    
    return render_template('add_animal.html', form=form, pageTitle='Add a New Animal')


if __name__ == '__main__':
    app.run(debug=True)