import pandas as pd

# Load the dataset
data = pd.read_csv("day_25/TheSquirrelCensusDataAnalysis/Squirrel_Data.csv")

# Count the number of cinnamon and black squirrels
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

# Create a DataFrame with the counts
squirrel_counts = pd.DataFrame({
    "Fur Color": ["Cinnamon", "Black"],
    "Count": [cinnamon_count, black_count]
})

print(squirrel_counts)
print("--------------------------------")

fur_color_counts = data["Primary Fur Color"].value_counts()
print(fur_color_counts)
print("--------------------------------")

fur_color_df = pd.DataFrame(fur_color_counts)
print(fur_color_df)

# Save the DataFrame to a CSV file
# squirrel_counts.to_csv("day_25/TheSquirrelCensusDataAnalysis/squirrel_counts.csv", index=False)
