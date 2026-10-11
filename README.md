Name: Merve Dişci

Student Number: 2504109075

Department: Management Information Systems

Course Name: MIS203 Basic Programming


Week01
It asks for basic student and career info from the user and prints a clean profile on the screen.

Week02
AI Tool Used: ChatGPT

Prompt Used: After the loop ends, print the number of students and the average score, rounded to 2 decimal places

What did I change: I wrote the code myself at first but I couldn't remember to get the average.

What does break do in my program: It exits the loop immediately; if you didn't enter, it prints 'No student entered.', if you entered students, it prints 
the score letter and how many student you entered and average score.


Week03
AI Tool Used: Gemini
Prompt Used:
Create a Python program named ticket_office.py that sells cinema tickets in a loop using inputs, type conversion, f-strings, and conditions (if/elif/else). 
Validate age (0-120), day (weekday/weekend), and student status (yes/no). 
Apply discounts in order: <6 (100% Free), >=65 (50% Senior), 6-12 (40% Child), Student <=25 (30% Student), Else (0% Standard). 
Keep track of total tickets sold, revenue, average price, and free tickets.

What did you change?
I adjusted the output messages to make sure they matched the exact required format.
I also added a try-except block for the age input so the program wouldn't crash if someone entered a letter instead of a number.

Why does the order of the rules matter?
The order is important because Python stops checking conditions as soon as it finds the first true one. If we put the Student rule before the Child rule,
a 10-year-old student would get the 30% Student discount instead of the 40% Child discount that they actually deserve.

Week04 
AI Tool Used: Gemini
Prompt Used: Write a Python script for a Smart Budget & Spending Analyst that handles monthly budgets, categorizes expenses with validation, includes randomized financial surprise events, and prints a formatted summary report.

What I changed: I added robust input validation loops with try-except blocks, restricted negative expense entries, and applied :.2f f-string formatting for currency precision.

Why does the order of the rules matter?
The order of the rules matters because the code needs to ask for inputs and fix any errors first before it can accurately calculate the final results.
