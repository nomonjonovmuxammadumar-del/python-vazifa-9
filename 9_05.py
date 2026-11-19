import matplotlib.pyplot as plt

mashgulot = [1, 2, 3, 4, 5, 6]
masofa = [2.0, 2.5, 2.3, 3.0, 3.5, 4.0]

plt.plot(mashgulot, masofa, color="green", marker="o", linewidth=2)
plt.title("Sport mashg'ulotlari natijalari")
plt.xlabel("Mashg'ulot")
plt.ylabel("Masofa (km)")
plt.grid(True, linestyle="--")

print("Sportchining bosib o'tgan masofasi mashg'ulotlar davomida umumiy hisobda o'sish tendensiyasini ko'rsatgan.")
print("Faqat uchinchi mashg'ulotda biroz pasayish kuzatilgan bo'lsa ham, keyin barqaror o'sib 4 kilometrga yetgan.")

plt.show()
