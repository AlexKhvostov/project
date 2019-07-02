from app import app
from flask import render_template, request, Flask, jsonify
from flask_restful import reqparse, abort, Resource
import requests, logging


@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def index():
    filtr_date = {'birthday_begin': '1950-01-01', 'birthday_end': '2020-01-01'}

    # added new workers or new department
    if request.method == 'POST':
        logging.info(" method POST. first level ")
        if request.form.get('fullname'):
            logging.info("fullname :"+request.form.get('fullname'))
            post_arguments = {'fullname': request.form.get('fullname'),
                              'department_id': request.form.get('department_id'),
                              'birthday': request.form.get('birthday'),
                              'salary': request.form.get('salary')}
            requests.post('http://127.0.0.1:5000/worker', post_arguments)

        elif request.form.get('department'):
            logging.info(" method POST. first lavel " + request.form.get('department'))
            post_arguments = {'department': request.form.get('department')}
            requests.post('http://127.0.0.1:5000/department', post_arguments)

        elif request.form.get('worker_delete'):
            requests.delete('http://127.0.0.1:5000/worker/'+str(request.form.get('worker_delete')))

        elif request.form.get('department_delete'):
            requests.delete('http://127.0.0.1:5000/department/' + str(request.form.get('department_delete')))





    departments = requests.get('http://127.0.0.1:5000/department').json()
    workers = requests.get('http://127.0.0.1:5000/worker', filtr_date).json()

    for i in departments:
        salary_sum = 0
        num = 0
        for j in workers:
            if departments[i]['name'] == workers[j]['department']:
                salary_sum += int(workers[j]['salary'])
                num += 1

        if num:
            delta_salary = salary_sum / num
        else:
            delta_salary = 0
        departments[i]['delta_salary'] = delta_salary

    numb = range(10)
    return render_template('index.html', name=workers, depart=departments, numb=numb)


