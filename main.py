#namedtuple
# class Employee:
#     def __init__(self,id,name,lastname,age,email):
#         self.id=id
#         self.name=name
#         self.lastname=lastname
#         self.age=age
#         self.email=email
# employees= [
#     (1,"Toxir","Toxirov",27,"toxir@gmail.com"),
#     (2,"Sobir","Sobirov",25,"sobir@gmail.com")
# ]
# for emp in employees:
#     em1=Employee(*emp)
#     print(em1.name)


# from collections import namedtuple
# Employee=namedtuple("Employee","id nam lastname age email")
#
# employees= [
#     (1,"Toxir","Toxirov",27,"toxir@gmail.com"),
#     (2,"Sobir","Sobirov",25,"sobir@gmail.com")
# ]
#
# for employee in employees:
#     em1=Employee(*employee)
#     print(em1.id,em1.nam,em1.lastname,em1.age,em1.email)

# --------------------------------------------------------------------------------------------------------
# Amaliy darsda
# class Car:
#     def __init__(self,id,model,color,speed,price):
#         self.id = id
#         self.model =model
#         self.color = color
#         self.speed = speed
#         self.price = price
# cars=[
#     (1,'AMG 7','Black','300km/h','500000$'),
#     (2,'m6','Light blue','350km/h','600000$'),
#     (3,'Malibu 2','Black','220km/h','26000$')
# ]
# print('models', '|'.center(5),'colors', '|'.center(5),'speed', '|'.center(5),'price')
# for car in cars:
#     car1=Car(*car)
#     print(car1.model,'|'.center(7),car1.color,'|'.center(7),car1.speed,'|'.center(7),car1.price)

# ------------------------------------------------------------------------------------------------------------------------


