class Job():

    def __init__(self, title="", priority=0):
        self.title = title
        self.priority = priority

    def get_priority(self):
        return self.priority

    def get_title(self):
        return self.title


class Job_Jar():

    def __init__(self):
        self.jobs = []

    def add_job(self, j):
        if type(j) == Job:
            self.jobs.append(j)

    def highest_piority(self):
        '''
        This function will return the job title with the highest priority
        '''

        max = 0
        for i in self.jobs:
            if (i.get_priority() > max):
                max = i.get_priority()

        for i in self.jobs:
            if i.get_priority() == max:
                return i.get_title()
