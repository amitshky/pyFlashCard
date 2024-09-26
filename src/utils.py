from textwrap import TextWrapper


def wrap_meanings(meaning_string: list[str]) -> list[str]:
    wrapper = TextWrapper()
    wrapper.width = 40
    wrapper.subsequent_indent = "   "
    meanings = []
    for i, meaning in enumerate(meaning_string.split(";")):
        meaning = f"{i+1}. {meaning.strip()}"
        meanings.extend(wrapper.wrap(meaning))
    return meanings
