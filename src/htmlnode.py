class HTMLNode:
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        attributes = ""
        if self.props:
            for attribute, value  in (self.props).items():
                attributes += f"{attribute}={value} "
        return attributes
    
    def __repr__(self) :
        return f"
        HTMLNode(tag={self.tag}, value={self.value}, children= {self.children}, attributes={self.props})"
