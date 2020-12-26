
class DataContainer():

    def __init__(self):
        self.container = []
        self.buffer = []
        
    def append(self, data_new):
        self.container.append(data_new)
        self.buffer.append(data_new)
    
    def get_buffer(self):
        data_buffer = self.buffer.copy()
        self.buffer = []
        length = len(self.container)
        return data_buffer,length
    


    



