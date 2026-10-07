import json
import os
from datetime import datetime


class Task:
    def __init__(self, title, category="General", completed=False, created_at=None):
        self.title = title
        self.category = category
        self.completed = completed
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M")

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        """Convert task object to dictionary for JSON storage."""
        return {
            "title": self.title,
            "category": self.category,
            "completed": self.completed,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a task object from a dictionary loaded from JSON."""
        return cls(
            title=data["title"],
            category=data.get("category", "General"),
            completed=data.get("completed", False),
            created_at=data.get("created_at"),
        )


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Read and load tasks from the JSON file."""
        if not os.path.exists(self.filename):
            self.tasks = []
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, IOError):
            print("\n[!] Warning: Could not read tasks.json. Starting fresh.")
            self.tasks = []

    def save_tasks(self):
        """Save current task list to the JSON file."""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([task.to_dict() for task in self.tasks], file, indent=4)
        except IOError as e:
            print(f"\n[!] Error saving tasks to file: {e}")

    def add_task(self, title, category="General"):
        """Add a new task and persist to file."""
        new_task = Task(title=title, category=category)
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task

    def complete_task(self, index):
        """Mark a task as completed by its 1-based index."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()
            return True
        return False

    def delete_task(self, index):
        """Delete a task by its 1-based index."""
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            return removed
        return None

    def get_all_tasks(self):
        return self.tasks