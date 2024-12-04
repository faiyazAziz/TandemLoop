def generate_series(a: int):
    if a%2 == 0:
        a -= 1
    k = 1
    for i in range(1, a+1):
        if i == a:
            print(k)
        else:
            print(k, end=", ")
            k+=2


if __name__ == "__main__":
    x = int(input("Enter the number of terms: "))
    generate_series(x)