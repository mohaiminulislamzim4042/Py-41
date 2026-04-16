try:
    marks = []
    # Lec 11: File open kora
    with open("marks.txt", "r") as f:
        for line in f:
            # Lec 11: Data alada kora
            name, score = line.strip().split(",")
            score = int(score)
            print(f"Name: {name} -> Mark: {score}")
            marks.append(score)

    # Lec 8 & 9: Calculation
    if marks:
        print("-" * 20)
        print(f"Highest: {max(marks)}")
        print(f"Lowest: {min(marks)}")
        print(f"Average: {sum(marks)/len(marks):.2f}")

# Lec 11: Error handling
except Exception:
    print("File-e somossya ba file pawa jayni!")

Rahim,82
Karim,75
Manik,88
Jabbar,92
Sabbir,65
Nabil,70
Siam,85
Arif,78
Rafi,89
Arham,93

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# plt.plot(x, y)
# plt.title("Simple line chart")
# plt.xlabel("Days")
# plt.ylabel("Marks")
# plt.show()
# import matplotlib.pyplot as plt

# names = ['A', 'B', 'C']
# marks = [85, 92, 78]

# plt.bar(names, marks)
# plt.show()

import matplotlib.pyplot as plt

sizes = [40, 30, 30 ]
labels = ['Python', 'Java', 'C++']

plt.pie(sizes, labels=labels)
plt.show()
