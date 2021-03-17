from app import db



class Employee(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    team = db.Column(db.String(35), nullable=True)
    department = db.Column(db.String(25), nullable=False)
    customer= db.relationship('sales', backref='employee')

class Client(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(30), nullable=False)
    contact_name = db.Column(db.String(30), nullable=False)
    contact_surname = db.Column(db.String(30), nullable=True)
    phone = db.Column(db.String(20), nullable=False)
    details = db.Column(db.String(150), nullable=True)
    customer= db.relationship('sales', backref='client')

class Sales(db.Model):

    date = db.Column(db.DateTime, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

class Expenses(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nature = db.Column(db.String(35), nullable=False)
    vendor = db.Column(db.String(60), nullable=False)
    reason = db.Column(db.String(100), nullable=True)
    hr_expenses = db.relationship('hr', backref='expenses')
    
    #sales_expenses = relationship()
    #operations_expenses = relationship()

class HR(db.Model):

    date = db.Column(db.DateTime, primary_key=True)
    expense_id = db.Column(db.Integer, db.ForeignKey('expenses.id'), nullable=True)
    amount = db.Column(db.Float, nullable=False)
    details = db.Column(db.String(50), nullable=True)





db.drop_all()
db.create_all()