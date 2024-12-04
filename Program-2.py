def generate_series(x):
    if x <= 0:
        return "Input must be a positive integer."
    series = [2 * i - 1 for i in range(1, x + 1)]
    return ', '.join(map(str, series))


if __name__ == "__main__":
    x = int(input("Enter the number of terms: "))
    result = generate_series(x)
    print(result)