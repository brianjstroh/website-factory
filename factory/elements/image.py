"""The image module holds the Image class."""

from typing import List


class Image:
    """The Image class is a thin wrapper for html code to show an image file"""

    def __init__(self, name: str, file_path: str) -> None:
        """Create the Image instance"""
        self.name = name
        self.file_path = file_path

    @property
    def html(self) -> List[str]:
        """Return the HTML code for the element"""
        return [f'<img src="{{{{ {self.file_path} }}}}" alt="{self.name}">']
