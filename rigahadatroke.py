import random

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
sent = input().lower()

sent = random.choice(abc).join(sent[i:i + random.randint(1, 9)] for i in range(0, len(sent), random.randint(1, 9)))
print(sent)
