import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import gif
import numpy as np


@gif.frame
def plot(size, x, y):
    fig = plt.figure(figsize=size)
    fig.patch.set_alpha(0)
    ax = plt.axes(projection=ccrs.Orthographic(central_longitude=x, central_latitude=y), frameon=False)

    ax.add_feature(cfeature.OCEAN, facecolor='white')
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.coastlines(linewidth=0.1)

    ax.gridlines(xlocs=xlocator, ylocs=ylocator, linestyle=':', linewidth=0.1, color='black')


##########
# size
gif.options.matplotlib["dpi"] = 300
figsize = (2, 2)
duration = 20

##########
# viewpoint
latitude = 36
long_delta = 1

##########
# grid
xlocator = mticker.FixedLocator(np.arange(-180, 180, 20))
ylocator = mticker.FixedLocator(np.arange(-80, 90, 20))     # from -80 to draw equator.

##########
# for Frame
frames = []
for longitude in reversed(range(0, 360, long_delta)):
    print(f'drawing around ({longitude}, {latitude}).')
    frames.append(plot(figsize, longitude, latitude))

##########
# Save "frames" to gif with a specified duration (milliseconds) between each frame
print(f'saving gif ...')
gif.save(frames, 'rotatingEarth.gif', duration=duration)
