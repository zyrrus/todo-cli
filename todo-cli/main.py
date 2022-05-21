from runtime.display_manager import DisplayManager


def main():
    dm = DisplayManager()
    dm.run_tui('todo.md')


if __name__ == '__main__':
    main()
