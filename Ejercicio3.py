import numpy as np
import matplotlib.pyplot as plt

x = ["5/1/2016","6/1/2016","7/1/2016","8/1/2016","9/1/2016"]
y1 = [32, 32, 28, 12, 15]
y2 = [12, 12, 12, 21, 28]
y3 = [16, 18, 20, 16, 17]

y = np.vstack([y1, y2, y3])

labels = ["Serie 1", "Serie 2", "Serie 3"]

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
ax.stackplot(x, y1, y2, y3, labels=labels)


fig.legend([y1,y2,y3],    
           labels=labels,   
           loc="center right", 
           borderaxespad=1,    
           title="Series" 
           )

plt.show()