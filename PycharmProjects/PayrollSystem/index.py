from payroll import *
from payrollCalculator import Payrollcalculator
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    allEmployees = Employee.select()

    return render_template("index.html", displayEmployees=allEmployees)


@app.route("/employee")
def employee():
    return render_template("addEmployee.html")


@app.route("/saveMyemployee", methods=["POST"])
def saveEmployee():
    name = request.form["form_full_name"]
    kra = request.form["form_kra_pin_number"]
    department = request.form["form_department"]
    position = request.form["form_position"]
    basic = request.form["form_basic_salary"]
    house = request.form["form_house_allowance"]

    Employee.create(full_name=name,kra_pin_number=kra,department=department,position=position,basic_salary=basic,
                    house_allowance=house)
    return redirect(url_for("home"))


@app.route("/updateEmployee/<me>", methods=["POST"])
def update(me):
    # fetch the employee using the id
    emp = Employee.select().where(Employee.id == int(me)).get()
    # update the employee details
    emp.full_name = request.form["form_full_name"]
    emp.kra_pin_number = request.form["form_kra_pin_number"]
    emp.department = request.form["form_department"]
    emp.position = request.form["form_position"]
    emp.basic_salary = request.form["form_basic_salary"]
    emp.house_allowance = request.form["form_house_allowance"]
    emp.save()
    return redirect(url_for("home"))


@app.route("/deleteEmployee/<me>", methods=["GET"])
def deleteEmployee(me):
    # fetch the employee using the id
    emp = Employee.select().where(Employee.id == int(me)).get()
    # delete the employee details
    emp.delete_instance()
    return redirect(url_for("home"))


# payroll routes start here
@app.route("/payroll/<m>")
def payroll(m):
    allPayrolls = Payroll.select().join(Employee).where(Employee.id == int(m))
    return render_template("payroll.html", myPayrolls = allPayrolls, employeeid=m)


@app.route("/payroll/add", methods=["POST"])
def addpayroll():

    employeeids = request.form["form_emp_id"]
    over = request.form["form_overtime"]
    other = request.form["form_other_benefits"]
    payroll_date = request.form["form_payroll_date"]

    x = over
    y = other
    z = payroll_date

    emp = Employee.select().where(Employee.id == employeeids).get()
    print("from emp",emp.full_name)
    calc = Payrollcalculator(over,other,payroll_date)

    Payroll.create(
            overtime=x,
            other_benefits=y,
            payroll_date=z,
            nhif=200,
            nssf=600,
            payee=5000,
            employee_id=employeeids)
    payroll.select()
    return redirect(url_for("payroll", m=employeeids))


if __name__ == "__main__":
    app.run(debug=True, port='5005')


# flask is used to create routes and use routes to pull html files

