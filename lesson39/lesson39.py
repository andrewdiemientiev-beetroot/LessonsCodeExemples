from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from datetime import date

engine = create_engine('sqlite:///hr.db', echo=True)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)


class Employees(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(25))
    email = Column(String(25))
    phone_number = Column(String(25))
    hire_date = Column(Date)
    job_id = Column(String(10), ForeignKey('jobs.job_id')) # DATABASE
    salary = Column(Numeric(precision=2, scale=2))
    commission_pct = Column(Numeric(precision=2, scale=2))
    manager_id = Column(Integer)
    department_id = Column(Integer)

    job = relationship("Jobs", back_populates='employees') # ORM

    def __repr__(self):
        return f"ID: {self.employee_id} First name: {self.first_name}, Last name: {self.last_name}"


class Jobs(Base):
    __tablename__ = 'jobs'

    job_id = Column(String(10), primary_key=True)
    job_title = Column(String(25))
    min_salary = Column(Numeric(precision=2, scale=2))
    max_salary = Column(Numeric(precision=2, scale=2))

    employees = relationship("Employees", back_populates='job')

    def __repr__(self):
        return f"Job_id {self.job_id}, title: {self.job_title}"

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    # employees = session.query(Employees).all()
    # for employee in employees:
    #     print(employee.commission_pct)
    # hire_date = date(year=2008, month=7, day=23)
    # vasia = Employees(employee_id=209,
    #                   first_name='Vasia',
    #                   last_name='Pupkin',
    #                   email='vasia@gmail.com',
    #                   phone_number='535.09.90',
    #                   hire_date=hire_date,
    #                   job_id="IT_PROG",
    #                   salary=30000,
    #                   commission_pct=0,
    #                   manager_id=100,
    #                   department_id=90)
    # session.add(vasia)
    # try:
    #     session.commit()
    # except IntegrityError:
    #     print('ERROR!')
    #     session.rollback()
    #     session.add(vasia)
    #     session.commit()
    # employee = session.query(Employees).first()
    # print(employee.job.job_title)
    vasii = session.query(Employees).filter_by(first_name='Vasia').all()
    for vasia in vasii:
        vasia.first_name = 'Petia'
        session.add(vasia)
    session.commit()
    for petia in session.query(Employees).filter_by(first_name='Petia').all():
        print(petia)