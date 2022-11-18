from csv import reader, writer
# using nested with statements
with open("fighters.csv") as file:
	csv_reader = reader(file)
	with open("screaming_fighters.csv", "w") as file:
		csv_writer = writer(file)
		for fighter in csv_reader:
			csv_writer.writerow([s.upper() for s in fighter])


# Other approach, with only 1 file open at a time
# with open("fighters.csv") as file:
# 	csv_reader = reader(file)
# 	fighters = [[s.upper() for s in row] for row in csv_reader]
	
# with open("screaming_fighters.csv", "w") as file:
# 	csv_writer = writer(file)
# 	for fighter in fighters:
# 		csv_writer.writerow(fighter)