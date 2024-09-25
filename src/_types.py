from typing import TypedDict


vocabs_t = TypedDict(
    "vocab",
    {
        "word": str,
        "meaning": list[str],
    },
    total=False,
)
vocabs_list_t = list[vocabs_t]
path_list_t = list[str]
