from employee import Employee
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/employee")
def home():
    # Employee.create(full_name='Einstein', kra_pin_number='1234xs567', department='ICT', position='Systems Analyst',
    #                 basic_salary=50000, house_allowance=60000)

    allEmployees = Employee.select()

    return render_template("addEmployee.html")

@app.route("/SaveEmployee")
def save():
    return einstein


if __name__ == "__main__":
    app.run(debug=True, port='5005')


