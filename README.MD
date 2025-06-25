# Inventory and Sales Management System

This is a console-based Python application designed to manage book inventory, record sales, and generate various reports for a national bookstore. The system focuses on modular design, robust input validation, and clear exception handling.

## Features

* **Inventory Management:**

        Register new books with auto-incrementing IDs (e.g., B001, B002).

        Consult book details by ID or by title (supporting partial title search).

        Update existing book information (title, author, category, price, quantity).

        Delete books from the inventory with a confirmation step.

        List all books currently in stock.

* **Sales Management:**

        Register new sales, associating client, product, quantity, date, and discount.

        Automatically validate available stock and update it upon sale.

        Generate and print a detailed invoice for each completed sale.

        Option to list existing books or register a new book directly during sale registration.

        Consult all registered sales.

* **Reporting Module:**

        Display the top 3 most sold books by quantity.

        Generate a comprehensive sales report grouped by author, including total quantity sold, gross income, and net income (after discounts).

* **Advanced Validations:**

        Ensures positive numbers for price and quantity.

        Verifies non-empty strings for mandatory fields.

        Prevents sales with insufficient stock.

        Handles invalid discount percentages.

* **Modular Design:**

        Each core functionality is encapsulated in independent functions with parameters and return values.

        Utilizes match-case for cleaner menu navigation.

* **Exception Handling:**

        Robust try-except blocks to manage invalid inputs and prevent abrupt program termination.

* **Interactive Console Menu:**

        User-friendly text-based menu for easy navigation and interaction.

## Getting Started

### Prerequisites

    Python 3.10 or higher (for match-case statements).

### Installation

    Clone the repository (or copy the code):

    git clone git@github.com:jesuviloria/module.git
    cd module


    Alternatively, simply save the provided Python code into a .py file (e.g., bookstore_system.py).

### Running the Application

    Open your terminal or command prompt.

    Navigate to the directory where you saved the bookstore_system.py file.

    Run the script:

    python bookstore_system.py


The system will start with 6 pre-loaded books and present the main menu.

## How to Use

The system operates through an interactive console menu. Follow the prompts to perform various actions.

### Main Menu Options:

    1. Inventory Management: Access functions to add, view, update, and delete books.

    2. Sales Management: Register new sales and view all past sales.

    3. Reports: Generate analytical reports on sales and product performance.

    4. Exit: Terminate the program.

### Example Flow: Registering a Sale

    From the Main Menu, enter 2 for Sales Management.

    From the Sales Management menu, enter 1 to Register Sale.

    Enter the Client Name.

    When prompted for book ID, you can:

        Enter an existing book ID (e.g., B001).

        Type list to see all available books and their IDs.

        Type new to register a new book on the fly before making the sale.

    Enter quantity to sell and discount percentage.

    Upon successful registration, a detailed SALES INVOICE will be printed to the console.

### Code Structure

* books: A global dictionary to store book details, keyed by idBook.

* sales: A global list to store sale records, where each record is a dictionary.

* bookId: A global integer counter for generating sequential book IDs.

* Helper Functions (inputFloat, inputInt, inputString): Handle user input and validation.

* Inventory Management Functions (createdBook, getBook, getBookByTitle, updatedBook, deletedBook, getAllBooks): Encapsulate all inventory-related operations.

* Sales Management Functions (generateInvoice, createdSale, getAllSales): Handle sales registration, invoice generation, and sales lookup.

* Reporting Module Functions (getTopSoldBooks, getSalesAuthor): Provide analytical insights into sales data.

* preloadBooks(): Initializes the system with a set of predefined books.

* Menu Functions (mainMenu, inventoryMenu, salesMenu, reportMenu): Display the interactive menu options.

* Deployed Menu Functions (deployedInventoryMenu, deployedSalesMenu, deployedReportMenu): Manage the flow within each submenu, including asking if the user wants to perform another action.

* main(): The entry point of the program, orchestrating the main application loop and handling top-level exceptions.

### Future Enhancements

* **Data Persistence:** Implement saving and loading data to/from a file (e.g., JSON, CSV) so that inventory and sales data is retained after the program closes.

* **Customer Management:** Add a dedicated module to manage customer information and track their purchase history.

* **Advanced Reporting:** Introduce more complex reports, such as sales by category, sales over specific time periods, or low-stock alerts.

* **User Authentication:** Implement a basic login system for different user roles (e.g., administrator, sales associate).

* **Graphical User Interface (GUI):** Transition from a console-based interface to a more intuitive GUI using libraries like Tkinter, PyQt, or Kivy.
