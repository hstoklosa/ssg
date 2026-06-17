class HTMLNode:
    def __init__(self, 
        tag: str | None = None, 
        value: str | None = None, 
        children: list[HTMLNode] | None = None, 
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join([f" {name}=\"{value}\"" for name, value in self.props.items()])

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


if __name__ == "__main__":
    node = HTMLNode("p", "This is a html node", None, {"href": "https://www.google.com", "target": "_blank"})
    print(node.props_to_html())