from flask import Blueprint, render_template, request, redirect, url_for
from .models import Event

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', event=events)


@bp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = "%" + request.args['search'] + '%'
        events = Event.query.filter(
            Event.description.like(dest)).all()
        events += Event.query.filter(
            Event.name.like(dest)).all()
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))


