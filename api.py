from flask import Flask
import jsonsempai #json-sempai
import json
import logging

from flask_restful import reqparse, abort, Api, Resource
from RESTapi import Workers, Dept
from RESTapi import app

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker
from setting_sql import settingSQL


api = Api(app)



# add filemode="w" to overwrite

logging.basicConfig(filename="sample.log", level=logging.DEBUG , filemode="w" )

logging.debug("This is a debug message")
logging.info("Informational message:")
logging.error("An error has happened!")




#Создаем подключение к базе данных с использованием логина и пароля
engine = create_engine(settingSQL)
#открываем сессию  ( пока не понятно замем. В расках сессии идет работа с базой и пользователями.
Session = sessionmaker(bind=engine)
# Создаем объекат session класса Session() для общения с базой данных
session = Session()

# post_item = Post.query.all()
# TODOS = []
# for number in range(3):
#     TODOS.append(post_item[number].title)
#     for number2 in range(3):
#         TODOS[number] = [post_item[0].body, post_item[1].body, post_item[2].body]

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

#WorkList = {}


WorkersListQuery = Workers.query.all()


WorkersList = {a: {} for a in range(1, len(WorkersListQuery)+1)}
for number in range(len(WorkersListQuery)):
    WorkersList[number+1] = {'id': WorkersListQuery[number].id, 'deptname': WorkersListQuery[number].deptname, 'name': WorkersListQuery[number].fullname, 'salary' : WorkersListQuery[number].salary}


# WorkList
# return list workers
class Workerss(Resource):
    def get(self):
        return WorkersList

dept_names={}
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


class Dept(Resource):
    def get(self):
        return DeptList


def test():
    return 'Hello', 1, [1, 2, 3]


class Worker(Resource):
    def get(self, worker_id):
        return ({'id': WorkersListQuery[int(worker_id)].id, 'deptname': dept_names[int(WorkersListQuery[int(worker_id)].deptname)], 'name': WorkersListQuery[int(worker_id)].fullname, 'salary' : WorkersListQuery[int(worker_id)].salary}, 200, )

    def delete(self, worker_id):
        #abort_if_todo_doesnt_exist(worker_id)
        print(Workers.query.filter_by(id=int(worker_id)).first())
        session.query(Workers).filter(Workers.id == int(worker_id)).delete()
        a =Workers.query.filter_by(id=4).first()
        logging.info('dell item : '+str(a))
        return '', 204


 #   item = Workers(deptname, fullname, birthday, salary)
##
## Actually setup the Api resource routing here
##
#api.add_resource(TodoList, '/todos')
#api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(Workerss, '/workers')
api.add_resource(Worker, '/workers/<worker_id>')
api.add_resource(Dept, '/dept')

session.commit()

if __name__ == '__main__':
    app.run(debug=True)


