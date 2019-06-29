from app import db


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


