while True:
    print("1. View products")
    print("2. Add to cart")
    print("3. Checkout")

    choice = input("Choose: ")

    if choice == "1":
        store.show_products()

    elif choice == "2":
        name = input("Product name: ")
        store.add_to_cart(name)

    elif choice == "3":
        store.checkout()
        break