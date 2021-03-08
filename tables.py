from app import db

class Employee(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    team = db.Column(db.String(35), nullable=True)
    department = db.Column(db.String(25), nullable=False)

class Client(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(30), nullable=False)
    contact_name = db.Column(db.String(30), nullable=False)
    contact_surname = db.Column(db.String(30), nullable=True)
    phone = db.Column(db.String(20), nullable=False)
    details = db.Column(db.String(150), nullable=True)
    #customer= db.relationship('sales', backref='client')

class Sales(db.Model):

    #id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    #customer= db.relationship('employee', backref='sales')



db.drop_all()
db.create_all()