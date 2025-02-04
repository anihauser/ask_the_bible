import json

# File paths
topics_txt_file = "data/nave/topics.txt"
txt_file = "data/nave/topicxref.txt"
json_file = "data/nave/verses.json"
esv_file = "data/nave/ESV.json"

# Mapping topic ID to topic name
mapping = {}
with open(topics_txt_file , 'r') as map_file:
    for line in map_file:
        id, topic_name,_ = line.strip().split('\t')
        mapping[int(id)] = topic_name  

# Define the field names for the JSON structure
fields = ["topic_key", "category_key", "subtopic_key",
 "book_key", "chapter_nbr", "verse_nbr", "verse_txt"]

# Book key - names linked to numbers
book_map = {
    1: "Genesis",
    2: "Exodus",
    3: "Leviticus",
    4: "Numbers",
    5: "Deuteronomy",
    6: "Joshua",
    7: "Judges",
    8: "Ruth",
    9: "1 Samuel",
    10: "2 Samuel",
    11: "1 Kings",
    12: "2 Kings",
    13: "1 Chronicles",
    14: "2 Chronicles",
    15: "Ezra",
    16: "Nehemiah",
    17: "Esther",
    18: "Job",
    19: "Psalm",
    20: "Proverbs",
    21: "Ecclesiastes",
    22: "Song of Solomon",
    23: "Isaiah",
    24: "Jeremiah",
    25: "Lamentations",
    26: "Ezekiel",
    27: "Daniel",
    28: "Hosea",
    29: "Joel",
    30: "Amos",
    31: "Obadiah",
    32: "Jonah",
    33: "Micah",
    34: "Nahum",
    35: "Habakkuk",
    36: "Zephaniah",
    37: "Haggai",
    38: "Zechariah",
    39: "Malachi",
    40: "Matthew",
    41: "Mark",
    42: "Luke",
    43: "John",
    44: "Acts",
    45: "Romans",
    46: "1 Corinthians",
    47: "2 Corinthians",
    48: "Galatians",
    49: "Ephesians",
    50: "Philippians",
    51: "Colossians",
    52: "1 Thessalonians",
    53: "2 Thessalonians",
    54: "1 Timothy",
    55: "2 Timothy",
    56: "Titus",
    57: "Philemon",
    58: "Hebrews",
    59: "James",
    60: "1 Peter",
    61: "2 Peter",
    62: "1 John",
    63: "2 John",
    64: "3 John",
    65: "Jude",
    66: "Revelation",
    67: "Tobit",
    68: "Judith",
    69: "Wisdom",
    70: "Ecclesiasticus",
    71: "Baruch",
    72: "1 Maccabees",
    73: "2 Maccabees"
}

# Read ESV file
with open(esv_file, "r") as esv_file:
    esv_data = json.load(esv_file)

# Read and process the text file
data = []
with open(txt_file, 'r') as file:
    for line in file:
        values = line.strip().split('\t')

        # find book name
        book_name = book_map.get(int(values[3]))
        
        # get verse text
        try:
            verse_text = esv_data[book_name][values[4]][values[5]]
        except KeyError:
            verse_text = "Verse not found"
        
        #create entry
        entry = {
            "topic_key": mapping[int(values[0])],
            "category_key": int(values[1]),
            "subtopic_key": int(values[2]),
            "book_key": book_name,
            "chapter_nbr": int(values[4]), 
            "verse_nbr": int(values[5]),
            "verse_txt": verse_text
        }
        data.append(entry)

# Write to JSON file
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Conversion completed. JSON saved to {json_file}")

