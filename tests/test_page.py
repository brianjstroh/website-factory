"""Test module for the Page class"""
from pathlib import Path

from factory.page import Page

test_page = Page(name="Test Page", route="test/page", elements=[])


def test_page_html() -> None:
    """Test that the html property of Page returns as expected"""
    assert test_page.html == "<!doctype html>"


def test_page_html_path() -> None:
    """Test that the html property of Page returns as expected"""
    assert test_page.html_path == Path("templates/test/page.html")
