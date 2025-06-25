import datetime
import uuid

# --- Global Data Structures ---
books = {}  # Stores book details
sales = []     # Stores sales records
bookId = 1 # Global counter for incrementable book IDs

# --- Helper Functions (for input validation and common tasks) ---

def inputFloat(prompt):
    """
    Prompts the user for a positive floating-point number and validates the input.
    Handles exceptions for invalid input.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Input must be a positive number. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def inputInt(prompt):
    """
    Prompts the user for a positive integer and validates the input.
    Handles exceptions for invalid input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Input must be a positive integer. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def inputString(prompt):
    """
    Prompts the user for a non-empty string and validates the input.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("This field cannot be empty. Please try again.")

# --- 1. Inventory Management Functions ---

def createdBook():
    """
    Registers a new book in the inventory with an incrementable ID.
    Each book needs: title, author, category, price, quantity in stock.
    Validates inputs (numbers positive, formats correct, fields obligatory).
    """
    global bookId
    print("\n--- Register New Book ---")
    
    idBook = f"B{bookId:03d}" # e.g., B001, B002
    bookId += 1 # Increment for the next book

    print(f"Generated Book ID: {idBook}")

    title = inputString("Enter book title: ")
    author = inputString("Enter book author: ")
    category = inputString("Enter book category: ")
    price = inputFloat("Enter book price: ")
    quantity = inputInt("Enter quantity in stock: ")

    books[idBook] = {
        "title": title,
        "author": author,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    print(f"Book '{title}' registered successfully with ID: {idBook}!")

def getBook():
    """
    Consults and displays details of a book by its ID.
    """
    print("\n--- Consult Book by ID ---")
    idBook = inputString("Enter book ID to consult: ").upper() # Ensure input is uppercase for consistent lookup
    book = books.get(idBook) 
    if book:
        print(f"\nBook ID: {idBook}")
        for key, value in book.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")
    else:
        print(f"Book with ID '{idBook}' not found.")

def getBookByTitle():
    """
    Consults and displays details of books by their title.
    Allows partial matching and lists all found books.
    """
    print("\n--- Consult Book by Title ---")
    searchTitle = inputString("Enter book title (or part of it) to search: ").lower()
    foundBooks = []
    for idBook, details in books.items():
        if searchTitle in details['title'].lower():
            foundBooks.append((idBook, details))
    
    if foundBooks:
        print("\nMatching Books Found:")
        print(f"{'ID':<10} | {'Title':<30} | {'Author':<20} | {'Category':<15} | {'Price':<8} | {'Stock':<5}")
        print("-" * 100)
        for idBook, details in foundBooks:
            print(f"{idBook:<10} | {details['title']:<30} | {details['author']:<20} | {details['category']:<15} | {details['price']:<8.2f} | {details['quantity']:<5}")
    else:
        print(f"No books found with title matching '{searchTitle}'.")


def updatedBook():
    """
    Updates the details of an existing book.
    Allows updating title, author, category, price, and quantity.
    Validates inputs (numbers positive, formats correct, fields obligatory).
    Ensures the book to update exists.
    """
    print("\n--- Update Book ---")
    idBook = inputString("Enter book ID to update: ").upper() # Convert input to uppercase
    if idBook not in books:
        print(f"Error: Book with ID '{idBook}' not found. Cannot update.")
        return

    book = books[idBook]
    print(f"Updating book: {book['title']}")

    # Prompt for new values with current values as reference
    newTitle = inputString(f"Enter new title (current: {book['title']}): ")
    newAuthor = inputString(f"Enter new author (current: {book['author']}): ")
    newCategory = inputString(f"Enter new category (current: {book['category']}): ")
    newPrice = inputFloat(f"Enter new price (current: {book['price']}): ")
    newQuantity = inputInt(f"Enter new quantity in stock (current: {book['quantity']}): ")

    # Update book details
    book['title'] = newTitle
    book['author'] = newAuthor
    book['category'] = newCategory
    book['price'] = newPrice
    book['quantity'] = newQuantity

    print(f"Book '{idBook}' updated successfully!")

def deletedBook():
    """
    Deletes a book from the inventory by its ID.
    Ensures the book to delete exists.
    """
    print("\n--- Delete Book ---")
    idBook = inputString("Enter book ID to delete: ").upper() # Convert input to uppercase
    if idBook not in books:
        print(f"Error: Book with ID '{idBook}' not found. Cannot delete.")
        return

    confirm = inputString(f"Are you sure you want to delete '{books[idBook]['title']}' (yes/no)? ").lower()
    if confirm == 'yes':
        del books[idBook]
        print(f"Book with ID '{idBook}' deleted successfully.")
    else:
        print("Book deletion cancelled.")

def getAllBooks():
    """
    Lists all books currently in the inventory.
    """
    print("\n--- All Books in Inventory ---")
    if not books:
        print("No books in inventory.")
        return

    print(f"{'ID':<10} | {'Title':<30} | {'Author':<20} | {'Category':<15} | {'Price':<8} | {'Stock':<5}")
    print("-" * 100)
    for idBook, details in books.items():
        print(f"{idBook:<10} | {details['title']:<30} | {details['author']:<20} | {details['category']:<15} | {details['price']:<8.2f} | {details['quantity']:<5}")

# --- 2. Sales Registration and Consultation Functions ---

def generateInvoice(saleRecord):
    """
    Generates and prints a detailed invoice for a given sale record.
    """
    print("\n" + "="*50)
    print(f"{'SALES INVOICE':^50}")
    print("="*50)
    # Using a UUID for invoice ID for uniqueness, as sales records don't have unique IDs
    print(f"Invoice ID: {str(uuid.uuid4())[:8].upper()}") 
    print(f"Date: {saleRecord['date']}")
    print(f"Client Name: {saleRecord['client']}")
    print("-" * 50)
    print(f"Product: {saleRecord['productTitle']}")
    print(f"Product ID: {saleRecord['idBook']}")
    print(f"Quantity: {saleRecord['quantity']}")
    print(f"Unit Price: ${saleRecord['unitPrice']:.2f}")
    print(f"Discount: {saleRecord['discountPercentage']:.2f}%")
    print(f"Price per Unit (after discount): ${saleRecord['priceAfterDiscountPerUnit']:.2f}")
    print("-" * 50)
    print(f"Gross Total: ${saleRecord['salePriceGross']:.2f}")
    print(f"Net Total (after discount): ${saleRecord['SalePriceNet']:.2f}")
    print("="*50)
    print(f"{'THANK YOU FOR YOUR PURCHASE!':^50}")
    print("="*50 + "\n")

def createdSale():
    """
    Registers a new sale, validates stock, and updates inventory automatically.
    Allows applying a discount.
    Prints an invoice after successful registration.
    Includes validation for book existence and sufficient stock.
    Adds functionality to list or create a new book during sale registration.
    """
    print("\n--- Register New Sale ---")
    clientName = inputString("Enter client name: ")

    while True:
        idBookInput = inputString("Enter book ID sold (or type 'list' to see books, 'new' to register a new book): ").upper() # Convert to uppercase
        
        match idBookInput:
            case 'LIST':
                getAllBooks()
                continue
            case 'NEW':
                createdBook() # Call function to register a new book
                # After creating, prompt again to select the newly created or another existing book
                if not books: # If no books after registration, continue loop
                    continue
                continue # Continue the loop to allow selection of the newly added book
            case _: # Default case for an ID
                book = books.get(idBookInput)
                if not book:
                    print(f"Error: Book with ID '{idBookInput}' not found. Please try again.")
                    continue
                else:
                    idBook = idBookInput # Assign the validated ID
                    break # Book found, exit loop

    availableStock = book["quantity"]
    print(f"Available stock for '{book['title']}': {availableStock}")
    quantitySold = inputInt("Enter quantity to sell: ")

    if quantitySold > availableStock:
        print(f"Error: Insufficient stock. Only {availableStock} available for '{book['title']}'. Cannot complete sale.")
        return

    discountPercentage = inputFloat("Enter discount percentage (0-100, enter 0 if no discount): ")
    if not (0 <= discountPercentage <= 100):
        print("Warning: Discount percentage must be between 0 and 100. Setting discount to 0%.")
        discountPercentage = 0.0

    originalPrice = book["price"]
    discountAmount = originalPrice * (discountPercentage / 100)
    priceAfterDiscount = originalPrice - discountAmount

    book["quantity"] -= quantitySold
    books[idBook] = book # Ensure the global dictionary is updated

    saleEnd = {
        "client": clientName,
        "idBook": idBook,
        "productTitle": book["title"],
        "quantity": quantitySold,
        "unitPrice": originalPrice,
        "discountPercentage": discountPercentage,
        "priceAfterDiscountPerUnit": priceAfterDiscount,
        "salePriceGross": originalPrice * quantitySold,
        "SalePriceNet": priceAfterDiscount * quantitySold,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    sales.append(saleEnd)
    print(f"Sale of {quantitySold} units of '{book['title']}' to '{clientName}' registered successfully!")
    print(f"Remaining stock for '{book['title']}': {book['quantity']}")

    generateInvoice(saleEnd) # Generate and print invoice after successful sale

def getAllSales():
    """
    Displays all registered sales.
    """
    print("\n--- All Registered Sales ---")
    if not sales:
        print("No sales registered yet.")
        return

    print(f"{'Sale #':<8} | {'Date':<20} | {'Client':<20} | {'Product':<30} | {'Qty':<5} | {'Gross Total':<12} | {'Net Total':<10}")
    print("-" * 130)
    for i, sale in enumerate(sales):
        print(f"{i+1:<8} | {sale['date']:<20} | {sale['client']:<20} | {sale['productTitle']:<30} | {sale['quantity']:<5} | ${sale['salePriceGross']:<10.2f} | ${sale['SalePriceNet']:<8.2f}")

# --- 3. Reporting Module Functions ---

def getTopSoldBooks():
    """
    Shows the top 3 most sold books based on quantity sold.
    Uses efficient grouping and searching.
    """
    print("\n--- Top 3 Most Sold Books ---")
    if not sales:
        print("No sales data available to determine top books.")
        return

    bookSalesQuantity = {}
    for sale in sales:
        idBook = sale["idBook"]
        quantity = sale["quantity"]
        bookSalesQuantity[idBook] = bookSalesQuantity.get(idBook, 0) + quantity

    sortedBooks = sorted(bookSalesQuantity.items(), key=lambda item: item[1], reverse=True)

    print(f"{'Rank':<6} | {'Book ID':<10} | {'Title':<30} | {'Quantity Sold':<15}")
    print("-" * 70)
    for i, (idBook, quantity) in enumerate(sortedBooks[:3]):
        title = books[idBook]["title"] if idBook in books else "Unknown"
        print(f"{i+1:<6} | {idBook:<10} | {title:<30} | {quantity:<15}")

def getSalesAuthor():
    """
    Generates a report of total sales grouped by author.
    Calculates gross and net income (with and without discount) for each author.
    Uses efficient grouping and searching.
    """
    print("\n--- Sales Report by Author ---")
    if not sales:
        print("No sales data available to generate report.")
        return

    authorSales = {}
    for sale in sales:
        idBook = sale["idBook"]
        if idBook in books:
            author = books[idBook]["author"]
            quantity = sale["quantity"]
            grossSale = sale["salePriceGross"]
            netSale = sale["SalePriceNet"]

            if author not in authorSales:
                authorSales[author] = {"total_quantitySold": 0, "total_gross_income": 0.0, "total_net_income": 0.0}
            
            authorSales[author]["total_quantitySold"] += quantity
            authorSales[author]["total_gross_income"] += grossSale
            authorSales[author]["total_net_income"] += netSale
        else:
            print(f"Warning: Book ID '{idBook}' in sale record not found in current book inventory. Sales data for this book might be incomplete.")

    print(f"{'Author':<25} | {'Total Quantity Sold':<20} | {'Total Gross Income':<20} | {'Total Net Income':<20}")
    print("-" * 100)
    for author in sorted(authorSales.keys()): # Sort authors alphabetically
        data = authorSales[author]
        print(f"{author:<25} | {data['total_quantitySold']:<20} | ${data['total_gross_income']:<18.2f} | ${data['total_net_income']:<18.2f}")

# --- Initial Data Loading ---
def preloadBooks():
    """
    Loads at least 6 pre-loaded books into the system with incrementable IDs.
    Includes "A Game of Thrones".
    """
    global bookId # Use the global counter
    initialBooks = [
        {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "category": "Fantasy", "price": 25.00, "quantity": 100},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "category": "Romance", "price": 15.50, "quantity": 75},
        {"title": "1984", "author": "George Orwell", "category": "Dystopian", "price": 12.00, "quantity": 120},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction", "price": 18.75, "quantity": 90},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Classics", "price": 10.00, "quantity": 80},
        {"title": "A Game of Thrones", "author": "George R.R. Martin", "category": "Fantasy", "price": 30.00, "quantity": 150}
    ]
    for book_data in initialBooks:
        idBook = f"B{bookId:03d}"
        bookId += 1
        books[idBook] = book_data
        """print(f"Preloaded book '{book_data['title']}' with ID: {idBook}")"""
    """print("Initial books loaded successfully!")"""

# --- Main Menu and Program Execution ---

def mainMenu():
    """
    Displays the main interactive menu to the user.
    """
    print("\n--- Inventory and Sales Management System ---")
    print("1. Inventory Management")
    print("2. Sales Management")
    print("3. Reports")
    print("4. Exit")

def inventoryMenu():
    """
    Displays the inventory management menu.
    """
    print("\n--- Inventory Management ---")
    print("1. Register Book")
    print("2. Consult Book by ID")
    print("3. Consult Book by Title")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. List All Books")
    print("7. Back to Main Menu")

def salesMenu():
    """
    Displays the sales management menu.
    """
    print("\n--- Sales Management ---")
    print("1. Register Sale")
    print("2. Consult Sales")
    print("3. Back to Main Menu")

def reportMenu():
    """
    Displays the reports menu.
    """
    print("\n--- Reports ---")
    print("1. Top 3 Most Sold Books")
    print("2. Sales Report by Author")
    print("3. Back to Main Menu")

def deployedInventoryMenu():
    while True:
        inventoryMenu()
        choice = inputString("Enter your choice: ")
        
        match choice:
            case '1':
                createdBook()
            case '2':
                getBook()
            case '3':
                getBookByTitle()
            case '4':
                updatedBook()
            case '5':
                deletedBook()
            case '6':
                getAllBooks()
            case '7':
                break
            case _:
                print("Invalid choice. Please try again.")
        
        # Ask if user wants to perform another action in this menu
        if choice != '7': # Don't ask if they chose to go back
            repeat = inputString("Do you want to perform another action in Inventory Management (yes/no)? ").lower()
            if repeat != 'yes':
                break

def deployedSalesMenu():
    while True:
        salesMenu()
        choice = inputString("Enter your choice: ")
        
        match choice:
            case '1':
                createdSale()
            case '2':
                getAllSales()
            case '3':
                break
            case _:
                print("Invalid choice. Please try again.")

        # Ask if user wants to perform another action in this menu
        if choice != '3': # Don't ask if they chose to go back
            repeat = inputString("Do you want to perform another action in Sales Management (yes/no)? ").lower()
            if repeat != 'yes':
                break

def deployedReportMenu():
    while True:
        reportMenu()
        choice = inputString("Enter your choice: ")
        
        match choice:
            case '1':
                getTopSoldBooks()
            case '2':
                getSalesAuthor()
            case '3':
                break
            case _:
                print("Invalid choice. Please try again.")

        # Ask if user wants to perform another action in this menu
        if choice != '3': # Don't ask if they chose to go back
            repeat = inputString("Do you want to perform another action in Reports (yes/no)? ").lower()
            if repeat != 'yes':
                break

def main():
    """
    Main function to run the book and sales management system.
    Handles exceptions for unexpected errors to prevent abrupt termination.
    """
    preloadBooks() # Load initial data upon startup

    while True:
        try:
            mainMenu()
            choice = inputString("Enter your choice: ")
            
            match choice:
                case '1':
                    deployedInventoryMenu()
                case '2':
                    deployedSalesMenu()
                case '3':
                    deployedReportMenu()
                case '4':
                    print("Exiting the system. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again or restart the system.")
            # In a real application, you might log the error to a file

if __name__ == "__main__":
    main()