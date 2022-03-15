import os

from render.workspace_renderer import WorkspaceRenderer
from utils.storage import Storage


def main():
    # el = EventLoop(STORAGE_PATH)
    # el.loop()

    s = Storage('./src/data/workspaces.json')

    wr = WorkspaceRenderer(s.data["workspaces"][0])
    wr.render()


if __name__ == '__main__':
    main()
