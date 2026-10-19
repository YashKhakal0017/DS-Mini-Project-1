
# Mini Project: Web Browser Back Button Using Stack

class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def visit_page(self, url):
        if self.current_page is not None:
            self.back_stack.append(self.current_page)

        self.current_page = url
        self.forward_stack.clear()

        print("Visited:", self.current_page)

    def go_back(self):
        if not self.back_stack:
            print("No previous page available.")
            return

        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()

        print("Moved back to:", self.current_page)

    def go_forward(self):
        if not self.forward_stack:
            print("No next page available.")
            return

        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()

        print("Moved forward to:", self.current_page)

    def show_current_page(self):
        if self.current_page is None:
            print("No page is currently open.")
        else:
            print("Current Page:", self.current_page)

    def show_history(self):
        print("\n--- Browser History ---")
        print("Back Stack:", self.back_stack)
        print("Current Page:", self.current_page)
        print("Forward Stack:", self.forward_stack)


def main():
    browser = Browser()

    while True:
        print("\n===== Web Browser Navigation =====")
        print("1. Visit New Page")
        print("2. Go Back")
        print("3. Go Forward")
        print("4. Show Current Page")
        print("5. Show Browser History")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            url = input("Enter website URL: ").strip()

            if url:
                browser.visit_page(url)
            else:
                print("URL cannot be empty.")

        elif choice == "2":
            browser.go_back()

        elif choice == "3":
            browser.go_forward()

        elif choice == "4":
            browser.show_current_page()

        elif choice == "5":
            browser.show_history()

        elif choice == "6":
            print("Thank you for using the browser simulation!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
