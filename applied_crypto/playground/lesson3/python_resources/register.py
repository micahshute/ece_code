class Register:

    def __init__(self, state):
        self.state = state

    def shift(self):
        return self.state.pop(), lambda x: self.state.insert(0, x)

    