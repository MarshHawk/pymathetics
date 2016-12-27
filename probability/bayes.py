class BayesTheorem(object):

    def __init__(self, prior=None, likelihood=None, posterior =None,\
                 norm_const =None):
        self.prior = prior
        self.likelihood = likelihood
        self.posterior = posterior
        self.norm_const = norm_const

    def set_prior(self, prior):
        self.prior = prior

    def set_likelihood(self, likelihood):
        self.likelihood = likelihood

    def set_posterior(self, posterior):
        self.posterior = posterior

    def prior_times_like(self):
        return self.prior * self.likelihood

class ProbabilityMassFunction(object):

    def __init__(self):
        self.hypotheses = []

    def set_hypotheses(self, hypos):
        self.hypotheses = hypos

    def set_posteriors(self):
        total = sum(h.prior_times_like() for h in self.hypotheses)
        for h in self.hypotheses:
            h.set_posterior(h.prior_times_like() * (1.0/total))

class MmProblem(ProbabilityMassFunction):
    def __init__(self):
        super().__init__()
        self.dist94 = {'orange': 10, 'green': 10, 'red': 20, 'brown': 30, 'yellow': 20, 'tan': 10}
        self.dist96 = {'brown': 13, 'orange': 16, 'red': 13, 'green': 20, 'blue': 24, 'yellow': 14}

    def build_hypotheses(self):
        self.hypotheses.append(BayesTheorem(.5, self.dist94['yellow'] * self.dist96['green']))
        self.hypotheses.append(BayesTheorem(.5, self.dist96['yellow'] * self.dist94['green']))
        
#https://www.safaribooksonline.com/library/view/think-bayes/9781491945407/ch02.html from Think Bayes
b1 = BayesTheorem(0.5, 0.75)
b2 = BayesTheorem(0.5, 0.5)
p = ProbabilityMassFunction()
p.set_hypotheses([b1, b2])
p.set_posteriors()
print(b1.posterior)

montyb1 = BayesTheorem(1/3, 0)
montyb2 = BayesTheorem(1/3, 0.5)
montyb3 = BayesTheorem(1/3, 1)
p = ProbabilityMassFunction()
p.set_hypotheses([montyb1, montyb2, montyb3])
p.set_posteriors()
print(montyb1.posterior)
print(montyb2.posterior)
print(montyb3.posterior)

mm1 = MmProblem()
mm1.build_hypotheses()
mm1.set_posteriors()
print(mm1.hypotheses[0].posterior)



