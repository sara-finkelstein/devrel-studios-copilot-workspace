import argparse
import re
import subprocess
import time

from pywinauto import Desktop


APP_ID = r"shell:AppsFolder\Microsoft.Todos_8wekyb3d8bbwe!App"


def get_window(timeout_seconds: int = 30):
    desktop = Desktop(backend="uia")
    window = desktop.window(title="Microsoft To Do")

    if not window.exists():
        subprocess.run(
            ["explorer.exe", APP_ID],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        if window.exists() and window.is_visible():
            return window
        time.sleep(1)

    raise RuntimeError("Microsoft To Do did not become available.")


def select_list(window, list_name: str):
    pattern = rf"^{re.escape(list_name)}(?:,|$)"
    list_item = window.child_window(
        title_re=pattern,
        control_type="ListItem",
    )

    if not list_item.exists():
        raise RuntimeError(f'To Do list "{list_name}" was not found.')

    list_item.select()

    deadline = time.time() + 10
    heading_pattern = rf"^{re.escape(list_name)} selected, Rename list$"
    while time.time() < deadline:
        if window.child_window(
            title_re=heading_pattern,
            control_type="Button",
        ).exists():
            return
        time.sleep(0.5)

    raise RuntimeError(f'To Do list "{list_name}" did not open.')


def get_add_task_edit(window):
    edits = [
        edit
        for edit in window.descendants(control_type="Edit")
        if edit.is_visible()
        and edit.is_enabled()
        and edit.rectangle().left > window.rectangle().left + 400
    ]

    if not edits:
        raise RuntimeError("The Add task field was not found.")

    return max(edits, key=lambda edit: edit.rectangle().top)


def add_task(list_name: str, title: str, due: str | None):
    window = get_window()
    select_list(window, list_name)

    task_text = title.strip()
    if due:
        task_text = f"{task_text} by {due.strip()}"

    add_task_edit = get_add_task_edit(window)
    add_task_edit.set_edit_text(task_text)
    add_task_edit.type_keys("{ENTER}")

    deadline = time.time() + 10
    task_pattern = rf"^Task {re.escape(title.strip())}(?:,|$)"
    while time.time() < deadline:
        if window.child_window(
            title_re=task_pattern,
            control_type="ListItem",
        ).exists():
            print(f'Created "{title}" in "{list_name}".')
            return
        time.sleep(0.5)

    raise RuntimeError("The task could not be verified after creation.")


def main():
    parser = argparse.ArgumentParser(
        description="Append a task to an existing Microsoft To Do list."
    )
    parser.add_argument("--list", required=True, dest="list_name")
    parser.add_argument("--title", required=True)
    parser.add_argument("--due")
    args = parser.parse_args()

    add_task(args.list_name, args.title, args.due)


if __name__ == "__main__":
    main()
