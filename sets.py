# The following list of cities has some duplicate data
cities = ["Los Angeles", "Tokyo", "Florence", "Boulder", "Los Angeles", "Oslo", "Tokyo", "Santiago", "Kyoto", "San Francisco", "Tokyo", "Shanghai", "Florence"]
# To count unique cities
print(len(set(cities)))

#convert from list -> set -> list to get a list of uniques
print(list(set(cities)))


# Suppose I teach two classes:
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# To generate a set with all my unique students
math_students | biology_students

# To generate a set with students who are in both courses
math_students & biology_students
