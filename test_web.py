import pytest
import re
from playwright.sync_api import Page, expect

@pytest.fixture(autouse=True)
def setup(page: Page):
    """Automatické otevření domovské stránky před každým testem."""
    page.goto("https://www.wikipedia.org/")

def test_wikipedia_title(page: Page):
    """Ověření přesné shody titulku stránky."""
    expect(page).to_have_title("Wikipedia")

def test_search_input_visibility(page: Page):
    """Ověření viditelnosti vyhledávacího pole pomocí role-based lokátoru."""
    search_input = page.get_by_role("searchbox")
    expect(search_input).to_be_visible()

def test_main_heading_visibility(page: Page):
    """Ověření přítomnosti hlavního nadpisu na stránce."""
    heading = page.get_by_role("heading", name="Wikipedia")
    expect(heading).to_be_visible()