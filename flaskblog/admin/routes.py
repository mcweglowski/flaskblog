from flask import Blueprint, render_template, request, redirect, url_for
from flaskblog import db
from flaskblog.admin.forms import ManageUserForm
from flaskblog.models import User
from flask_login import login_required
from flask_user import roles_required

admin = Blueprint('admin', __name__)

@admin.route('/users')
@login_required
@roles_required('admin')
def users():
    all_users = User.query.all()
    return render_template('admin_users.html', title='Manage Users', users=all_users)

@admin.route('/users/<int:user_id>/update', methods=['POST', 'GET'])
@login_required
@roles_required('admin')
def manage_user(user_id):
    user = User.query.get_or_404(user_id)
    form = ManageUserForm()
    if form.validate_on_submit():
        user.is_active = form.is_active.data
        user.is_banned = form.is_banned.data
        db.session.commit()
        return redirect(url_for('admin.users'))
    elif request.method == 'GET':
        form.id.data = user.id
        form.username.data = user.username
        form.email.data = user.email
        form.is_active.data = user.is_active
        form.is_banned.data = user.is_banned
    return render_template('admin_user.html', title='Manage User', form=form, legend='Manage User')