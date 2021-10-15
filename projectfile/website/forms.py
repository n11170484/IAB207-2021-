from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.fields.core import IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

allowed_file = {'png', 'jpg', 'PNG', 'JPG'}

#Event form
class EventForm(FlaskForm):
    #Event name
    name = StringField('Venue', validators=[InputRequired()])
    #Event description
    description = TextAreaField('Description', validators=[InputRequired()])
    #Event Image
    image = FileField('Event Image', validators=[FileRequired(message='Image must be uploaded'), 
    FileAllowed(allowed_file, message='Sorry, only .png and .jpg files allowed')])
    #Event price
    price = IntegerField('Price', validators=[InputRequired()])
    submit = SubmitField('Create event')


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field


    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")


#Comment form
class CommentForm(FlaskForm):
    text = TextAreaField('Comment:', [InputRequired()])
    submit = SubmitField('Submit')