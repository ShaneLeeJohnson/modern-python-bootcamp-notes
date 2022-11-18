users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# print(sorted(users, key=lambda user: user["username"]))
print(sorted(users, key=lambda user: len(user["tweets"])))
