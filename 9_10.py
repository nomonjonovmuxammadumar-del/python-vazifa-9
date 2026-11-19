import matplotlib.pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

plt.bar(ismlar, ballar, color="steelblue")
plt.title("O'quvchilar natijalari tahlili")
plt.xlabel("O'quvchilar")
plt.ylabel("Ballar")
plt.grid(True)
plt.savefig("oquvchilar_natijasi.png")

eng_yuqori = max(ballar)
eng_past = min(ballar)
ortacha = sum(ballar) / len(ballar)

print(f"Eng yuqori ball: {eng_yuqori} ({ismlar[ballar.index(eng_yuqori)]})")
print(f"Eng past ball: {eng_past} ({ismlar[ballar.index(eng_past)]})")
print(f"O'rtacha ball: {ortacha:.1f}")

print("1. Aziza 95 ball bilan sinfda eng yuqori natijani ko'rsatdi.")
print("2. O'quvchilarning umumiy o'rtacha bali 81.8 ballni tashkil qildi.")

plt.show()
