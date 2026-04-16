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
