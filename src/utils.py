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


# converts txt files (should be of proper format, see README.md) to yml files
# @params in_file - input file (should include extenstion (ie .txt))
# @params out_file - output file (should include extenstion (ie .yml))
def txt_to_yml(in_file: str, out_file: str):
    with open(in_file) as file:
        data = ""
        for line in file:
            split = line.split(" - ")
            data += f"- word: {split[0]}\n  definition: '{split[1].replace('\n', '')}'\n  language: en\n"

    with open(out_file, 'w+') as file:
        file.write(data)
