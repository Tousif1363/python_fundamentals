from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    print(type(story))
    for line in story:
        print(type(line))
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

print(story_words)
