# Pascal's Triangle Question
In this project we were tasked to create a function that returns a list of integers representing the pascal's triangle
The function should return an empty list if n <= 0

---

## Definition
Pascal’s triangle is a pattern of the triangle which is based on nCr.

## Pictorial Representation

![image](Screenshot%25from%252023-09-28%2512-43-51.png)

## Algorithmn

- Take a number of rows to be printed, lets assume it to be n
- Make outer iteration i from 0 to n times to print the rows.
- Make inner iteration for j from 0 to (N – 1).
- Print single blank space ” “.
- Close inner loop (j loop) //its needed for left spacing.
- Make inner iteration for j from 0 to i.
- Print nCr of i and j.
- Close inner loop.
- print newline character (\n) after each inner iteration

## Time Complexity

- O(N^2)
