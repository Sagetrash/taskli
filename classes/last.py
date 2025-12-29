import json_helpers as j

def lastId():
    try:
        last = j.openJson()[-1].taskdict["id"]
    except IndexError as e:
        last = 0

    return 