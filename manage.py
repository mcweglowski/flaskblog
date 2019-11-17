from flaskblog import create_app, db, bcrypt
from flaskblog.static_data.SeedSecurity import SeedSecurity
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('seed', SeedSecurity(app, db, bcrypt))

if __name__ == '__main__':
    manager.run()