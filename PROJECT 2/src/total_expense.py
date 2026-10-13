def main():
    print("=" * 40)
    print("          EXPENSE TRACKER")
    print("=" * 40)

    # Starting total
    total = 0.0

    print("\nEnter your expenses one by one.")
    print("Enter 0 when you have finished.\n")

    while True:
        try:
            expense = float(input("Enter expense amount: ₹"))

            # Stop when the user enters 0
            if expense == 0:
                break

            # Do not allow negative expenses
            if expense < 0:
                print("Please enter a positive amount.")
                continue

            # Add the new expense to the total
            total = total + expense

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Display the final total
    print("\n" + "=" * 40)
    print(f"Total Spent: ₹{total:.2f}")
    print("=" * 40)


# Run the program
if __name__ == "__main__":
    main()
    