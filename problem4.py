# =============================================================================
# csc349-hw1 - Problem 4
#
#   Suppose that you are given a sorted list of distinct integers {a1, a2, . . . an}.
#   Design and analyze a divide-and-conquer algorithm that determines whether
#   there exists an index i such that ai = i.
#
#   For example, in {-10, -4, 3, 41}, a3 = 3,
#            and in {4, 7, 19, 20}    there is no such i.
#
#   Input:  An array of distinct integers, sorted in increasing order.
#
#   Goal:   Determine if there exists an index i such that ai = i
#            (using a divide and conquer strategy).
#
#   NOTE: Input files should be text files containing comma-separated
#           integer values.  Spaces allowed, but not line breaks.
#           ( ex. -1, -1, 2, 2, 4, 5, 5 )
#
#   Andrew Weisman (aweisman@calpoly.edu)
#   HW 1, Problem 4 - CSC 349 (Spring 2019)
# =============================================================================

import sys


def problem4(arr, left, right):
    # NOTE: REMEMBER ARRAY IS INDEXED AT 1.
    #       Comparisons involving mid as an index
    #        are incremented by one before check.

    # Check array bounds
    if (right < left):
        return None

    # Get middle term.
    # Using (l + (r-l) // 2) form to avoid possible overflow
    mid = left + (right - left) // 2

    if (arr[mid] == mid + 1):
        # Found matching index
        return mid + 1
    elif (arr[mid] < mid + 1):
        # Value at index is less than the index, eliminate left of mid (inclusive)
        return problem4(arr, mid + 1, right)
    else:
        # Value at index is greater than the index, eliminate right of mid (inclusive)
        return problem4(arr, left, mid - 1)


def main(argv):
    if len(argv) < 2:
        print("Usage: ./problem4 <path to input file>")
    else:
        array = []
        try:
            # Read input file into an array to send to problem4()
            with open(argv[1], "r") as inFile:
                for line in inFile:
                    for x in line.strip().split(","):
                        array.append(int(x))
        except FileNotFoundError:
            if argv[1] == '':
                print("Usage: ./problem4 <path to input file>")
            else:
                print(f"No such file or directory '{argv[1]}'")
            return 0
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return 0

        # print(array)

        # Print result of algorithm to stdout
        print(problem4(array, 0, len(array) - 1))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
