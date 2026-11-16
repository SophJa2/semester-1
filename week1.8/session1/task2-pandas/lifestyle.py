import pandas

data = pandas.read_csv("lifestyle_data.csv")
print(data)
# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

#print(data.describe())
#print(data.info())
# Find the total number of students
print(f"Total num of students: {len(data)}")
# Find the mean average GPA of the students
#GPAs = data.groupby("GPA")

print(data["GPA"].mean())

# Find the standard deviation of how much sleep students get per day

print(data["Sleep_Hours_Per_Day"].std())

# Find the maximum amount of study hours per day
max = data["Study_Hours_Per_Day"].max()
print(max)

# Sort the students by social hours per day ascending (lowest -> highest)



# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
high_levels = data[data["Stress_Level"]== "High"]
print(high_levels)

#assessing rows - .iloc(num) means that it will go that position
#col just use the name of the column
