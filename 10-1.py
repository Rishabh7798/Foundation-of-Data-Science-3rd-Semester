#Design a python program demonstrating data visualization using matplotlib module.

"""
#bar(x, height)
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

#make data:
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

#plot
fig, ax = plt.subplots()
ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
ax.set(xlim=(0,8), xticks=np.arange(1,8),
       ylim=(0,8), yticks=np.arange(1,8))
plt.show()
"""

"""
# scatter(x,y)
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

#make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))

#size and color
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

#plot
fig, ax = plt.subplots()
ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
ax.set(xlim=(0,8), xticks=np.arange(1,8),
       ylim=(0,8), yticks=np.arange(1,8))
plt.show()
"""

"""
# plot(x,y)
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

#make the data
x = np.linspace(0, 10, 100)
y = 4 + 2*np.sin(2*x)

#plot
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)
ax.set(xlim=(0,8), xticks=np.arange(1,8),
       ylim=(0,8), yticks=np.arange(1,8))
plt.show()
"""

"""
# histogram(x)
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

#make the data
np.random.seed(1)
x=4+np.random.normal(0, 1.5, 200)

#plot
fig, ax=plt.subplots()
ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")
ax.set(xlim=(0,8), xticks=np.arange(1,8),
       ylim=(0,56), yticks=np.arange(0, 56, 9))
plt.show()
"""

"""
# pie(x)
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

#make the data
x = [1, 2, 3, 4]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

#plot
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4,4),
       wedgeprops={"linewidth":1, "edgecolor":"white"}, frame=True)
ax.set(xlim=(0,8), xticks=np.arange(1,8),
       ylim=(0,8), yticks=np.arange(1,8))
plt.show()
"""















