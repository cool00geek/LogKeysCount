#!/usr/bin/env python3

import sys

def replace(key):
    if "<" in key:
        key = key.replace("<", "")
    if ">" in key:
        key = key.replace(">", "")
    key_sub = {
        "~":"`",
        "!":"1",
        "@":"2",
        "#":"3",
        "$":"4",
        "%":"5",
        "^":"6",
        "&":"7",
        "*":"8",
        "(":"9",
        ")":"0",
        "_":"-",
        "+":"=",
        "{":"[",
        "}":"]",
        "|":"\\",
        ":":";",
        "\"":"'",
        "<":",",
        ">":".",
        "?":"/",
        " ":"Space"
    }
    return key_sub.get(key, key)

def pad_key(key):
    front = ""
    back = ""
    if len(key) <= 4:
        back += "_"
    if len(key) <= 3:
        front += "_"
    if len(key) <= 2:
        back += "_"
    if len(key) <= 1:
        front += "_"
    return front + key + back

def pad_value(val):
    if val > 99999:
        return "2Many"
    value = str(val)
    while len(value) != 5:
        value = " " + value
    return value


def pretty_print(keys, layout="layouts/en_US-apple"):
    with open(layout, "r") as f:
        text = ''.join(f.readlines())
    print(text)
    total = 0
    max_key = ''
    max_presses = 0
    for k,v in keys.items():
        if v > max_presses:
            max_presses = v
            max_key = k
        key = pad_key(k)
        total += v
        val = pad_value(v)
        text = text.replace(key, val)
    print(text)
    print("Total keypresses: {}".format(total))
    print("You use {} the most, with {} presses!".format(max_key, max_presses))

def main():
    char_count = dict()
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        for line in f.readlines():
            if ">" not in line:
                continue
            line = line[line.find(">")+2:].strip()
            while len(line) != 0:
                if line[0] == '<':
                    end_key = line.find(">")
                    char = line[1:end_key]
                    line = line[end_key+1:]
                else:
                    char = line[0]
                    line = line[1:]
                char = replace(char)
                char_count[char] = char_count.get(char, 0) + 1

    if len(sys.argv) >= 3:
        pretty_print(char_count, "layouts/" + sys.argv[2])
    else:
        pretty_print(char_count)

main()
