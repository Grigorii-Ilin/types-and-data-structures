class Button:
    def __init__(self):
        self.is_enabled = False

    def change_state(self, new_state):
        #if new_state in {True, False}:#is True or new_state is False:
        self.is_enabled = new_state 

    def __str__(self):
        return str(self.is_enabled)
