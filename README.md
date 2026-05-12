[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/T6sJM4w6)
# Week 5 — Midnight Mail Train

## Summary
This assignment uses a doubly linked list, recursion, and regular expressions to solve different train mail problems.  
The program can add and remove train cars, validate ticket codes, count labels recursively, and clean radio messages by removing spaces.  
The assignment also practices problem solving using both recursive and iterative approaches.

---

## Approach

### Problem 1:
Created a doubly linked list using nodes.  
Used `append_car()` to add cars to the end of the train.  
Used `detach_last_car()` to safely remove the final car.  
Used reverse traversal from tail to head for `to_reverse_list()`.

### Problem 2:
Used Python regular expressions with `re.fullmatch()` to check whether a ticket code follows the format:
`MM-1234`

### Problem 3:
Used recursion on a list.  
The function checks the first label and recursively processes the remaining labels until the list becomes empty.

### Problem 4:
Used recursion on a string.  
The function removes spaces one character at a time until the message becomes empty.

---

## Complexity

### Problem 1 — Doubly Linked List
- append_car:
  - Time Complexity: O(1)
  - Space Complexity: O(1)
  - Reason: Adds directly to the tail.

- detach_last_car:
  - Time Complexity: O(1)
  - Space Complexity: O(1)
  - Reason: Removes directly from the tail.

- to_reverse_list:
  - Time Complexity: O(n)
  - Space Complexity: O(n)
  - Reason: Visits every node once and stores values in a list.

### Problem 2 — Ticket Code Validation
- Time Complexity: O(n)
- Space Complexity: O(1)
- Reason: Regex checks characters in the string once.

### Problem 3 — Recursive Label Counter
- Time Complexity: O(n)
- Space Complexity: O(n)
- Reason: Recursive call for each item in the list.

### Problem 4 — Recursive Message Cleaner
- Time Complexity: O(n)
- Space Complexity: O(n)
- Reason: Recursive call for each character in the string.

---

## Edge-case checklist

- [x] empty train
- [x] one train car
- [x] invalid ticket code
- [x] empty label list
- [x] empty message
- [x] one-character or all-space message

---

## Assistance & Sources

- AI used? Yes

- What it helped with:
  - Understanding recursion
  - Checking linked list logic
  - Reviewing edge cases
  - Improving code formatting and comments

- Other sources used:
  - Python documentation
  - Class lecture notes
  - VS Code and pytest documentation