import numpy as np
import matplotlib.pyplot as plt
import scipy
import functools
from pandas import Series,DataFrame

def displacement(amplitude,w,phi,t):
    return amplitude * np.sin(w * t + phi)

def velocity(amplitude,w,phi,t):
    return (amplitude * w) * np.cos(w * t + phi)


def wave_path(amplitude,w,phi,start_t,end_t,t_step = 0.01):
    disp = functools.partial(displacement,amplitude,w , phi)
    ll = np.linspace(start_t,end_t,1.0/t_step)
    t = Series(index = ll,data = [disp(t) for t in ll])
    return t

def wave_vels(amplitude,w,phi,start_t,end_t,t_step = 0.01):
    vels = functools.partial(velocity,amplitude,w , phi)
    ll = np.linspace(start_t,end_t,1.0/t_step)
    t = Series(index = ll, data = [vels(t) for t in ll])
    return t