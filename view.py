from RESTapi import db, api
from models import Workers, Dept
from flask_restful import Resource








class addDept(Resource):
    def get(self, deptname):
        work = Dept(name=deptname)
        db.session.add(work)
        db.session.commit()
        return {'dept': deptname}

api.add_resource(addDept, '/addDept/<deptname>')
