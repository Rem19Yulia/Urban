def all_variants(text):
    length = len(text)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]

text = "abc"
generator = all_variants(text)

print("Подпоследовательности:") 
for variant in generator:
    print(variant)