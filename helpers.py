def content_to_str(content: dict) -> str:
    """
    Converts area content to a string.
    :param content: dict with content of a single area
    :return: formatted string
    """
    fu = ""
    for key, value in content.items():
        foo = f"- {key}: {value}\n"
        fu += foo
    fu = fu.strip()

    return fu
