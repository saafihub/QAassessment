from behave import given, when, then
import json
from pages.todo_page import TodoPage
from utils.logger import info_logger

with open("config.json") as config_file:
    config = json.load(config_file)

BASE_URL = config["base_url"]

logger = info_logger()


@given('I am on the Todos page')
def step_impl(context):
    context.todo_page = TodoPage(context.page)
    context.todo_page.visit(BASE_URL)
    logger.info("Navigated to Todos page")


@when('I type "{todo_text}" in the input field and press Enter')
def step_impl(context, todo_text):
    context.todo_page.add_todo(todo_text)
    logger.info(f"Added todo: {todo_text}")


@then('the todo "{todo_text}" should appear in the list')
def step_impl(context, todo_text):
    assert context.todo_page.verify_todo_text(todo_text)
    logger.info(f"Verified todo '{todo_text}' is in the list")


@given('I have a todo "{todo_text}"')
def step_impl(context, todo_text):
    context.todo_page.add_todo(todo_text)
    logger.info(f"Pre-condition: Added todo '{todo_text}'")


@given('I have a todo below todo list')
def step_impl(context):
    for row in context.table:
        context.todo_page.add_todo(row["todo_text"])
        logger.info(f"Pre-condition: Added todo '{row}'")


@when('I double-click on "{todo_text}" and change the text to "{new_text}"')
def step_impl(context, todo_text, new_text):
    context.todo_page.edit_todo_text(todo_text, new_text)
    logger.info(f"Edited todo '{todo_text}' to '{new_text}'")


@then('the todo should be updated to "{new_text}"')
def step_impl(context, new_text):
    assert context.todo_page.verify_todo_text(new_text)
    logger.info(f"Verified todo updated to '{new_text}'")


@when('I click the checkbox next to todo lists')
def step_impl(context):
    for row in context.table:
        context.todo_page.toggle_todo_checkbox(row["todo_text"])
        logger.info(f"Marked todo '{row}' as completed")


@then('the todo "{todo_text}" should be marked as completed')
def step_impl(context, todo_text):
    assert context.todo_page.verify_todo_completed(todo_text) is True, f"Todo '{todo_text}' is not marked as completed"
    logger.info(f"Verified todo '{todo_text}' is completed")


@then('the todo "{todo_text}" should be marked as not completed')
def step_impl(context, todo_text):
    assert not context.todo_page.verify_todo_completed(todo_text), f"Todo '{todo_text}' should not be completed"
    logger.info(f"Verified todo '{todo_text}' is not been completed")


@when('I have a completed todo and select all as "{todo_text}"')
def step_impl(context, todo_text):
    context.todo_page.select_all_check_uncheck(todo_text)
    logger.info(f"Select/Unselect all Checkboxes")


@when('I click the delete button next to "{todo_text}"')
def step_impl(context, todo_text):
    # context.todo_page.delete_todo_text(todo_text)
    context.todo_page.delete_todo(todo_text)
    logger.info(f"Deleted todo '{todo_text}'")


@then('the todo "{todo_text}" should be removed from the list')
def step_impl(context, todo_text):
    assert not context.todo_page.get_todo_label_exists()
    logger.info(f"Verified todo '{todo_text}' is removed")


@when('I click on the "{filter_type}" filter')
def step_impl(context, filter_type):
    context.todo_page.filter_types(filter_type)
    logger.info(f"Applied filter: {filter_type}")


@then('I should see {filter_type} todos')
def step_impl(context, filter_type):
    visible_todos = context.todo_page.get_visible_todos()
    if filter_type == 'all':
        assert len(visible_todos) > 0
    elif filter_type == 'active':
        assert all(todo['completed'] == False for todo in visible_todos)
    elif filter_type == 'completed':
        assert all(todo['completed'] == True for todo in visible_todos)
    logger.info(f"Verified the filter '{filter_type}' works correctly")


@when('I click on Clear completed')
def step_impl(context):
    context.todo_page.clear_completed_todos()
    logger.info("Clicked 'Clear completed'")


@then('only completed todos should be removed')
def step_impl(context):
    active_todos = context.todo_page.get_active_todos()
    completed_todos = context.todo_page.get_completed_todos()
    assert len(completed_todos) == 0
    assert len(active_todos) > 0
    logger.info("Verified only completed todos are cleared")


@then('I should see count of "{todo_text}" as "{gcount}"')
def step_impl(context, todo_text, gcount):
    filtered_todos = context.todo_page.get_filtered_todos(todo_text)
    logger.info(filtered_todos)
    assert len(filtered_todos) == int(gcount)
    logger.info("Verified only completed todos are cleared")


@then("I should see all todos including")
def step_verify_all_todos(context):
    todos = context.todo_page.get_all_todos()
    for row in context.table:
        todo_text = row["todo_text"]
        assert todo_text in todos, f"Todo '{todo_text}' not found in {todos}"
        logger.info("Verified only completed todos are cleared:" + str(todo_text))


@then('I should see count of todo as below')
def step_impl(context):
    getcount = context.todo_page.get_count_todo_list()
    for row in context.table:
        logger.info(f"Actual count: {getcount}, Expected count: {row['text_count']}")
        assert str(getcount) == str(row["text_count"])
        logger.info("Verified only completed todos are cleared:" + str(getcount))


@then('the todo "{todo_text}" should remain unchanged')
def step_verify_todo_in_list(context, todo_text):
    assert context.todo_page.verify_todo_text(todo_text)
    logger.info(f"Verified todo is in the list: {todo_text}")


@when('I press "{key}"')
def step_press_key(context, key):
    context.todo_page.press_enter_key(key)
    logger.info(f"Press Key : {key}")


@when('I double-click on "{todo_text}" and leave the input field empty')
def step_empty_input(context, todo_text, new_text=""):
    context.todo_page.edit_todo_text(todo_text, new_text)
    logger.info(f"Edited todo '{todo_text}' to empty string("")")
