from textnode import TextType,TextNode



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
        node_text_str = old_node.text
        inside_group = False
        while len(nodetext_str) > 0:
            segments = node_text_str.partition(delimiter)
            if segments[0].startswith(delimiter):
                inside_group = True
                _ = segments.pop(0)
                new_nodes.append(TextNode(segments.pop(0),text_type))
                _se

    return new_nodes
