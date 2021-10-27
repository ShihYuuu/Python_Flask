import os
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask import Flask
from datetime import datetime

#  取得目前文件資料夾路徑
pjdir = os.path.abspath(os.path.dirname(__file__))
FILE_PATH = f'{pjdir}/db1.sqlite'
DB_URI = 'sqlite+pysqlite:///{file_path}'
app = Flask(__name__)

#  設置sqlite檔案路徑
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI.format(file_path=FILE_PATH)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()

"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    text = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, server_default=func.now())

new_user = User(id = 2,
                username = 'username',
                text = 'text',
                timestamp = datetime.utcnow())

db.session.add(new_user)
db.session.commit()
"""