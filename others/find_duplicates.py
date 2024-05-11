def find_duplicates(num1, num2, num3):
    # Merge three arrays into a set
    all_elements = set(num1) | set(num2) | set(num3)
    
    # Initialize the result list
    result = []
    
    # Iterate over all elements
    for element in all_elements:
        # Record the count of occurrences of the element in arrays
        count = 0
        # Check the occurrence of the element in each array
        if element in num1:
            count += 1
        if element in num2:
            count += 1
        if element in num3:
            count += 1
        # If the element occurs in at least two arrays, add it to the result list
        if count >= 2:
            result.append(element)
            
    return result

if __name__ == '__main__':
    # Example
    num1 = [1, 1, 3, 2]
    num2 = [3, 2]
    num3 = [3]
    result = find_duplicates(num1, num2, num3)
    print("Elements occurring in at least two arrays:", result)
