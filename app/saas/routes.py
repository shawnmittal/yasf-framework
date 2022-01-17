from flask import render_template
from flask_login import current_user, login_required
from app.saas import bp

@bp.route('/charts')
@login_required
def charts():
    return render_template('saas/charts.html')