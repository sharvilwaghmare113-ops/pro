# E-commerce Customer Account ID Search Program

# Sample list of customer account IDs
customer_ids = [1034, 2051, 1022, 1505, 3002, 2501, 1890, 1200]

# -------- Linear Search --------
def linear_search(ids, target):
    for i in range(len(ids)):
        if ids[i] == target:
            return i
    return -1

# -------- Binary Search --------
def binary_search(ids, target):
    left = 0
    right = len(ids) - 1
    while left <= right:
        mid = (left + right) // 2
        if ids[mid] == target:
            return mid
        elif ids[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# -------- Main Program --------
print("Customer Account ID Search System")
print("List of Customer IDs:", customer_ids)

# Sort the list once for binary search
sorted_ids = sorted(customer_ids)
print("Sorted Customer IDs for Binary Search:", sorted_ids)

while True:
    # Get ID to search from user
    user_input = input("\nEnter Customer ID to search (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break

    try:
        search_id = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a numeric ID.")
        continue

    # Linear Search
    index_linear = linear_search(customer_ids, search_id)
    if index_linear != -1:
        print(f"Linear Search: Customer ID {search_id} found at index {index_linear} in original list.")
    else:
        print(f"Linear Search: Customer ID {search_id} not found in original list.")

    # Binary Search on sorted list
    index_binary = binary_search(sorted_ids, search_id)
    if index_binary != -1:
        # Find original index for the binary search result
        original_index = customer_ids.index(search_id)
        print(f"Binary Search: Customer ID {search_id} found at index {index_binary} in sorted list, "
              f"which corresponds to index {original_index} in original list.")
    else:
        print(f"Binary Search: Customer ID {search_id} not found in sorted list.")
