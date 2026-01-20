def word_counts(words):
    counts = {}
    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts

test = "wwrd"

print(word_counts(test))


