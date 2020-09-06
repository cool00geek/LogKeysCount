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


def pretty_print(keys):
    text = """
. -----------------------------------------------------------------------------------------------------------------------------------------------------------.
| [_Esc_] [_F1__][_F2__][_F3__][_F4__][_F5__][_F6__][_F7__][_F8__][_F9__][_F10_][_F11_][_F12_]            [PrtSc][ScrLk][Pause]                              |
|                                                                                                                                                            |
| [__`__][__1__][__2__][__3__][__4__][__5__][__6__][__7__][__8__][__9__][__0__][__-__][__=__][BckSp]      [_Ins_][Home_][PgUp_]  [NumLk][  =  ][_KP/_][_KP*_]|
| [_Tab_][__q__][__w__][__e__][__r__][__t__][__y__][__u__][__i__][__o__][__p__][__[__][__]__][__\__]      [_Del_][_End_][PgDn_]  [_KP7_][_KP8_][_KP9_][_KP+_]|
| [CpsLk][__a__][__s__][__d__][__f__][__g__][__h__][__j__][__k__][__l__][__;__][__'__]       [Enter]                             [_KP4_][_KP5_][_KP6_][_KP-_]|
| [LShft][__z__][__x__][__c__][__v__][__b__][__n__][__m__][__,__][__.__][__/__]              [RShft]             [_Up__]         [_KP1_][_KP2_][_KP3_]       |
| [LCtrl][LAlt_][LMeta][                        Space                         ][RMeta][AltGr][RCtrl]      [Left_][Down_][Right]  [       _KP0_][_KP._][KPEnt]|
`------------------------------------------------------------------------------------------------------------------------------------------------------------'
"""
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

    for k,v in char_count.items():
        #print("{}\t{}".format(k,v))
        pass
    pretty_print(char_count)

main()