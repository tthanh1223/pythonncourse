import urllib.request
import urllib.error

url = 'http://data.pr4e.org/intro-short.txt'

try:
    with urllib.request.urlopen(url) as fhand:
        for line in fhand:
            print(line.decode().strip())
except urllib.error.HTTPError as e:
    print(f"HTTP error: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"Error fetching URL: {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")
