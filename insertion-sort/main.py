def insertion_sort(sample):

    for number in range(1, len(sample)):
        element = sample[number]
        position = number - 1
        while position >= 0 and sample[position] < element:
            sample[position + 1] = sample[position]
            position = position - 1

        sample[position + 1] = element
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
