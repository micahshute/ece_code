class AnalysisDecorator:

    def __init__(self, analyzer):
        self.analyzer = analyzer

    @property
    def ciphertext(self):
        return self.analyzer.ciphertext

    @ciphertext.setter
    def ciphertext(self, ciphertext):
        self.analyzer.ciphertext = ciphertext

    # A little bit of a factory mixed with a decorator
    # Don't know if that's cool or not...
    def new_analyzer(self, ciphertext):
        return type(self.analyzer)(ciphertext)

    def crack(self):
        raise Exception("Child classes of AnalysisDecorator must implement a #crack method")
