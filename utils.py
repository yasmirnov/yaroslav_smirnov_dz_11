import json

CANDIDATES_FILE = "candidates.json"


def load_candidates() -> list[dict]:
    """
    загружает данные из файла
    """
    with open(CANDIDATES_FILE, "r") as file:
        return json.load(file)


def get_candidates_all():
    return load_candidates()


def get_candidate(id):
    """
    получает кандидата по id
    """
    for candidate in load_candidates():
        if int(id) == candidate["id"]:
            return candidate
    return 'Not Found'


def get_candidate_by_name(name):
    """
    получает кандидата по имени
    """
    candidates = []
    for candidate in load_candidates():
        if name.lower() in candidate["name"].lower():
            candidates.append(candidate)
    return candidates


def get_candidate_by_skill(skill) -> list:
    """
    получает кандидата по навыку
    """
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate["skills"].lower().split(', '):
            candidates.append(candidate)
    return candidates
