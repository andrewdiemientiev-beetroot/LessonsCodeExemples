import requests
import time

def get_classes():
    resp = requests.get('https://www.dnd5eapi.co/api/classes/')
    return resp.text


def get_spells():
    resp = requests.get('https://www.dnd5eapi.co/api/spells/')
    return resp.text


def write_to_file(filename, text):
    with open(filename, mode='w') as file:
        file.write(text)


if __name__ == '__main__':
    classes = get_classes()
    spells = get_spells()
    write_to_file('sync_classes.txt', classes)
    write_to_file('sync_spells.txt', spells)

    print(f"Time consumed {time.perf_counter()}")