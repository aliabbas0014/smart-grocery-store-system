
# Smart Grocery Store Management System

# Product and sales records
products = []
sales_records = []


# Function to find a product using its ID
def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


# Function to get a valid positive integer
def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Function to add a new product
def add_product():
    print("\n--- Add New Product ---")

    product_id = get_positive_integer("Enter Product ID: ")

    if find_product(product_id) is not None:
        print("Error: This Product ID already exists!")
        return

    name = input("Enter Product Name: ").strip()
    while name == "":
        print("Product name cannot be empty.")
        name = input("Enter Product Name: ").strip()

    category = input("Enter Product Category: ").strip()
    while category == "":
        print("Category cannot be empty.")
        category = input("Enter Product Category: ").strip()

    while True:
        try:
            price = float(input("Enter Product Price: "))
            if price > 0:
                break
            print("Price must be greater than zero.")
        except ValueError:
            print("Please enter a valid price.")

    while True:
        try:
            stock = int(input("Enter Available Stock: "))
            if stock >= 0:
                break
            print("Stock cannot be negative.")
        except ValueError:
            print("Please enter a valid stock quantity.")

    new_product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }

    products.append(new_product)
    print("Product added successfully!")


# Function to display all products
def display_products():
    print("\n--- All Products ---")

    if len(products) == 0:
        print("No products available.")
        return

    for product in products:
        print("--------------------------------")
        print("Product ID:", product["id"])
        print("Name:", product["name"])
        print("Category:", product["category"])
        print("Price: Rs.", product["price"])
        print("Available Stock:", product["stock"])


# Function to search for a product
def search_product():
    print("\n--- Search Product ---")
    choice = input("Search by ID or Name (I/N): ").strip().lower()

    if choice == "i":
        product_id = get_positive_integer("Enter Product ID: ")
        product = find_product(product_id)

    elif choice == "n":
        name = input("Enter Product Name: ").strip().lower()
        product = None

        for item in products:
            if item["name"].lower() == name:
                product = item
                break
    else:
        print("Invalid search option!")
        return

    if product is not None:
        print("\nProduct Found!")
        print("Product ID:", product["id"])
        print("Name:", product["name"])
        print("Category:", product["category"])
        print("Price: Rs.", product["price"])
        print("Available Stock:", product["stock"])
    else:
        print("Product not found!")


# Function to update product stock
def update_stock():
    print("\n--- Update Product Stock ---")

    product_id = get_positive_integer("Enter Product ID: ")
    product = find_product(product_id)

    if product is None:
        print("Product not found!")
        return

    print("Product:", product["name"])
    print("Current Stock:", product["stock"])
    print("1. Add More Stock")
    print("2. Set New Stock Quantity")

    choice = input("Enter your choice: ")

    if choice == "1":
        quantity = get_positive_integer("Enter quantity to add: ")
        product["stock"] += quantity

    elif choice == "2":
        while True:
            try:
                quantity = int(input("Enter new stock quantity: "))
                if quantity >= 0:
                    product["stock"] = quantity
                    break
                print("Stock cannot be negative.")
            except ValueError:
                print("Please enter a valid number.")

    else:
        print("Invalid choice!")
        return

    print("Stock updated successfully!")
    print("Updated Stock:", product["stock"])


# Function to process customer sale
def process_sale():
    print("\n--- Process Customer Sale ---")

    product_id = get_positive_integer("Enter Product ID: ")
    product = find_product(product_id)

    if product is None:
        print("Product not found!")
        return

    print("Product:", product["name"])
    print("Price: Rs.", product["price"])
    print("Available Stock:", product["stock"])

    quantity = get_positive_integer("Enter Purchase Quantity: ")

    if quantity > product["stock"]:
        print("Insufficient stock! Sale cannot be completed.")
        return

    total_amount = product["price"] * quantity
    product["stock"] -= quantity

    sale = {
        "product_id": product["id"],
        "product_name": product["name"],
        "quantity_sold": quantity,
        "total_amount": total_amount
    }

    sales_records.append(sale)

    print("\n--- Purchase Summary ---")
    print("Product:", product["name"])
    print("Quantity Sold:", quantity)
    print("Total Amount: Rs.", total_amount)
    print("Remaining Stock:", product["stock"])
    print("Sale completed successfully!")


# Function to view sales records
def view_sales_records():
    print("\n--- Sales Records ---")

    if len(sales_records) == 0:
        print("No sales records available.")
        return

    for sale in sales_records:
        print("--------------------------------")
        print("Product ID:", sale["product_id"])
        print("Product Name:", sale["product_name"])
        print("Quantity Sold:", sale["quantity_sold"])
        print("Total Amount: Rs.", sale["total_amount"])


# Function to generate store report
def generate_report():
    print("\n--- Store Report ---")

    total_products = len(products)
    total_stock = 0
    total_revenue = 0

    for product in products:
        total_stock += product["stock"]

    for sale in sales_records:
        total_revenue += sale["total_amount"]

    print("Total Products:", total_products)
    print("Total Available Stock:", total_stock)
    print("Total Sales Transactions:", len(sales_records))
    print("Total Revenue: Rs.", total_revenue)

    print("\nProducts with Stock Below 5 Units:")

    low_stock_found = False

    for product in products:
        if product["stock"] < 5:
            print(product["name"], "- Stock:", product["stock"])
            low_stock_found = True

    if not low_stock_found:
        print("No products have low stock.")

    if total_products > 0:
        highest_price_product = max(products, key=lambda p: p["price"])
        lowest_price_product = min(products, key=lambda p: p["price"])

        print("\nHighest Priced Product:")
        print(highest_price_product["name"], "- Rs.", highest_price_product["price"])

        print("\nLowest Priced Product:")
        print(lowest_price_product["name"], "- Rs.", lowest_price_product["price"])
    else:
        print("\nNo products available for price comparison.")


# Main menu
while True:
    print("\n====================================")
    print("     SMART GROCERY STORE SYSTEM")
    print("====================================")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        add_product()

    elif choice == "2":
        display_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_stock()

    elif choice == "5":
        process_sale()

    elif choice == "6":
        view_sales_records()

    elif choice == "7":
        generate_report()

    elif choice == "8":
        print("Thank you for using Smart Grocery Store System!")
        break

    else:
        print("Invalid choice! Please select between 1 and 8.")
