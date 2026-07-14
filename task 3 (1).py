balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)

except ValueError as e:
    print("Error:", e)

finally:
    print("Thank You for Using ATM")