# Library Management System

# Sample data (can be modified or extended)
borrow_records = {
    "member1": ["Book A", "Book B"],
    "member2": [],
    "member3": ["Book A", "Book C", "Book B"],
    "member4": ["Book C"],
    "member5": ["Book A"]
}

# Step 1: Compute average number of books borrowed by all members
def compute_average_borrowed(records):
    total_books = sum(len(books) for books in records.values())
    total_members = len(records)
    average = total_books / total_members if total_members > 0 else 0
    return average

# Step 2: Find the book with the highest and lowest number of borrowings
def find_max_min_borrowed_books(records):
    book_count = {}
    for books in records.values():
        for book in books:
            book_count[book] = book_count.get(book, 0) + 1

    if not book_count:
        return None, None

    max_borrowed = max(book_count.items(), key=lambda x: x[1])
    min_borrowed = min(book_count.items(), key=lambda x: x[1])
    return max_borrowed, min_borrowed

# Step 3: Count members who have not borrowed any books
def count_zero_borrow_members(records):
    return sum(1 for books in records.values() if len(books) == 0)

# Step 4: Display the most frequently borrowed book (mode)
def find_most_frequent_book(records):
    book_count = {}
    for books in records.values():
        for book in books:
            book_count[book] = book_count.get(book, 0) + 1

    if not book_count:
        return None

    max_borrow = max(book_count.values())
    most_frequent_books = [book for book, count in book_count.items() if count == max_borrow]
    return most_frequent_books

# --------------------------
# Main Execution & Display
# --------------------------
print("Library Borrowing Management System\n")

# 1. Average
avg = compute_average_borrowed(borrow_records)
print(f"Average books borrowed per member: {avg:.2f}")

# 2. Highest and Lowest Borrowed Books
max_book, min_book = find_max_min_borrowed_books(borrow_records)
if max_book and min_book:
    print(f"Most borrowed book: {max_book[0]} ({max_book[1]} times)")
    print(f"Least borrowed book: {min_book[0]} ({min_book[1]} times)")
else:
    print("No books have been borrowed.")

# 3. Count members with 0 borrowings
zero_borrow_count = count_zero_borrow_members(borrow_records)
print(f"Number of members who borrowed 0 books: {zero_borrow_count}")

# 4. Most Frequently Borrowed Book (Mode)
mode_books = find_most_frequent_book(borrow_records)
if mode_books:
    print("Most frequently borrowed book(s):", ", ".join(mode_books))
else:
    print("No books found to determine mode.")
