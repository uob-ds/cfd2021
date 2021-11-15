import matplotlib.pyplot as _plt
import numpy as _np

def interactive_plot(intercept, slope):
    
    _plt.figure(figsize = (8,8))
    x = _np.arange(-10, 11)
    y = slope * x + intercept
    _plt.plot(x, y, label = 'y = '+str(slope)+' * x + '+str(intercept))
    biggest_abs_x = _np.max(_np.abs([_np.min(x), _np.max(x)]))
    biggest_abs_y = _np.max(_np.abs([_np.min(y), _np.max(y)]))
    x_axis = _np.arange(-biggest_abs_x, biggest_abs_x+1)
    y_axis = _np.arange(-biggest_abs_y , biggest_abs_y +1)
    _plt.plot(x_axis, _np.repeat(0, len(x_axis)), color = 'black')
    _plt.plot(_np.repeat(0, len(y_axis)), y_axis, color = 'black')
    _plt.xlabel('X Axis')
    _plt.ylabel('Y Axis')
    _plt.plot(0,0, 'o', color = 'black', markersize = 8, label = 'The Origin (x = 0, y = 0)')
    
    max_x_axis = _np.max(x_axis)
    if max_x_axis == 0:
        max_x_axis = max_x_axis + 0.05
        
    max_y_axis = _np.max(y_axis)
    if max_y_axis == 0:
        max_y_axis = max_y_axis + 0.05
        
    _plt.xticks(_np.arange(_np.min(x_axis), _np.max(x_axis)+1, max_x_axis/10))
    _plt.yticks(_np.arange(_np.min(y_axis), _np.max(y_axis)+1, max_y_axis/10))
    _plt.legend()
    _plt.show()