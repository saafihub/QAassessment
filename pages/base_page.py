class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url):
        self.page.goto(url)

    def click(self, selector):
        self.page.click(selector)

    def doubleclick(self, selector):
        self.page.dblclick(selector)

    def fill_input(self, selector, value):
        self.page.fill(selector, value)

    def press_key(self, selector, key):
        self.page.press(selector, key)

    def press_enter_key(self, key):
        self.page.keyboard.press(key)

    def check_uncheck(self, selector, select):
        self.page.check(selector) if select == 'Yes' else self.page.uncheck(selector)

    def filter_types(self, filter):
        self.page.get_by_role("link", name=filter).click()

    def locator_get(self, selector):
        return self.page.locator(selector)

    def get_text(self, selector):
        return self.page.inner_text(selector)

    def element_exists(self, selector):
        return self.page.query_selector(selector) is not None
