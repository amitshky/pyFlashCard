import sys
import random
import pyray as rl


def load_vocabs(path: str) -> list[dict[str, str]]:
    vocabs_list: list[dict[str, str]] = []

    with open(path) as f:
        for i, line in enumerate(f):
            split: list[str] = line.split(" - ")
            if len(split) != 2:
                raise Exception(f"ERROR in file: \"{path}\"\nWrong format on line {i + 1}:\n{line}")

            vocab: dict[str, str] = {"word": split[0], "meaning": split[1]}
            vocabs_list.append(vocab)

    if len(vocabs_list) == 0:
        raise Exception("Vocabs list is empty")

    return vocabs_list


def main():
    try:
        if (len(sys.argv) == 2):
            path: str = sys.argv[1]
        elif (len(sys.argv) > 2):
            raise Exception("Invalid number of arguments provided!")
        else:
            path: str = "lists/vocabs.md"
        vocabs_list: list[dict[str, str]] = load_vocabs(path)
    except Exception as error:
        print(error)
        return

    random.shuffle(vocabs_list)
    vocabs_list_len: int = len(vocabs_list)
    index: int = 0  # index of the current word

    rl.set_config_flags(rl.FLAG_WINDOW_RESIZABLE)
    rl.init_window(1200, 800, "Flash card")
    rl.set_exit_key(rl.KEY_Q)
    FONT: rl.Font = rl.load_font("fonts/CONSOLA.TTF")
    FONT_ITALIC: rl.Font = rl.load_font("fonts/Consolas.ttf")

    while not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.BLACK)



        FONT_SIZE_HEADER: int = 40
        FONT_SIZE_BODY: int = 30
        rl.draw_text_ex(
            FONT,
            f'{index + 1}. {vocabs_list[index]["word"]}',
            rl.Vector2(10, 10),
            FONT_SIZE_HEADER,
            0.2,
            rl.GREEN
        )

        # next word
        if rl.is_key_pressed(rl.KEY_J) or rl.is_key_pressed_repeat(rl.KEY_J):
            index = (index + 1) % vocabs_list_len

        # previous word
        elif rl.is_key_pressed(rl.KEY_K) or rl.is_key_pressed_repeat(rl.KEY_K):
            # negative indexing works in python
            index = (index - 1) % vocabs_list_len

        elif rl.is_key_pressed(rl.KEY_H):  # first word
            index = 0

        elif rl.is_key_pressed(rl.KEY_L):  # last word
            index = vocabs_list_len - 1

        elif rl.is_key_pressed(rl.KEY_R):  # randomize the list
            random.shuffle(vocabs_list)

        elif rl.is_key_pressed(rl.KEY_S):  # sort the list
            vocabs_list = sorted(vocabs_list, key=lambda vocab: vocab["word"])

        elif rl.is_key_down(rl.KEY_SPACE):  # unhide the meanings of the words
            MAX_CHAR: int = 50
            WRAP_NUM: int = len(vocabs_list[index]["meaning"]) // MAX_CHAR
            if (WRAP_NUM >= 1):  # string wrapping
                for i in range(WRAP_NUM + 1):
                    rl.draw_text_ex(
                        FONT_ITALIC,
                        vocabs_list[index]["meaning"][i * MAX_CHAR:(i + 1) * MAX_CHAR],
                        rl.Vector2(10, (i + 1) * FONT_SIZE_HEADER + 10),
                        FONT_SIZE_BODY,
                        0.2,
                        rl.GRAY
                    )
            else:
                rl.draw_text_ex(
                    FONT_ITALIC,
                    vocabs_list[index]["meaning"],
                    rl.Vector2(10, FONT_SIZE_HEADER + 10),
                    FONT_SIZE_BODY,
                    0.2,
                    rl.GRAY
                )

        rl.end_drawing()

    rl.unload_font(FONT)
    rl.unload_font(FONT_ITALIC)
    rl.close_window()


if __name__ == "__main__":
    main()
