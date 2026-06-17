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

    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        html_props = ""
        for name in self.props:
            html_props += f' {name}=\"{self.props[name]}\"'
        return html_props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None) -> str:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("all leaf nodes must have a value") 
        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(
        self, 
        tag: str, 
        children: list[HTMLNode], 
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("all parent nodes must have a tag")
        if not self.children:
            raise ValueError("all parent nodes must have children")
        
        children_html = ""
        for node in self.children:
            children_html += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"


    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


if __name__ == "__main__":
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())