from datetime import datetime
from flask import render_template, g, flash, current_app
from flask_login import current_user
from flask_babel import _, get_locale
from app import db
from app.landing import bp
from app.landing.forms import contactForm
from app.email import send_email

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())
    
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    contact_form = contactForm()
    if contact_form.validate_on_submit():
        send_email(('[YASF App] Reset Your Password'),
               sender='shawn@shawnmittal.com',
               recipients=[contact_form.email.data],
               text_body='test',
               html_body='test')
        flash("Thanks, we'll get back to you as soon as possible!")
    return render_template('index.html', title=('Home'), form=contact_form)