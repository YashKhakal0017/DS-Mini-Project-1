
# Web Browser Back Button Using Stack

## 1. Introduction

This mini-project implements the basic back button functionality of a web browser using the Stack data structure in Python.

When a user visits different web pages, the browser stores previously visited pages in a stack. The user can return to the previous page using the Back operation and move forward again using the Forward operation.

## 2. Objectives

- Understand the Stack data structure.
- Implement the LIFO (Last In, First Out) principle.
- Simulate browser back and forward navigation.
- Manage previously visited web pages efficiently.
- Understand stack operations such as push and pop.

## 3. Description

The project uses two stacks:

1. **Back Stack:** Stores previously visited pages.
2. **Forward Stack:** Stores pages that can be revisited using the Forward operation.

The current page stores the URL of the page currently being viewed.

When a new page is visited, the current page is pushed onto the Back Stack. When the Back button is pressed, the current page is moved to the Forward Stack, and the previous page is restored.

Visiting a new page clears the Forward Stack because the previous forward-navigation path is no longer valid.

## 4. Technologies Used

- Programming Language: Python
- Data Structure: Stack
- IDE: Visual Studio Code

## 5. Features

- Visit a new web page.
- Navigate to the previous page using Back.
- Navigate forward using Forward.
- Display the current page.
- Display the back stack and forward stack.
- Handle empty-stack conditions.

## 6. Stack Operations Used

- **Push:** Adds a page to a stack.
- **Pop:** Removes the top page from a stack.
- **LIFO:** The last page added to a stack is the first page removed.

Python lists are used to implement the stacks.

## 7. How to Run the Project

1. Install Python 3.
2. Open the project folder in Visual Studio Code.
3. Save the code as `browser_stack.py`.
4. Open the VS Code terminal.
5. Execute the following command:

```bash
python browser_stack.py
```

No additional Python libraries are required.

## 8. Sample Output

```text
===== Web Browser Navigation =====
1. Visit New Page
2. Go Back
3. Go Forward
4. Show Current Page
5. Show Browser History
6. Exit

Enter your choice: 1
Enter website URL: www.google.com
Visited: www.google.com

Enter your choice: 1
Enter website URL: www.youtube.com
Visited: www.youtube.com

Enter your choice: 2
Moved back to: www.google.com

Enter your choice: 3
Moved forward to: www.youtube.com
```

## 9. Time Complexity

| Operation | Time Complexity |
|---|---|
| Visit a new page | O(1), excluding forward-stack clearing |
| Go Back | O(1) |
| Go Forward | O(1) |
| Show current page | O(1) |
| Show browser history | O(n) |

Clearing the Forward Stack when visiting a new page takes O(n) time in the worst case.

## 10. Applications

- Web browser navigation
- Undo and redo operations
- Navigation in mobile applications
- Page history management
- State management in software applications

## 11. Conclusion

This mini-project demonstrates how stacks can be used to implement browser back and forward functionality.

It uses the LIFO principle to manage navigation history and shows how two stacks can support efficient page navigation.
