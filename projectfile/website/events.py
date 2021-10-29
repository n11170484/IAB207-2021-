from flask import Blueprint, render_template, request, redirect, url_for
from .models import Event, Comment
from .forms import EventForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user


bp = Blueprint('event', __name__, url_prefix='/events')


@bp.route('/<id>')
def show(id):
    destination = Event.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm()
    return render_template('events.EventPage.html', #event=event, #this is the link to our html pages
     form=cform)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    print('Method type: ', request.method)
    form = EventForm()
    if form.validate_on_submit():
        # call the function that checks and returns image
        db_file_path = check_upload_file(form)
        event = Event(name=form.name.data, description=form.description.data,
                                  image=db_file_path, price=form.price.data)
        # add the object to the db session
        db.session.add(event)
        # commit to the database
        db.session.commit()
        print('Successfully created new travel destination', 'success')
        # Always end with redirect when form is valid
        return redirect(url_for('event.create'))
    return render_template('events/Createevent.html', form=form)


def check_upload_file(form):
    # get file data from form
    fp = form.image.data
    filename = fp.filename
    # get the current path of the module file… store image file relative to this path
    BASE_PATH = os.path.dirname(__file__)
    # upload file location – directory of this file/static/image
    upload_path = os.path.join(
        BASE_PATH, 'static/img', secure_filename(filename))
    # store relative path in DB as image location in HTML is relative
    db_upload_path = '/static/img/' + secure_filename(filename)
    # save the file and return the db upload path
    fp.save(upload_path)
    return db_upload_path


@bp.route('/<event>/comment', methods=['GET', 'POST'])
def comment(event):
    form = CommentForm()
    # get the destination object associated to the page and the comment
    destination_obj = Event.query.filter_by(id=event).first()
    if form.validate_on_submit():
        # read the comment from the form
        comment = Comment(text=form.text.data,
                          event=event)
        # here the back-referencing works - comment.destination is set
        # and the link is created
        db.session.add(comment)
        db.session.commit()

        # flashing a message which needs to be handled by the html
        flash('Your comment has been added')
        #print('Your comment has been added', 'success')
    # using redirect sends a GET request to destination.show
    return redirect(url_for('events.EventPage', id=event))
