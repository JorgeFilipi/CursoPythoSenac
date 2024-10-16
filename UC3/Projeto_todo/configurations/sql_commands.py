from sqlalchemy import text
from models.user_model import User

def create_table_tasks(app, db):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        conteudo VARCHAR(200) NOT NULL,
        completa BOOLEAN DEFAULT FALSE,
        prioridade VARCHAR(50) NOT NULL
    );"""

    with app.app_context():
        db.session.execute(text(create_table_sql))
        db.session.commit()
        print("Tabela 'tasks' crada com sucesso!")

def create_table_users(app, db):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRiMARY KEY,
        username VARCHAR(255) NOT NULL,
        is_admin BOOLEAN DEFAULT FALSE
    );"""

    with app.app_context():
        db.session.execute(text(create_table_sql))
        db.session.commit()
        print("Tabela 'users' crada com sucesso!")

def create_root_user(app, db):
    with app.app_context():
        root_user = User.query.filter_by(username="root").first()
        if not root_user:
            root_user = User(username="root", is_admin=True)
            root_user.ser_password("root@123")
            db.session.add(root_user)
            db.session.commit()
            print("Usuário 'root' criado com sucesso!")
        else:
            print("Usuário 'root já existe!")