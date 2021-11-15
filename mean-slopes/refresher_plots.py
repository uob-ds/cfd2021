import matplotlib.pyplot as _plt
import numpy as _np

# a fucntion for a plot showing the origin, with arguments to adjust the display options as needed by this tutorial
def axes_func(fig_size_1, fig_size_2, low_ax_lim, up_ax_lim, new_fig = True, five_ticks = False, double_y = False,
             five_ticks_y = False):
  
    # create a new figure?
    if new_fig == True:
       _plt.figure(figsize = (fig_size_1,fig_size_2))
        
    # create points for the x axis
    x_axis =_np.arange(low_ax_lim, up_ax_lim)
    
    # should the y axis been double the length of the x axis?
    if double_y == False:
        y_axis = _np.arange(low_ax_lim, up_ax_lim)
    else:
        y_axis =_np.arange(low_ax_lim*2, up_ax_lim*2)
        
    # plot and label the axes and the origin
    _plt.plot(x_axis,_np.repeat(0, len(x_axis)), color = 'black')
    _plt.plot(_np.repeat(0, len(y_axis)), y_axis, color = 'black')
    _plt.xlabel('X Axis')
    _plt.ylabel('Y Axis')
    _plt.plot(0,0, 'o', color = 'black', markersize = 14, label = 'The Origin (x = 0, y = 0)')
    
    # set the limits of the axes
    _plt.xlim(min(x_axis), max(x_axis))
    _plt.ylim(min(y_axis), max(y_axis))
    
    # show the axes ticks in intervals of 5?
    if five_ticks == False:
       _plt.xticks(_np.arange(_np.min(x_axis),_np.max(x_axis)+1, 1))
       _plt.yticks(_np.arange(_np.min(y_axis),_np.max(y_axis)+1, 1))
    else:
       _plt.xticks(_np.arange(_np.min(x_axis),_np.max(x_axis)+1, 5))
       _plt.yticks(_np.arange(_np.min(y_axis),_np.max(y_axis)+1, 5))
    if five_ticks_y == True:
        _plt.yticks(_np.arange(_np.min(y_axis),_np.max(y_axis)+1, 5))
    
    # show the legend
    _plt.legend()

def interactive_plot(intercept, slope):
    
    # a function for the interactive plot at the end of the lines, slopes and
    # intercepts refresher
    
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