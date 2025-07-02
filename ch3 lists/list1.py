notes = [12, 3, 14, 16, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

average = sum(notes) / len(notes)

above_average = [note for note in notes if note > average]

print(f"Average: {average:.2f}")
print("Grades above average:", above_average)
