import webbrowser
import time
import random

while True:
    bob = random.choice(['google.com', 'www.youtube.com/watch?v=dQw4w9WgXcQ', 'homer.stuy.edu/~ali20/', 'weather.gov', 'theuselessweb.com/'])
    billyboi = 'http://{}'.format(bob)
    webbrowser.open(billyboi)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)
