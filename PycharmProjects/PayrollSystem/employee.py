from peewee import *

try:
    db = PostgresqlDatabase('payrollsystem', user='postgres', password="1234", host="127.0.0.1")
    print("Successfully connected!")
except:
    print("Didn't connect!")


class Employee(Model):
    full_name = CharField()
    kra_pin_number = CharField()
    department = CharField()
    position = CharField()
    basic_salary = FloatField()
    house_allowance = FloatField()

    class Meta:
        database = db
        table_name = "employees"


Employee.create_table(fail_silently=True)