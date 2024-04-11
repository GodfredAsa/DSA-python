
""" Dependency Inversion Principle (DIP).

- Abstractions should not depend upon details. Details should depend upon abstractions.

In this redesign of your classes, 
you’ve added a DataSource class as an abstraction that provides the required interface, 
or the .get_data() method. 
Note how FrontEnd now depends on the interface provided by DataSource, which is an abstraction.

Then you define the Database class, 
which is a concrete implementation for those cases where you want to retrieve the data from your database. 
This class depends on the DataSource abstraction through inheritance. 
Finally, you define the API class to support retrieving the data from the REST API. 
This class also depends on the DataSource abstraction.

"""

from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source: 'DataSource'):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"
    


db_front_end = FrontEnd(Database())
db_front_end.display_data()


api_front_end = FrontEnd(API())
api_front_end.display_data()