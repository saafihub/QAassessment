import os
from subprocess import run
import json
from playwright.sync_api import sync_playwright
from utils.logger import error_logger

with open("config.json") as config_file:
    config = json.load(config_file)

logger = error_logger()


def before_all(context):
    browser_type = config["browser"]
    valid_browsers = {"chromium", "firefox", "webkit"}
    if browser_type not in valid_browsers:
        print(f"Invalid browser specified: {browser_type}. Defaulting to Chromium.")
        browser_type = "chromium"

    context.playwright = sync_playwright().start()
    context.browser = getattr(context.playwright, browser_type).launch(headless=False)
    context.page = context.browser.new_page()
    context.page.set_viewport_size({"width": 1920, "height": 1080})
    print("Before scenario\n")


def after_step(context, step):
    if step.status == "failed":
        logger.error(f"Step failed: {step.name}")
        if step.exception:
            logger.exception(f"Exception occurred: {step.exception}")

        for msg in context.page.console_messages():
            logger.error(f"Console Log: {msg.text}")

        context.page.on('response', lambda response: logger.info(f"Response: {response.url}"))
        context.page.on('request', lambda request: logger.info(f"Request: {request.url}"))


def after_scenario(context, scenario):
    print(f"Scenario status: {scenario.status}")
    if scenario.status == "failed":
        logger.error(f"Scenario failed: {scenario.name}")
        screenshot_dir = "failed_screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name}_failed.png")
        context.page.screenshot(path=screenshot_path)
        print(f"Saved screenshot: {screenshot_path}")


def after_all(context):
    context.browser.close()
    context.playwright.stop()

