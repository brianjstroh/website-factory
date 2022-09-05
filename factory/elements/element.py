"""The element module holds the Element abstract base class."""

from abc import ABC


class Element(ABC):
    """The Element class holds common attributes and methods for all Web Elements"""

    def __init__(self, name: str, route: str) -> None:
        """Create the Element instance"""
        self.name = name
        self.route = route

    @property
    def html(self) -> None:
        """Return the HTML code for the Element"""
        raise NotImplementedError

    @property
    def python(self) -> None:
        """Return the Python code for the Element"""
        raise NotImplementedError

    def to_html(self) -> None:
        """Write the element to its HTML page"""
        raise NotImplementedError

    def to_python(self) -> None:
        """Write the element to its Python module"""
        raise NotImplementedError
