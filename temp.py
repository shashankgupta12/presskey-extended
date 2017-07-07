import numpy as np 
import pylab 
import scipy.stats as stats

# measurements = np.random.normal(loc = 20, scale = 5, size=100)
measurements = [127322, 127246, 121472, 152504, 132350, 117370, 162605, 110489, 120283, 154608, 122392, 122496, 77102, 106105, 109993, 107505, 147369, 121577, 82400, 131979, 116903, 133035, 139360, 127468, 117263, 117332, 107248, 112395, 111723, 172922, 136790, 163201, 102078, 132502, 87203, 102390, 117495, 112304]
stats.probplot(measurements, dist="norm", plot=pylab)
pylab.show()