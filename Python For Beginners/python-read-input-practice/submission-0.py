def add_two_numbers() -> int:
    user_input=input()
    S=user_input.split(",")
    for i in range(len(S)):
        S[i]=int(S[i])
    T=0
    for j in range(len(S)):
        T=T+S[j]
    return T





# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
