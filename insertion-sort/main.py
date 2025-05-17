def insertion_sort(sample):
    """
    Use Insertion Sort algorithm and sort in
    monotonically decreasing order.

    :param sample List of numbers.

    Returns: None
    """

    # Iterate over a list of numbers
    for number in range(1, len(sample)):

        # Get the current item
        element = sample[number]

        # Get the previous item
        position = number - 1

        # Compare between the two and shift small value
        # to the right
        while position >= 0 and sample[position] < element:
            sample[position + 1] = sample[position]

            # Move to the next item
            position = position - 1

        sample[position + 1] = element

    # Return the sorted list.
    return sample


def main():
    sample1 = [15, 43, 2, 95, 37, 8, 49]
    print(f"Sample1: {sample1}")
    print(f"Result: {insertion_sort(sample1)}\n")

    sample2 = [99, 0, 75, 98, 67, 6, 88]
    print("Sample2:", sample2)
    print(f"Result: {insertion_sort(sample2)}\n")

    sample3 = [87, -1, 28, 5, 5, 67, 39]
    print("Sample3:", sample3)
    print(f"Result: {insertion_sort(sample3)}\n")


if __name__ == "__main__":
    main()
