import matplotlib.pyplot as plt

plt.figure(dpi=150)
plt.title('Pair of Lines', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
plt.style.use('ggplot')

x = [0, 1, 2, 3, 4, 5]
y = [i**2 for i in x]

plt.xlabel('X-axis', fontdict={'fontname':'Comic Sans MS', 'fontweight':'bold'})
plt.ylabel('Y-axis', fontdict={'fontname':'Comic Sans MS', 'fontweight':'bold'})

plt.plot(x[:4], y[:4], label='y = x**2', color='blue', marker='o')
plt.plot(x[3:], y[3:], label='infinity', color='red', marker='*', linestyle='--')

plt.legend()

plt.savefig('Practice.jpg', dpi=300)

plt.show()