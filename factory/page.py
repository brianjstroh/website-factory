"""The page module holds the Page class for the web page factory"""

from pathlib import Path
from typing import List

from factory.elements import Element


class Page:
    """Page class holds elements of a web page"""

    def __init__(self, name: str, route: str, elements: List[Element]) -> None:
        """Create the Page instance"""
        self.name = name
        self.route = Path(route)
        self.elements = elements

    @property
    def html(self) -> str:
        """Compile HTML from each of the page elements"""
        out = ["<!doctype html>"]
        for element in self.elements:
            out += element.html
        return "\n".join(out)

    @property
    def html_path(self) -> Path:
        """Return the html path for the page"""
        return Path("templates").joinpath(self.route).with_suffix(".html")

    def to_html(self) -> None:
        """Write the Page's HTML out"""
        if not self.html_path.parent.exists():
            self.html_path.parent.mkdir()
        with open(self.html_path, mode="w", encoding="utf-8") as outfile:
            outfile.writelines(self.html)
