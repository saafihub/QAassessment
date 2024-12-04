from pages.base_page import BasePage
from pages.ui_locators import UiLocators

class TodoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def add_todo(self, todo_text):
        self.fill_input(UiLocators.todo_input, todo_text)
        self.press_key(UiLocators.todo_input, "Enter")

    def verify_todo_text(self, todo_text):
        return todo_text in self.get_text(UiLocators.todo_list)

    # Check if the input field is empty
    def is_input_field_empty(self):
        input_field = self.locator_get(UiLocators.todo_input)
        return input_field.input_value() == ''

    def edit_todo_text(self, old_text, new_text):
        self.doubleclick(f'{UiLocators.todo_label_text}"{old_text}"]')
        self.fill_input(UiLocators.edit, new_text)

    def press_key_enter(self, key):
        self.press_enter_key(key)

    def mark_todo_completed(self):
        self.click(UiLocators.todo_toggle)

    def toggle_todo_checkbox(self, todo_text):
        self.click(f'{UiLocators.todo_label_text}"{todo_text}"{UiLocators.todo_xsibling}')

    def verify_todo_completed(self, todo_text):
        todo = self.locator_get(f'{UiLocators.todo_label_text}"{todo_text}"{UiLocators.todo_xancestor}')
        return 'completed' in todo.get_attribute('class')

    def select_all_check_uncheck(self, select):
        self.check_uncheck(UiLocators.checkall, select)

    def delete_todo(self, todo_text):
        self.click(f'{UiLocators.todo_text}"{todo_text}")')
        self.click(f'{UiLocators.todo_text}"{todo_text}"{UiLocators.todo_destroy}')

    def apply_filter(self, filter_type):
        self.click(f'{UiLocators.todo_button_text}"{filter_type.capitalize()}"]')

    def get_filtered_todos(self, filter_type):
        if filter_type == "Completed":
            todo_selector = f'{UiLocators.todo_list}{UiLocators.complete}'
        elif filter_type == "Active":
            todo_selector = f'{UiLocators.todo_list}:not({UiLocators.complete})'
        else:
            todo_selector = UiLocators.todo_list
        self.page.wait_for_selector(todo_selector, timeout=30000)

        todos = self.page.locator(f"{todo_selector} label").all_text_contents()
        print(f"Filtered todos ({filter_type}): {todos}")
        return todos

    # Clear all completed todos
    def clear_completed_todos(self):
        self.click(UiLocators.clear_complete)

    def get_todo_label_exists(self):
        self.element_exists(UiLocators.todo_label)

    # Get completed todos
    def get_completed_todos(self):
        todo_list = self.locator_get(UiLocators.todo_list)
        completed_todos = todo_list.locator(UiLocators.complete)
        return completed_todos.all_text_contents()

    def is_todo_present(self, todo_text):
        todo_list = self.locator_get(UiLocators.todo_list)
        todo_items = todo_list.all_text_contents()
        return any(todo_text in todo for todo in todo_items)

    def get_all_todos(self):
        todos = self.locator_get(UiLocators.todo_list)
        return todos.all_text_contents()

    def get_count_todo_list(self):
        return self.get_text(UiLocators.todo_count)
