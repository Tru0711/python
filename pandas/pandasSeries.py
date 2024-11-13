import pandas as pd

# Create a Series of exam scores
scores = pd.Series([88, 92, 79, 93, 85, 91, 78, 84, 95, 89])

# Calculate and display statistics
mean_score = scores.mean()
max_score = scores.max()
min_score = scores.min()

print("Exam Scores:")
print(scores)
print("\nMean Score:", mean_score)
print("Highest Score:", max_score)
print("Lowest Score:", min_score)
