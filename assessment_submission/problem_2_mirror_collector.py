def mirror_collector(words):
    return [word for word in words if word == word[::-1]]

# Example Tests
print(mirror_collector(["level", "code", "radar"]))  # ['level', 'radar']
print(mirror_collector(["soul", "mirror", "eye"]))   # ['eye']
print(mirror_collector(["openai", "eidon"]))         # []
