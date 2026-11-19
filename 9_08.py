import matplotlib.pyplot as plt

soat = [1, 2, 3, 4, 5, 6, 7]
ball = [40, 48, 55, 65, 72, 85, 90]

plt.scatter(soat, ball, color="coral")
plt.title("O'qish vaqti va test ballari")
plt.xlabel("Tayyorlanish vaqti (soat)")
plt.ylabel("Test bali")
plt.grid(True)

print("Tayyorlanish vaqti ko'paygani sari test ballari ham oshib borgan, ya'ni ijobiy to'g'ri mutanosib bog'liqlik mavjud.")

plt.show()
