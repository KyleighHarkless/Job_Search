class Job_Class:
    def __init__(self, title, company, location, date_posted):
        self.title = title
        self.company = company
        self.location = location
        self.date_posted = date_posted

    def __repr__(self):
        return f"{self.title} \nCompany: {self.company} \nLocation: {self.location}\nDate Posted: {self.date_posted} \n"