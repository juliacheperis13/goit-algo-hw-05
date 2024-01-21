def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    iteration = 0

    if upper_bound < x:
        return (0, None)

    while low <= high:
        iteration = iteration + 1

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (iteration, mid)

    # якщо елемент не знайдений
    return (iteration, upper_bound)


if __name__ == '__main__':
    arr = [0.1, 0.5, 0.89, 1.1, 1.4, 2.5, 5.99, 9.234]
    
    x = 2

    (iteration, result) = binary_search(arr, x)

    if result is not None:
        print(f'The result is {result}, found in {iteration} iterations.')
    else:
        print("Element is not present in array.")
