from classes.Pthreading import Pthreading

class CentralProcessor():

    def __init__(self,curent_timestamp,default_api_code,last_schedules):
        self.curent_timestamp = curent_timestamp
        self.default_api_code = default_api_code
        self.last_schedules = last_schedules

    @staticmethod
    def zone_periodic_prediction(zone,host='192.168.43.209'):
        p = Pthreading(zone,host)
        p.start()


    @staticmethod
    def periodic_prediction_schedular(host='192.168.43.209'):
        # def proce():
        #     print 'process created'
            # threadList = []
        for i in range(1,11):
            if i ==9:
                continue
            p = Pthreading(i,host)
            p.start()
                # threadList.append(p)

        # process = multiprocessing.Process(target=proce)
        # process.start()
        # process.join()


        # for i in range(1,11):
        #     if i == 9:
        #         continue
        #     threadList[i].join()
        #     print('thread {} exits'.format(i))

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
    # CentralProcessor.periodic_prediction_schedular(4)
    # CentralProcessor.periodic_prediction_schedular(host='192.168.43.91')
    CentralProcessor.zone_periodic_prediction(1,'192.168.43.91')