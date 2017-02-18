class AnnealingCounter():

    def __init__(self, alpha=0.9):
        self.alpha = alpha  # rate of decay
        self.last_t = .0
        self.heat = .0

    def increment(self, t=None, amount=1.0):
        """
        t is a floating point temporal index.
        If t is not provided, the value of last_t is used
        """
        if t is None: t = self.last_t
        elapsed = t - self.last_t
        if elapsed < .0 :
            raise ValueError('Cannot increment the counter in the past, i.e. before the last increment')
        self.heat = amount + self.heat * (self.alpha ** elapsed)
        self.last_t = t

    def get_value(self, t=None):
        """
        t is a floating point temporal index.
        If t is not provided, the value of last_t is used
        """
        if t is None: t = self.last_t
        elapsed = t - self.last_t
        if elapsed < .0 :
            raise ValueError('Cannot increment the counter in the past, i.e. before the last increment')
        return self.heat * (self.alpha ** elapsed)

    def __str__(self):
        return str('Counter has value {} at time {}'.format(self.heat, self.last_t))

    def __repr__(self):
        return self.__str__()
