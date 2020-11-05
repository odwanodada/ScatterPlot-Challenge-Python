import matplotlib.pyplot as plt #import for graphs


x_axis = (14.2, 16.5, 16.5, 15.3, 18.8, 22.5, 19.5) #Temperature
y_axis = (220.00, 330.00, 190.00, 340.00, 410.00, 445.00, 415.00)#Price in R

plt.scatter(x_axis, y_axis)
plt.title("Tempearature & Prices")
plt.ylabel("Price in (R)")#Label for prices
plt.xlabel("Temperature")#Label for temperature
plt.show()