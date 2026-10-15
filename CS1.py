
def merge_sort(products):
    if len(products) <= 1:
        return products

    mid = len(products) // 2
    left = merge_sort(products[:mid])
    right = merge_sort(products[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["price"] <= right[j]["price"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


products = []

n = int(input("Enter number of products: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    for i in range(n):
        print(f"\nProduct {i + 1}")
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))

        if price < 0:
            print("Price cannot be negative.")
            break

        products.append({
            "id": product_id,
            "name": name,
            "price": price
        })
    else:
        sorted_products = merge_sort(products)

        print("\nProducts Sorted by Price (Low to High)")
        print("-" * 45)
        print(f"{'ID':<10}{'Name':<20}{'Price':>10}")

        for p in sorted_products:
            print(f"{p['id']:<10}{p['name']:<20}₹{p['price']:>9.2f}")
