from utilities.markdown import markdown_to_workspace, workspace_to_markdown


def announce(text):
    text = f" {text} "
    print(f"\n{text:=^40}")


def main():
    ws = markdown_to_workspace("/home/zyrrus/dev/todo-cli/test.md")

    inp = ""
    while inp != 'q':
        announce("")
        print(ws)
        inp = input("$> ")

        ls = ws.get_selected()
        ts = ls.get_selected()

        if inp == 'w':
            ls.select_up()
        elif inp == 'a':
            ls.select_left()
        elif inp == 's':
            ls.select_down()
        elif inp == 'd':
            ls.select_right()
        elif inp == 'z':
            ws.select_left()
        elif inp == 'x':
            ws.select_right()


if __name__ == '__main__':
    main()
