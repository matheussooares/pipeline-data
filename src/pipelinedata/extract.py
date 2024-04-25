import json
import csv
class read:
    def __init__(self,path,data_type):
        self.path = path
        self.data_type = data_type
        self.data = self.read_data()

    def readjson(self):
        data_json = []
        with open(self.path,'r') as file:
            data_json = json.load(file)
        
        return data_json

    def readcsv(self):
        data_csv = []
        with open(self.path,'r') as file:
            spamreader = csv.DictReader(file,delimiter=',')
            for row in spamreader:
                data_csv.append(row)
        return data_csv

    def read_data(self):
        data = []
        if self.data_type == 'csv':
            data = self.readcsv()
        elif self.data_type == 'json':
            data =  self.readjson()
        return data
