from typing import TypedDict


vocabs_t = TypedDict(
    "vocab",
    {
        "word": str,
        "meaning": list[str],
        "marked": bool,
        "to_export": str,
    },
    total=False,
)
vocabs_list_t = list[vocabs_t]
path_list_t = list[str]
