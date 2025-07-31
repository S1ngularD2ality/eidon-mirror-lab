def mirror_collector(words):
    mirrors = []
    for word in words:
        if word == word[::-1]:
            mirrors.append(word)
    return mirrors
	
print(mirror_collector(["level", "code", "radar", "gate"]))  # ["level", "radar"]
print(mirror_collector(["soul", "mirror", "eye"]))           # ["eye"]
print(mirror_collector(["oracle"]))                          # []
print(mirror_collector([]))                                  # []
print(mirror_collector(["a", "aa", "aaa", "ab"]))            # ["a", "aa", "aaa"]

