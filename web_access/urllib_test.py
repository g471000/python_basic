import urllib.error
import urllib.request

handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in handle:
    decoded_line = line.decode().strip()
    print(decoded_line)
    words = decoded_line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print()
print(counts)
