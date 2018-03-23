class Regression():

    def __init__(self,default_hyprerparameter,epoch_loss,batch_loss,epoch_accuracy):
        self.default_hyprerparameter = default_hyprerparameter
        self.epoch_loss = epoch_loss
        self.batch_loss = batch_loss
        self.epoch_accuracy = epoch_accuracy

    def read_dataset(self):
        pass

    def create_model(self):
        pass

    def train(self):
        pass

    def test(self):
        pass

    def save_model(self):
        pass