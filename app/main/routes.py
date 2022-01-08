from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify, current_app, g
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from app import db
from app.models import User
from app.main import bp

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())
    
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title=_('Home'))