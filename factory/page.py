"""The page module holds the Page class for the web page factory"""

from typing import Any, List


class Page:
    """Page class holds elements of a web page"""

    def __init__(self, name: str, route: str, elements: List[Any]) -> None:
        """Create the Page instance"""
        self.name = name
        self.route = route
        self.elements = elements
