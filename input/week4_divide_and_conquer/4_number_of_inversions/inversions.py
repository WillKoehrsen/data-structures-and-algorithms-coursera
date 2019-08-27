# Uses python3
import sys


def merge_sort(arr):

    inversion_count = 0

    if len(arr) <= 1:
        return inversion_count

    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merging arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                inversion_count += 1
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Account for left over elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return inversion_count


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0

    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # write your code here
    return number_of_inversions


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(merge_sort(a))
