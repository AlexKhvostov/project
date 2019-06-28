from flask import Flask
from config import Configuration
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(Configuration)
api = Api(app)
db = SQLAlchemy(app)


class Workers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deptname = db.Column(db.Integer)
    fullname = db.Column(db.String(30))
    birthday = db.Column(db.Date)
    salary = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super(Workers, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '(id: {}, fullname: {}, deptname: {}, birthday: {}, salary: {})'.format(self.id, self.fullname, self.deptname, self.birthday, self.salary)


class Dept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __init__(self, *args, **kwargs):
        super(Dept, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '(id: {}, DeptName: {})'.format(self.id, self.name)


db.create_all()
tester = Dept(name="Testers")
Galina = Workers(deptname=1, fullname="Galina pupkin", birthday="1984-04-13", salary=550)
Zhenja = Workers(deptname=1, fullname="Zhenja Guzik", birthday="1990-11-21", salary=400)

db.session.add(tester)
db.session.add(Galina)
db.session.add(Zhenja)

db.session.commit()
