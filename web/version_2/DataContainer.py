
class DataContainer():

    def __init__(self):
        self.container = []
        self.buffer = []
        self.length = 0
        
    def append(self, data_new):
        self.container.append(data_new)
        self.buffer.append(data_new)
        self.length += 1 
    
    def get_buffer(self):
        data_buffer = self.buffer.copy()
        self.buffer = []
        length = self.length
        return data_buffer,length
    


    



