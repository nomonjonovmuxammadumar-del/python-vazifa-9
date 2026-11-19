import matplotlib.pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog'", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

plt.bar(mahsulotlar, sotuv, color="teal")
plt.title("Haftalik do'kon savdosi")
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotilgan mahsulotlar soni")

eng_kop = mahsulotlar[sotuv.index(max(sotuv))]
eng_kam = mahsulotlar[sotuv.index(min(sotuv))]

print(f"Eng ko'p sotilgan mahsulot: {eng_kop}")
print(f"Eng kam sotilgan mahsulot: {eng_kam}")

plt.show()
