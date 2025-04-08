import asyncio
from playwright.async_api import async_playwright

# Your Instagram credentials
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

# Search keyword
SEARCH_QUERY = "Cars"  # You can change this to any keyword

async def scrape_instagram_profiles():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set headless=True for silent mode
        page = await browser.new_page()

        # Navigate to Instagram login page
        await page.goto("https://www.instagram.com/accounts/login/")
        await asyncio.sleep(3)

        # Enter username and password
        await page.fill("input[name='username']", USERNAME)
        await page.fill("input[name='password']", PASSWORD)
        await page.click("button[type='submit']")
        await asyncio.sleep(5)  # Wait for login

        # Go to search page with the correct query format
        await page.goto(f"https://www.instagram.com/explore/search/keyword/?q={SEARCH_QUERY}")
        await asyncio.sleep(5)

        # Extract profile URLs
        profiles = await page.eval_on_selector_all("a[href*='/']", "elements => elements.map(e => e.href)")
        profile_links = [link for link in profiles if "/p/" not in link][:20]  # Filter only profile links

        print("Collected Profile Links:")
        for link in profile_links:
            print(link)

        await browser.close()

# Run the script
asyncio.run(scrape_instagram_profiles())
