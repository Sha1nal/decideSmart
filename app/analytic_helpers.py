import pandas as pd

class Analytics:


    def __init__(self, decision_set_p):
        '''This class must be instantiated with a Decision Set Object'''
        self.decision_set = decision_set_p
        self.list_of_data = [u.__dict__ for u in self.decision_set]
        self.df = None
        self.pandas_init()
        print(self.df.info())
        print(self.df.shape)
        self.text = self.df['what']
        print(self.text)
        print(self.df.head())
        
        print(self.df.describe())

    def pandas_init(self):
        self.df = pd.DataFrame(self.list_of_data)
        self.df = self.df.drop('_sa_instance_state', axis=1)


        

