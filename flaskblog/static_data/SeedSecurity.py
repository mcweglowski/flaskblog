from flaskblog.models import User, Role, UserRole
from flask_script import Command

class SeedSecurity(Command):
    "Seeds blog initial configuration."
    app = None
    db = None
    bcrypt = None

    def __init__(self, app, db, bcrypt):
        self.app = app
        self.db = db
        self.bcrypt = bcrypt

    def seed_user_admin(self):
        with self.app.app_context():
            user = User.query.filter_by(username="admin").first()
            if user is None:
                user = User(username="admin", email="admin@email.com", password=self.bcrypt.generate_password_hash("admin").decode('utf-8'))
                self.db.session.add(user)
                self.db.session.commit()
            return user

    def seed_role_admin(self):
        with self.app.app_context():
            roles = Role.query.filter_by(name='admin')
            admin = roles.filter_by(name="admin").first()

            if admin is None:
                admin = Role(name="admin")
                self.db.session.add(admin)
                self.db.session.commit()            
            
            return admin

    def seed_userrole_admin(self, user_admin, role_admin):
        with self.app.app_context():
            if user_admin is None or role_admin is None:
                raise Exception('Admin role and Admin user should be defined before adding user to role')

            user_role = UserRole.query.filter_by(role_id=role_admin.id).first()
            if user_role is None:
                user_role = UserRole(user_id=user_admin.id, role_id=role_admin.id)
                self.db.session.add(user_role)
                self.db.session.commit()

    def run(self):
        user_admin = self.seed_user_admin()
        role_admin = self.seed_role_admin()
        self.seed_userrole_admin(user_admin, role_admin)