def mirror_match(text):
    return text == text[::-1]

# Test
print(mirror_match("level"))    # True
print(mirror_match("mirror"))   # False
print(mirror_match("racecar"))  # True
