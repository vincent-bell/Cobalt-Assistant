from json import loads, JSONDecodeError


def parse_ljson(file: str = "Cobalt/lesson.json"):
    with open(file, 'r') as f:
        file_contents = f.read()
    data = loads(file_contents)
    if type(data) == list:
        return data
    else:
        raise JSONDecodeError("Expecting an array of json objects in 'lesson.json'...")
