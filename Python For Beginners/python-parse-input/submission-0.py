from typing import List

def read_integers() -> List[int]:
    string=input()
    SL=[int(x) for x in string.split(",")]
    return SL

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
