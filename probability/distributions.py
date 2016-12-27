import abc
from math import pi, e, sqrt
from statistics import stdev, pstdev
from scipy import stats
import numpy as np

def mean(list_object):
    return float(sum(list_object)/len(list_object))

def standard_deviation(list_object, m=None):
    if not m:
        m = mean(list_object)
    return (sum(map(lambda x: (x - m)**2, list_object))/len(list_object))**.5

class Distribution(object):

    def __init__(self):
        __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def get_distribution(self):
        raise NotImplementedError

class GaussianDistribution(Distribution):

    @staticmethod
    def get_distribution(list_object):
        mu = mean(list_object)
        sig = standard_deviation(list_object)
        #v = float(std**2)
        return (1/sqrt(2*pi*sig**2) * (e**\
            (-(x-mu)**2/(2*sig**2)))\
                for x in list_object)

#http://stackoverflow.com/questions/14873203/plotting-of-1-dimensional-gaussian-distribution-function
def gaussian(x, mu, sig):
    return 1./(sqrt(2.*pi)*sig)*np.exp(-np.power((x - mu)/sig, 2.)/2)

l = [1,2,3,3,3,3,4,5]
print(next(GaussianDistribution.get_distribution(l)))
print(stats.norm(mean(l), pstdev(l)).pdf(l[0]))
print(gaussian(l[0], mean(l), pstdev(l)))




