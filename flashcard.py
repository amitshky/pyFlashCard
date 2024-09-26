import sys
import random
import pyray as rl
from src.loaders import load_vocabs
from src._types import vocabs_list_t, path_list_t


def main():
    try:
        if len(sys.argv) == 2:
            path: str = sys.argv[1]
        elif len(sys.argv) > 2:
            raise Exception("Invalid number of arguments provided!")
        else:
            path: str = "lists/"

        vocabs_list: vocabs_list_t = []
        path_list: path_list_t = []
        vocabs_list, path_list, vocabs_list_len, path_list_len = load_vocabs(path)
    except Exception as error:
        print(error)
        return

    index: int = 0  # index of the current word
    file_index: int = 0  # index of the current file

    rl.set_config_flags(rl.FLAG_WINDOW_RESIZABLE)
    rl.init_window(1200, 800, "Flash card")
    rl.set_window_title(f"{path_list[file_index]} - Flash Card")
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
            rl.GREEN,
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
            for i, meaning in enumerate(vocabs_list[index]["meaning"]):
                rl.draw_text_ex(
                    FONT_ITALIC,
                    meaning,
                    rl.Vector2(10, (i + 1) * FONT_SIZE_HEADER + 10),
                    FONT_SIZE_BODY,
                    0.2,
                    rl.GRAY,
                )

        # next file (if directory is provided in the args)
        elif rl.is_key_pressed(rl.KEY_N) and path_list_len > 1:
            file_index = (file_index + 1) % path_list_len
            rl.set_window_title(f"{path_list[file_index]} - Flash Card")
            vocabs_list, _, vocabs_list_len, _ = load_vocabs(path_list[file_index])
            index = 0

        # previous file (if directory is provided in the args)
        elif rl.is_key_pressed(rl.KEY_P) and path_list_len > 1:
            file_index = (file_index - 1) % path_list_len
            rl.set_window_title(f"{path_list[file_index]} - Flash Card")
            vocabs_list, _, vocabs_list_len, _ = load_vocabs(path_list[file_index])
            index = 0

        rl.end_drawing()

    rl.unload_font(FONT)
    rl.unload_font(FONT_ITALIC)
    rl.close_window()


if __name__ == "__main__":
    main()
