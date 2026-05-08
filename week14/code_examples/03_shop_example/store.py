from department import Department

class Store:
    def __init__(self):
        self.__name = ""
        self.__departments = { 'warehouse': Department("warehouse") }

    @property
    def departments(self):
        return self.__departments

    def add_department(self, department_name):
        department = Department(department_name)
        self.__departments[department_name] = department

    def receive_goods(self, department_name, product):
        department = self.departments.get(department_name, self.departments['warehouse'])
        department.add_product(product)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 5:
            print("No!")
            return
        self.__name = value
