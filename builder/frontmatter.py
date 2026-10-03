class MissingFrontmatterError(Exception):
    pass


def add_lines(text: bytes, lines: list[str]) -> bytes:
    opening, closing, body = text.partition(b"\n---\n")
    if not (opening.startswith(b"---\n") and closing):
        raise MissingFrontmatterError
    return opening + b"\n" + "\n".join(lines).encode() + closing + body
