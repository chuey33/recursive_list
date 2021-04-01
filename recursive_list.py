def list_max(list_numbers):
    """Returns the maximum number in a list"""
    if len(list_numbers) == 1:
        return list_numbers[0]
    # this is the base case
    if list_max(list_numbers[1:]) < list_numbers[0]:
        return list_numbers[0]
    else:
        return list_max(list_numbers[1:])
    # returns max number in the list using recursion

# Testing code
# def main():
#     list_numbers = [2, 3, 4, 5, 6, 7, 7, 2, 2, 3]
#     print(list_max(list_numbers))
#
# if __name__ == "__main__":
#     main()