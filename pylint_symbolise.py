#!/usr/bin/env python
import pylint.lint
import sys

linter = pylint.lint.PyLinter()
linter.load_defaults()
linter.load_default_plugins()

MAPPING = {msg.msgid: msg.symbol for msg in linter.messages}


def multipleReplace(text, wordDict):
    for key in wordDict:
        text = text.replace(key, wordDict[key])
    return text


def replace_list_msgs(text):
    return multipleReplace(text, MAPPING)


def replace_in_files(file_names):
    for file_name in file_names:
        with open(file_name, 'r') as f:
            replaced = replace_list_msgs(f.read())
        with open(file_name, 'w') as f:
            f.write(replaced)

if __name__ == "__main__":
    replace_in_files(sys.argv[1:])

