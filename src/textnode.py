from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMG = "imgage"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        is_equal = True
        url_self = None
        url_other = None

        if self.text_type != other.text_type:
            is_equal = False

        if self.url is not None:
            url_self = self.url.casefold()
        if other.url is not None:
            url_other = other.url.casefold()
        if url_self != url_other:
            is_equal = False

        if self.text != other.text:
            is_equal = False

        return is_equal

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
