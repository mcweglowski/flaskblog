from flaskblog.models import User

def seed(app, db, bcrypt):
    with app.app_context():
        user = User.query.filter_by(username="admin").first()
        if user is None:
            user = User(username="admin", email="admin@email.com", password=bcrypt.generate_password_hash("admin").decode('utf-8'))
            db.session.add(user)
            db.session.commit()