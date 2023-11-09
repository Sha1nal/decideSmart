class Analytics:


    def __init__(self, decision_set_p):
        '''This class must be instantiated with a Decision Set Object'''
        self.num_decisions = len(decision_set_p)
        self.decision_set = decision_set_p
        self.results = {}
        self.run_all_functions()


    def run_all_functions(self):
        self.results['confidence_avg'] = self.confidence_avg()
        self.results['confidence_scale_avg'] = self.confidence_scale_avg()
        self.results['impulsive_avg'] = self.impulsive_avg()
        self.results['backup_avg'] = self.backup_avg()
        self.mean_decision_log_time()


    def confidence_avg(self):
        count = 0
        for decision in self.decision_set:
            if decision.confident == "yes" or decision.confident == "Yes":
                count += 1
        return round(count/self.num_decisions*100,1)
    

    def confidence_scale_avg(self):
        total = 0
        for decision in self.decision_set:
            total += decision.confidence_scale
        return round(total/self.num_decisions,1)
    

    def impulsive_avg(self):
        count = 0
        for decision in self.decision_set:
            if decision.impulsive == "yes" or decision.confident == "Yes":
                count += 1
        return round(count/self.num_decisions*100,1)
    

    def backup_avg(self):
        count = 0
        for decision in self.decision_set:
            if decision.backup == "yes" or decision.confident == "Yes":
                count += 1
        return round(count/self.num_decisions*100,1)
    

    def mean_decision_log_time(self):
        total_days = 0
        for decision in self.decision_set:
            days_between = decision.timestamp.date() - decision.when
            print(days_between.days)
            total_days += abs(days_between.days)
        
        print(round(total_days/self.num_decisions,2))
        return round(total_days/self.num_decisions,2)

        

