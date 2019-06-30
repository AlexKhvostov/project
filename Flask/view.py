import logging

from app import db, api
from models import Workers, Dept
from flask_restful import Resource
from flask_json import FlaskJSON, JsonError, json_response, as_json


class showDepts(Resource):
    def get(self):
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
                    DeptList[dept_names[id]][WorkersListQuery[number].fullname] = {
                         'id': WorkersListQuery[number].id,
                         'deptname': dept_names[int(WorkersListQuery[number].deptname)],
                         'name': WorkersListQuery[number].fullname,
                         'salary': WorkersListQuery[number].salary
                    }
        return DeptList


    #      EXAMPLE____

    #
    # def delete(self, todo_id):
    #     abort_if_todo_doesnt_exist(todo_id)
    #     del TODOS[todo_id]
    #     return '', 204
    #
    # def put(self, todo_id):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     TODOS[todo_id] = task
    #     return task, 201
    #


####################################################
####################################################

''' show all Departments'''

class DepartmentList(Resource):
    def get(self):
        department_list = {}
        department_all = Dept.query.all()
        for id in range(len(department_all)):
            department_list[str(id+1)] = {'name': department_all[id].name}

        return department_list

    # add Department
    def post(self):
        pass


class WorkerList(Resource):
    # show all workers
    def get(self):
        worker_list = {}
        worker_all = Workers.query.all()
        for id in range(len(worker_all)):
            worker_list[str(id+1)] = {
                'name': worker_all[id].fullname,
                'Department': Department.get(self, worker_all[id].deptname)['name'],
                'Birthday': str(worker_all[id].birthday),
                'Salary': worker_all[id].salary}

        return worker_list

    # add worker
    def post(self):
        pass


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

    def delete(self, id = None):
        if id:
            department_list = {' info :': ' departmaent_id'}

        else:
            department_list = {' info :': ' departmaent_id'}

        return department_list

    def put(self, id=None, name=None):
        if id:
            department_list = {' info :': ' departmaent_id'}

        else:
            department_list = {' info :': ' departmaent_id'}

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
            worker_list = {}

        else:
            worker_list = {}

        return worker_list

    def put(self, worker_id=None, name=None, deportment=None, birthday=None, salary=None):
        if id:

            worker_list = {}

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