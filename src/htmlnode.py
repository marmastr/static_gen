from enum import Enum

class HTMLTags(Enum):
    ADDRESS = "address"
    ARTICLE = "article"
    ASIDE = "aside"
    BLOCKQUOTE = "blockquote"
    CANVAS = "canvas"
    DD = "dd"
    DIV = "div"
    DL = "dl"
    DT = "dt"
    FIELDSET = "fieldset"
    FIGCAPTION = "figcaption"
    FIGURE = "figure"
    FOOTER = "footer"
    FORM = "form"
    HEADER = "header"
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    HR = "hr"
    LI = "li"
    MAIN = "main"
    NAV = "nav"
    NOSCRIPT = "noscript"
    OL = "ol"
    P = "p"
    PRE = "pre"
    SECTION = "section"
    TABLE = "table"
    TFOOT = "tfoot"
    UL = "ul"
    VIDEO = "video"



class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f'tag={self.tag}, value={self.value}, children={self.children}, props={self.props}'

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_string = ""
        if self.props is None or self.props == "":
            return props_string
        for k in self.props.keys():
            props_string += f' {k}="{self.props[k]}"'
        return props_string
