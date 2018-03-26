from utils.function_schedular import FunSch
from Regression import Regression
from FetchDataUnit import FetchData
class CentralProcessor():

    def __init__(self,curent_timestamp,default_api_code,last_schedules):
        self.curent_timestamp = curent_timestamp
        self.default_api_code = default_api_code
        self.last_schedules = last_schedules

    @staticmethod
    def periodic_prediction_schedular():
        r = Regression()
        f = FetchData()
        a = f.gettestdata()
        tup = (r.predict,(a, 'first test', 1))
        FunSch.startNextHour(tup)


    def periodic_training_schedular(self):
        pass

    def save_training_module(self):
        pass

    def load_regressor(self):
        pass

    def predict(self):
        pass

    def schedule_training(self):
        pass

if __name__== '__main__':
    CentralProcessor.periodic_prediction_schedular()