from flask import Flask
from Flask_sqlalchemy import SQLAlchemy

from controllers.task_controller import task_blueprint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE'] = 'sqlite://task.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db_url = SQLAlchemy(app)

app.register_blueprint(task_blueprint)

if __name__ == '__main__':
    app.run(debug=True)