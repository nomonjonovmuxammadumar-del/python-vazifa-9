import matplotlib.pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
qadamlar = [4800, 6200, 5900, 8100, 7500, 9300, 10400]

plt.plot(kunlar, qadamlar, marker="o", color="navy")
plt.title("Haftalik qadamlar soni")
plt.xlabel("Hafta kunlari")
plt.ylabel("Qadamlar soni")
plt.grid(True)
plt.savefig("natija.png")
plt.show()
