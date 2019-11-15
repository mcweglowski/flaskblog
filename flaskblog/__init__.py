from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_user import UserManager, SQLAlchemyAdapter

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
db_adapter = None
user_manager = None

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.models import User
    db_adapter = SQLAlchemyAdapter(db, User)
    user_manager = UserManager(db_adapter, app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    from flaskblog.admin.routes import admin
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(admin)

    from flaskblog.static_data import roles
    from flaskblog.static_data import user
    from flaskblog.static_data import userrole
    roles.seed(app, db)
    user.seed(app, db, bcrypt)
    userrole.seed(app, db)

    return app