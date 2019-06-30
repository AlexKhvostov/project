import logging

from app import db, api
from models import Workers, Dept
from flask_restful import reqparse, abort, Resource
from flask_json import FlaskJSON, JsonError, json_response, as_json


''' show all Departments'''

parser = reqparse.RequestParser()
#Department
parser.add_argument('department')
#workers
parser.add_argument('department_id')
parser.add_argument('fullname')
parser.add_argument('birthday')
parser.add_argument('salary')


class DepartmentList(Resource):
    def get(self):
        department_list = {}
        department_all = Dept.query.all()
        for id in range(len(department_all)):
            department_list[str(id+1)] = {'name': department_all[id].name}

        return department_list

    # add Department
    def post(self):
        logging.info("start POST")
        args = parser.parse_args()

        logging.info("start POST , args : "+args['department'])
        print(args['department'])
        logging.info("end POST")

        department_add = Dept(name=args['department'])
        db.session.add(department_add)
        db.session.commit()
        return {'add Deportment: ': args['department']}


class WorkerList(Resource):
    # show all workers
    def get(self):
        worker_list = {}
        worker_all = Workers.query.all()
        for id in range(len(worker_all)):
            worker_list[str(worker_all[id].id)] = {
                'name': worker_all[id].fullname,
                'Department': Department.get(self, worker_all[id].deptname)['name'],
                'Birthday': str(worker_all[id].birthday),
                'Salary': worker_all[id].salary}

        return worker_list

    # add worker /
    # curl http://127.0.0.1:5000/worker -d "fullname=Anton Gorodetskij" -d "birthday=1991-02-02" -d "department_id=2" -d "salary=600" -X POST -v
    def post(self):
        logging.info("start POST")
        args = parser.parse_args()
        logging.info("start POST , args : " + args['fullname']+" / " + args['department_id']+" / " + args['salary']+" / ")
        logging.info("start POST , args : " + args['fullname'])
        print(args['fullname'])
        logging.info("end POST")

        worker_add = Workers(deptname=args['department_id'], fullname=args['fullname'], birthday=args['birthday'], salary=args['salary'])
        db.session.add(worker_add)
        db.session.commit()
        return {'add worker': {
            'deptname': Department.get(self, args['department_id'])['name'],
            'fullname': args['fullname'],
            'birthday': args['birthday'],
            'salary': args['salary']
                }
            }


'''show (1)! one of all Deportments'''

class Department(Resource):
    def get(self, department_id=None):
        department_one = Dept.query.filter_by(id=department_id).first()
        if id:
            department_list = {'id': department_id,
                               'name': department_one.name}

            # department_list = department_list = { ' info :': {' departmaent_id': department_id}}

        else:
            department_list = {' info :': ' error - no departmaent_id'}

        return department_list

    def delete(self, department_id = None):
        if id:
            logging.info("start DELETE DEPT , id : " + department_id)
            Dept.query.filter_by(id=department_id).delete()
            db.session.commit()
            logging.info("save to db : " + department_id)
            department_list = {' info. delete department :':  department_id}
        else:
            department_list = {' info :': ' department_id'}

        return department_list

    def put(self, department_id=None):
        #  curl http://127.0.0.1:5000/department/13 -d "department=teacher" -X PUT -v
        if id:
            logging.info("start POST")
            args = parser.parse_args()
            deportment_one = Dept.query.filter_by(id=department_id).first()
            logging.info("start put / id "+department_id+", args : " + args['department'])
            deportment_one.name = args['department']
            logging.info("end PUT / deportment_one : " + deportment_one.name)

            db.session.commit()
            department_list = {' edit id :': department_id}

        else:
            department_list = {' info :': ' department_id'}

        return department_list


'''show one of all Worker '''

class Worker (Resource):
    def get(self, worker_id = None):
        worker_one = Workers.query.filter_by(id=worker_id).first()
        if id:
            worker_list = {'id': worker_id,
                          'name': worker_one.fullname,
                          'Department': Department.get(self, worker_one.deptname)['name'],
                          'Birthday': str(worker_one.birthday),
                          'Salary': worker_one.salary}
        else:
            worker_list = {' info :': ' error - invalid  worker_id or no worker_id'}

        return worker_list

    def delete(self, worker_id = None):
        if id:
            logging.info("start DELETE WORKER , id : " + worker_id)
            Workers.query.filter_by(id=worker_id).delete()
            db.session.commit()
            logging.info("save to db : " + worker_id)
            worker_list = {' info. delete worker :':  worker_id}

        else:
            worker_list = {}

        return worker_list

    def put(self, worker_id=None):
        if id:
            logging.info("*-*-*-*-*-* start PUT (workers)*-*-*-*-*-*-*")
            args = parser.parse_args()
            worker_one = Workers.query.filter_by(id=worker_id).first()
           # logging.info("start put / id " + worker_id + ", args : " + args['department_id']+", "+ args['fullname']+", "+ args['birthday']+", "+ args['salary']+".")
            if args['department_id']:
                worker_one.deptname = args['department_id']
            if args['fullname']:
                worker_one.fullname = args['fullname']
            if args['birthday']:
                worker_one.birthday = args['birthday']
            if args['salary']:
                worker_one.salary = args['salary']

            logging.info("end PUT / worker_one : " + worker_one.fullname)

            db.session.commit()
            worker_list = {' edit id :': worker_id}

            logging.info("*-*-*-*-*-* end PUT (workers)*-*-*-*-*-*-*")
        else:
            worker_list = {}

        return worker_list


#
########## адреса запросов url_for
#

# show list and add new item
api.add_resource(DepartmentList, '/department')
api.add_resource(WorkerList, '/worker')

# show, edit and delete one item by id
api.add_resource(Department, '/department/<department_id>')
api.add_resource(Worker, '/worker/<worker_id>')