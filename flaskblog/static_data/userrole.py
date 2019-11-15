from flaskblog.models import UserRole, User, Role

def seed(app, db):
    with app.app_context():
        user = User.query.filter_by(username="admin").first()
        role = Role.query.filter_by(name="admin").first()
        userrole = UserRole.query.filter_by(user_id=user.id).first()
        if user is None or role is None:
            raise Exception('Admin role and Admin user should be defined before adding user to role')
        elif userrole is None:
            user_role = UserRole(user_id=user.id, role_id=role.id)
            db.session.add(user_role)
            db.session.commit()