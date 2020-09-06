# Logkeys Count

A simple Python tool to analyze your logkeys keylogger file and print it in a ASCII keyboard to show which keys you press more. This is designed to ultimately be similar to the program "wakatime" but without any cloud component.

## Usage

`./logkeys-count.py path/to/logkeys/log`

You may need root access if your logkeys log is using the standard 600 permissions so it's not world-readable.

## Keymaps

In order to have a better keymap for your particular keyboard layout, you can add a new layout in the `layouts` folder (If you do this please submit a PR!).

Currently, it will default to the `en_US-apple` layout.

If you wish to use a non-default layout, you can specify the layout by name: `./logkeys-count.py path/to/log layout-name`
