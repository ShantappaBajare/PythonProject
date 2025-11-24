from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.edge.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.youtube.com/")
    page.fill("")
    page.press("")
    browser.close()
