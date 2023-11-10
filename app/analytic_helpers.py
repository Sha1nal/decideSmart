from datetime import datetime
import pandas as pd

class Analytics:


    def __init__(self, decision_set_p):
        '''This class must be instantiated with a Decision Set Object'''
        self.decision_set = decision_set_p
        self.list_of_data = [u.__dict__ for u in self.decision_set]
        self.df = pd.DataFrame(self.list_of_data)
        self.results = {}
        self.pandas_init()


    def pandas_init(self):
        self.df = self.df.drop('_sa_instance_state', axis=1)
        self.results['total_decisions'] = self.df.shape[0]
        self.results['confidence_avg'] = self.confidence_avg()
        self.results['impulsive_avg'] = self.impulsive_avg()
        self.results['backup_avg'] = self.backup_avg()
        self.results['confidence_scale_avg'] = self.confidence_scale_avg()
        self.results['mean_logging_time'] = self.mean_logging_time()
        self.results['confident_decision_day'], self.results['num_confident_day_count'] = self.confident_days()
        print(self.confidence_avg())
        print(self.impulsive_avg())
        print(self.backup_avg())
        print(self.confidence_scale_avg())
        print(self.mean_logging_time())
        print(self.results['confident_decision_day'])
        print(self.results['num_confident_day_count'])


    def confidence_avg(self):
        confident_avg = self.df['confident'].value_counts()['yes']/self.df.shape[0]
        return round(confident_avg*100,2)
    

    def confidence_scale_avg(self):
        return round(self.df['confidence_scale'].mean(),2)
    

    def impulsive_avg(self):
        impulsive_avg = self.df['impulsive'].value_counts()['yes']/self.df.shape[0]
        return round(impulsive_avg*100,2)
    

    def backup_avg(self):
        backup_avg = self.df['backup'].value_counts()['yes']/self.df.shape[0]
        return round(backup_avg*100,2)
    

    def mean_logging_time(self):
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        self.df['when'] = pd.to_datetime(self.df['when'])
        self.df['difference'] = self.df['when'] - self.df['timestamp']
        return self.df['difference'].mean().days


    def confident_days(self):
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        self.df['timestamp_day'] = self.df['timestamp'].dt.day_name()
        filtered_df = self.df[self.df['confident'] == 'yes']
        day_counts = filtered_df['timestamp_day'].value_counts()
        most_confident_day = day_counts.index[0]
        times = day_counts.iloc[0]
        return most_confident_day, times
