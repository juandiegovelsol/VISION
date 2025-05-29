import matplotlib.pyplot as plt

años = [2009, 2010, 2011, 2012, 2013]
impuestos = [505, 500, 500, 510, 520]

plt.plot(años, impuestos, marker='D', linestyle='-', color='blue')

plt.title('City Taxes')
plt.xlabel('')
plt.ylabel('Tax Amount (dollars)')

plt.ylim(490, 525)

plt.grid(False)
plt.show()