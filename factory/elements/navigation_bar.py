"""The navigation_bar module holds the NavigationBar class."""

from typing import Dict


class NavigationBar:
    """The NavigationBar"""

    def __init__(self, name: str, route: str, links: Dict[str, str]) -> None:
        """Create the Element instance"""
        self.name = name
        self.route = route
        self.links = links

    @property
    def html(self) -> str:
        """Return the HTML code for the element"""
        out = ["<nav>"]
        for page_name, page_ref in self.links.items():
            out += f"<li><a href=\"{{ url_for('{page_ref}') }}\">{page_name}</a>"
        out += ["</nav>"]
        return "\n".join(out)

    @property
    def python(self) -> str:
        """Return the Python code for the element"""
        return ""

    def to_html(self) -> None:
        """Write the NavigationBar to its HTML page"""
        with open(f"templates{self.route}", mode="a", encoding="utf-8") as outfile:
            outfile.writelines(self.html)

    def to_python(self) -> None:
        """Write the NavigationBar to its Python module"""
        with open(self.route, mode="a", encoding="utf-8") as outfile:
            outfile.writelines(self.html)
