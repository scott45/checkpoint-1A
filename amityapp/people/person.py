__author__ = 'scotty'


# person class models the people in amity and is to be inherited by class staff and fellow

class Person(object):
    def __init__(self, f_name, l_name, person_label):
        self.f_name = f_name.strip().title()
        self.l_name = l_name.strip().title()
        self.person_label = person_label.strip().title()
        self.accommodate = 'N'
        self.all_names = self.f_name + ' ' + self.l_name
        self.qualifier = None

    def get_all_names(self):
        return self.f_name + ' ' + self.l_name

    def assign_qualifier(self, qualifier):
        self.qualifier = qualifier


class Staff(Person):
    # staff class method from the person class and overrides some properties using the super function call.

    def __init__(self, f_name, l_name):
        super(Staff, self).__init__(
            f_name, l_name, person_label="Staff"
        )


class Fellow(Person):
    # fellow class method from the person class and overrides some properties using the super function call

    def __init__(self, f_name, l_name):
        super(Fellow, self).__init__(
            f_name, l_name, person_label="Fellow"
        )
