from flaskblog.models import User, Role

class SeedSecurity():
    self.app = None
    self.db = None
    self.bcrypt = None

    def run(self):
        user_admin = seed_user_admin()
        role_admin = seed_role_admin()
        seed_userrole_admin(user_admin, role_admin)

    def seed_user_admin():
        with self.app.app_context():
            user = User.query.filter_by(username="admin").first()
            if user is None:
                user = User(username="admin", email="admin@email.com", password=self.bcrypt.generate_password_hash("admin").decode('utf-8'))
                self.db.session.add(user)
                self.db.session.commit()
            return user

    def seed_role_admin():
        with self.app.app_context():
            roles = Role.query.filter(name="admin" or name="user")
            admin = roles.filter_by(name="admin").first()
            user = roles.filter_by(name="user").first()

            if admin is None:
                admin = Role(name="admin")
                self.db.session.add(admin)
            if user is None:
                user = Role(name="user")
                self.db.session.add(user)
            self.db.session.commit()
            
            return roles

    def seed_userrole_admin(user_admin, role_admin):
        with self.app.app_context():
            userrole = UserRole.query.filter_by(user_id=user_role.id, role_id=role_admin.id).first()
            if user_admin is None or role_admin is None:
                raise Exception('Admin role and Admin user should be defined before adding user to role')
            elif userrole is None:
                userrole = UserRole(user_id=user_admin.id, role_id=role_admin.id)
                self.db.session.add(user_role)
                self.db.session.commit()