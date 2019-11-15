from flaskblog.models import Role

def seed(app, db):
    with app.app_context():
        roles = Role.query.all()
        if False == any(x.name == "admin" for x in roles):
            db.session.add(Role(name="admin"))
        if False == any(x.name == "user" for x in roles):
            db.session.add(Role(name="user"))
        db.session.commit()