from flask import Blueprint, render_template
from flaskblog.models import User
from flask_login import login_required

admin = Blueprint('admin', __name__)

@admin.route('/users')
@login_required
def users():
    all_users = User.query.all()
    return render_template('admin_users.html', title='Manage Users', users=all_users)

@admin.route('/users/<int:user_id>/update', methods=['POST', 'GET'])
@login_required
def manage_user():
    pass