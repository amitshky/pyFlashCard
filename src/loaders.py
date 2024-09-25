import random
import yaml
import os
from textwrap import TextWrapper
from glob import glob

try:
    from yaml import CLoader as Loader
except:
    from yaml import Loader

from ._types import vocabs_list_t, vocabs_t, path_list_t


# TODO: move this somewhere else and set wrapper constants in another file
def wrap_meanings(meaning_string: list[str]) -> list[str]:
    wrapper = TextWrapper()
    wrapper.width = 40
    wrapper.subsequent_indent = "   "
    meanings = []
    for i, meaning in enumerate(meaning_string.split(";")):
        meaning = f"{i+1}. {meaning.strip()}"
        meanings.extend(wrapper.wrap(meaning))
    return meanings


def load_text(path: str) -> vocabs_list_t:
    vocabs_list: vocabs_list_t = []

    with open(path) as f:
        for i, line in enumerate(f):
            split: list[str] = line.split(" - ")
            if len(split) != 2:
                raise Exception(
                    f'ERROR in file: "{path}"\nWrong format on line {i + 1}:\n{line}'
                )
            meanings = wrap_meanings(split[1])
            vocab: vocabs_t = {"word": split[0], "meaning": meanings}

            vocabs_list.append(vocab)

    if len(vocabs_list) == 0:
        raise Exception("Vocabs list is empty")
    return vocabs_list


def load_yml(path: str) -> vocabs_list_t:
    with open(path, encoding="utf-8") as f:
        file_contents = yaml.load(f, Loader)
    vocabs_list: vocabs_list_t = [
        {
            "word": item["word"],
            "meaning": wrap_meanings(item["definition"]),
        }
        for item in file_contents
    ]
    return vocabs_list


def load_from_file(path: str) -> vocabs_list_t:
    if path.split(".")[-1] == "yml":
        return load_yml(path)
    else:
        return load_text(path)


def load_from_dir(path: str) -> tuple[vocabs_list_t, path_list_t]:
    vocabs_list: vocabs_list_t = []
    path_list: path_list_t = glob(os.path.join(path, "*.*"))
    path_list.sort()

    if len(path_list) == 0:
        raise Exception(f'The directory: "{path}" is empty')

    vocabs_list = []
    for path in path_list:
        vocabs_list.extend(load_from_file(path))
    return (vocabs_list, path_list)


def load_vocabs(path: str) -> tuple[vocabs_list_t, path_list_t, int, int]:
    vocabs_list: vocabs_list_t = []
    path_list: path_list_t = []
    if os.path.isdir(path):
        vocabs_list, path_list = load_from_dir(path)
    else:
        path_list.append(path)
        vocabs_list = load_from_file(path)

    random.shuffle(vocabs_list)
    vocabs_list_len: int = len(vocabs_list)
    path_list_len: int = len(path_list)
    return (vocabs_list, path_list, vocabs_list_len, path_list_len)
