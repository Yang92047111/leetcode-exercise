class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_chain(arrays):
    # Sort the arrays in ascending order based on the first value
    arrays.sort(key = lambda x: x[0])

    # Initialize the head node of the chain
    head = Node(arrays[0])
    current = head
    
    # Iterate over the remaining arrays
    for array in arrays[1:]:
        # If the first value of the current array is greater than the second value of the last array in the chain,
        # then add it to the chain
        # p1[a, b] p2[c, d], when c > b
        if array[0] > current.data[1]:
            new_node = Node(array)
            current.next = new_node
            current = new_node
    
    return head

def chain_length(head):
    # Calculate the length of the chain
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

if __name__ == '__main__':
    # Example input
    input_arrays = [[1, 2], [7, 8], [3, 4]]
    result_head = create_chain(input_arrays)
    result_length = chain_length(result_head)

    print("The length of the chain satisfying the condition:", result_length)
