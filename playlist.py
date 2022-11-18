playlist = {
	"Title": "Spongebob Jams",
	"Author": "Shane Johnson",
	"Songs": [
	{"title": "Goofy Goober", "Artist": ["Spongebob"], "Album": "The Spongebob Movie", "Duration": 3.0}, 
	{"title": "Campfire Song Song", "Artist": ["Spongebob"], "Album": "Spongebob Squarepants", "Duration": 2.5}
	]
}

total_length = 0
for song in playlist["Songs"]:
	total_length += song["Duration"]

print(total_length)