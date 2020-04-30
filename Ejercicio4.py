import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '38.72', '38.73', '38.76', '38.78','38.83','38.90','39.92','38.89','38.88'
sizes = [5.56,5.56,11.11,5.56,5.56,22.22,5.56,22.22,16.67]
explode = (0, 0, 0, 0,0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%0.2f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('FRECUENCIA')

plt.show()