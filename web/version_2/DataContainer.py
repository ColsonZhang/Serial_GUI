import csv

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
    
    def clear_data(self):
        self.container = []
        self.buffer = []
        self.length = 0

    def save_data(self,file_name):
        with open(file_name, 'w+', newline='', encoding="utf-8") as csvfile:
            writer  = csv.writer(csvfile)
            for row in self.container:
                writer.writerow([row])

    def load_data(self,file_name):
        self.clear_data()
        with open(file_name, 'r', newline='', encoding="utf-8") as csvfile:    
            reader = csv.reader(csvfile)
            for row in reader:
                self.append(int(row[0]))
                # need to be improve !!!!


    



