from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.fields.core import DateField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG','JPG','png','jpg', 'jpeg', 'JPEG'}

#Create new destination
class EventForm(FlaskForm):
  name = StringField('Name', validators=[InputRequired()])
  venue = StringField('Venue', validators=[InputRequired()])
  event_date = StringField('Event Date', validators=[InputRequired()])
  description = TextAreaField('Description', validators=[InputRequired()])
  category = StringField('Category', validators=[InputRequired()])
  image = FileField('Event Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG,jpeg,JPEG')])
  price = StringField('Price', validators=[InputRequired()])
  status = StringField('Status', validators=[InputRequired()])
  avai_tickets = StringField('Available Tickets', validators=[InputRequired()])
  submit = SubmitField("Create event")
    
#User login
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

#User register
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    number = StringField("Contact Number", validators=[InputRequired('Enter Contact Number')])
    address = StringField("Address", validators=[InputRequired('Enter Address')])
    #submit button
    submit = SubmitField("Register")

#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')