def count_multiples(numbers):
    result = {}
    for i in range(1, 10):
        result[i] = 0

    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1

    return result

# Example usage
if __name__ == "__main__":
    input_numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    output = count_multiples(input_numbers)
    print(output)
