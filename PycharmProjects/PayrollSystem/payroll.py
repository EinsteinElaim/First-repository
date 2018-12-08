from employee import *
from peewee import *


class Payroll(Model):
    payroll_date = DateField()
    overtime = FloatField()
    other_benefits = FloatField()
    nhif = FloatField()
    nssf = FloatField()
    payee = FloatField()
    employee_id = ForeignKeyField(Employee, to_field='id', on_update="cascade")


    class Meta:
        database = db
        table_name = "payrolls"

Payroll.create_table(fail_silently=True)