from flask import Flask, url_for
from config import Configuration
from flask_restful import Api
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config.from_object(Configuration)

api = Api(app)
db = SQLAlchemy(app)


# описание объектов в базе данных
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


# описание объектов в базе данных
class Dept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __init__(self, *args, **kwargs):
        super(Dept, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '(id: {}, DeptName: {})'.format(self.id, self.name)


#
# проба вариантов отображения информации
#

class index(Resource):
    def get(self):
        return {'/dept': 'list'}


class addDept(Resource):
    def get(self, deptname):
        work = Dept(name=deptname)
        db.session.add(work)
        db.session.commit()
        return {'add in db, done.': deptname}




WorkersListQuery = Workers.query.all()
dept_names = {}
Dept_id = []
DeptListQ = Dept.query.all()

for i in range(len(DeptListQ)):
    dept_names[DeptListQ[i].id] = DeptListQ[i].name
    Dept_id.append(DeptListQ[i].id)


DeptList = {a: {} for a in dept_names.values()}

for id in Dept_id:
    for number in range(len(WorkersListQuery)):
        if id == int(WorkersListQuery[number].deptname):
            DeptList[dept_names[id]][WorkersListQuery[number].fullname] = {'id': WorkersListQuery[number].id, 'deptname' : dept_names[int(WorkersListQuery[number].deptname)], 'name': WorkersListQuery[number].fullname, 'salary' : WorkersListQuery[number].salary}


class showDept(Resource):
    def get(self):
        return DeptList




class showWorker(Resource):
    def get(self):
        plist = {}
        row = Workers.query.all()
        for id in range(len(row)):
            fio = row[id].fullname
            birthday = str(row[id].birthday)
            deptid =row[id].deptname
            dept = Dept.query.all()[row[id].deptname-1].name
            salary = row[id].salary
            plist[id+1] = {'name': fio, 'birthday': birthday, 'work_id': deptid, 'work': dept,'salary': salary}

        return plist


#
# адреса запросов url_for
#

api.add_resource(index, '/')

api.add_resource(showDept, '/Dept')
api.add_resource(showWorker, '/Piople')
api.add_resource(addDept, '/addDept/<deptname>')



# код для запуска сервиса
if __name__ == '__main__':
    app.run()
