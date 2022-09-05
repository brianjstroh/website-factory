"""The navigation_bar module holds the NavigationBar class."""

from typing import Dict, List


class NavigationBar:
    """The NavigationBar"""

    def __init__(self, name: str, route: str, links: Dict[str, str]) -> None:
        """Create the Element instance"""
        self.name = name
        self.route = route
        self.links = links

    @property
    def html(self) -> List[str]:
        """Return the HTML code for the element"""
        out = ["<nav>"]
        for page_name, page_ref in self.links.items():
            out += [f"<li><a href=\"{{ url_for('{page_ref}') }}\">{page_name}</a>"]
        out += ["</nav>"]
        return out

    @property
    def python(self) -> str:
        """Return the Python code for the element"""
        return ""
