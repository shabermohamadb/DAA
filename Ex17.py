# String Matching using Brute Force
text = input("Text: ")
pattern = input("Pattern: ")

found = False
for i in range(len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
        print("Match at index:", i)
        found = True

if not found:
    print("Pattern not found")
