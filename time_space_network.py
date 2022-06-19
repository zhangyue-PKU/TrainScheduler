from typing import Iterable
import matplotlib
import typing
from collections import OrderedDict

class TSModel:
    def __init__(self, ):
        self.station = []

    def add_one_station(self, name: str, miles: int):
        self.station.append([name, miles])
    
    def add_stations(self, stations: Iterable):
        for item in stations:
            self.station.append([item[0], item[1]])
    
    def add_one_train(self, )
    