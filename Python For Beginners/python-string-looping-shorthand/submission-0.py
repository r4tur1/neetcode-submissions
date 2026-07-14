def print_string_characters(word1: str, word2: str) -> None:
    length1=len(word1)
    for i in range(length1):
        print(word1[i])
    length2=len(word2)
    for j in range(length2):
        print(word2[j])
# do not modify below this line
print_string_characters("Hello, World!", "Good Job!")
