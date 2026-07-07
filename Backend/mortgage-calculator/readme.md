# Mortgage Calculator (Java)

A simple console-based Mortgage Calculator developed in Java to calculate the monthly mortgage payment based on the loan amount, annual interest rate, and loan term.

This project was built to strengthen my understanding of Java fundamentals, object-oriented programming concepts, user input handling, mathematical calculations, and clean console applications.

---

## Features

- Accepts mortgage amount from the user
- Accepts annual interest rate
- Accepts loan period (years)
- Calculates the monthly mortgage payment
- Displays results using formatted currency and percentage values
- Simple and easy-to-use console interface

---

## Technologies

- Java
- IntelliJ IDEA
- Java Scanner
- NumberFormat API
- Math Library

---

## How It Works

The application asks the user to enter:

- Mortgage amount
- Annual interest rate (without the `%` symbol)
- Loan period in years

It then calculates the monthly payment using the standard mortgage formula and displays the result in a formatted summary.

Example:

```
Hello!

Mortgage amount: 250000
Annual Interest Rate (without %): 7.5
Period (Years): 20

====================
MORTGAGE CALCULATOR
====================

Mortgage: $250,000.00

Interest: 7%

Years: 20

Monthly Payment: $2,013.85

====================
```

---

## Mortgage Formula

The monthly mortgage payment is calculated using the standard amortization formula:

\[
M = P \times \frac{r(1+r)^n}{(1+r)^n-1}
\]

Where:

- **M** = Monthly payment
- **P** = Mortgage amount
- **r** = Monthly interest rate
- **n** = Total number of monthly payments

---

## What I Learned

This project helped me practice:

- Java syntax and programming fundamentals
- User input using `Scanner`
- Mathematical calculations with `Math.pow()`
- Formatting currency and percentages using `NumberFormat`
- Writing clean and readable Java code
- Building complete console applications

---

## Future Improvements

- Input validation
- Mortgage payment schedule (amortization table)
- Total interest paid calculation
- Extra payment simulation
- Graphical User Interface (JavaFX)
- Spring Boot REST API version

---

## Author

**Dylan Kondo Tshilay**

GitHub: https://github.com/dylantshilay-sudo
