import matplotlib.pyplot as plt

testlar = [1, 2, 3, 4, 5]
guruh_a = [65, 70, 75, 80, 85]
guruh_b = [60, 72, 70, 88, 90]

plt.plot(testlar, guruh_a, color="blue", marker="o", label="A guruh")
plt.plot(testlar, guruh_b, color="red", marker="s", label="B guruh")
plt.title("Guruhlar natijalarini taqqoslash")
plt.xlabel("Testlar")
plt.ylabel("Ballar")
plt.legend()
plt.grid(True)

print("B guruhining natijasi yaxshiroq, chunki ularning o'rtacha bali yuqori va oxirgi bosqichda 90 ball to'plagan.")

plt.show()
