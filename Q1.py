def print_multiplication_table(n=12):
    # Print the main table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Print the product of i and j, formatted in a 4-character wide field
            print(f"{i*j:4d}", end="")
        print()  # Newline after each row

if __name__ == "__main__":
    # Call the function to print the multiplication table up to 12
    print_multiplication_table(12)
