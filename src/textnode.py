from enum import Enum


class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMG_TEXT = "imgage"

class TextNode():
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TextType(TEXT_TYPE)
        self.url = URL

    def __eq__(self, other):
        if self.text_type == other.text_type:
            return True
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'
