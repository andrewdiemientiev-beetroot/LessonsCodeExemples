from abc import ABC

import requests

url = "https://webknox-recipes.p.rapidapi.com/recipes/quickAnswer"

querystring = {"q":"How much vitamin c is in 2 apples?"}

headers = {
    'x-rapidapi-key': "3f2acf1dbcmsha9a8cfb34f1192ep1592a5jsna60287532c2d",
    'x-rapidapi-host': "webknox-recipes.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


class DBInterface(ABC):

    def add(self, data):
        raise NotImplemented

    def delete(self, id_of_record):
        raise NotImplemented

    def update(self, id_of_record, data):
        raise NotImplemented

    def list(self):
        raise NotImplemented


class MySQLConnector(DBInterface):

    def add(self, data):
        print("Saving data to MySQL")

    def delete(self, id_of_record):
        print("Deleting data to MySQL")

    def update(self, id_of_record, data):
        print("Updating data to MySQL")


class MongoDBConnector(DBInterface):

    def add(self, data):
        print("Saving data to MongoDB")

    def delete(self, id_of_record):
        print("Deleting data to MongoDB")

    def update(self, id_of_record, data):
        print("Updating data to MongoDB")

#
# if __name__ == '__main__':
#     app = Flask(db_connector: DBInterface = MySQLConnector)

