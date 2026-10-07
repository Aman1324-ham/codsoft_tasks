import os
import sys
from todo import TaskManager


def clear_screen():
    """Clear terminal screen for a cleaner interface."""
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    print("==========================================")
    print("            PYTHON TO-DO APP              ")
    print("==========================================")


def display_menu():
    print("\n[1] View All Tasks")
    print("[2] Add New Task")
    print("[3] Mark Task as Completed")
    print("[4] Delete Task")
    print("[5] Exit")
    print("-" * 42)


def view_tasks(manager):
    tasks = manager.get_all_tasks()
    print("\n--- YOUR TASK LIST ---")
    if not tasks:
        print("No tasks found! Your list is empty.")
        return

    print(f"{'#':<4} {'Status':<12} {'Category':<12} {'Title':<25} {'Created'}")
    print("-" * 65)
    for idx, task in enumerate(tasks, start=1):
        status = "[✓] Done" if task.completed else "[ ] Pending"
        print(
            f"{idx:<4} {status:<12} {task.category:<12} {task.title:<25} {task.created_at}"
        )


def main():
    manager = TaskManager(filename="tasks.json")

    while True:
        clear_screen()
        print_header()
        view_tasks(manager)
        display_menu()

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            input("\nPress Enter to return to menu...")

        elif choice == "2":
            print("\n--- Add New Task ---")
            title = input("Enter task description: ").strip()
            if not title:
                print("Task description cannot be empty!")
                input("Press Enter to continue...")
                continue
            category = (
                input("Enter category (default: General): ").strip() or "General"
            )
            manager.add_task(title=title, category=category)
            print("✓ Task added successfully!")
            input("Press Enter to continue...")

        elif choice == "3":
            print("\n--- Complete Task ---")
            try:
                task_num = int(input("Enter task number to mark complete: ")) - 1
                if manager.complete_task(task_num):
                    print("✓ Task marked as completed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number.")
            input("Press Enter to continue...")

        elif choice == "4":
            print("\n--- Delete Task ---")
            try:
                task_num = int(input("Enter task number to delete: ")) - 1
                deleted = manager.delete_task(task_num)
                if deleted:
                    print(f"✓ Task '{deleted.title}' deleted successfully!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number.")
            input("Press Enter to continue...")

        elif choice == "5":
            print("\nGoodbye!")
            sys.exit(0)

        else:
            print("Invalid selection! Please enter a number from 1 to 5.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()