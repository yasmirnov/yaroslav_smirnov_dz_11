from flask import Flask, request, render_template
import utils

app = Flask(__name__)


@app.route("/")
def index():
    """
    все кандидаты
    """
    candidates = utils.get_candidates_all()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:id>")
def get_candidate(id):
    """
    кандидат
    """
    candidate = utils.get_candidate(id)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<name>")
def get_candidate_by_name(name):
    """
    поиск по имени
    """
    candidates = utils.get_candidate_by_name(name)
    return render_template('search.html', candidates=candidates, count=len(candidates))


@app.route("/skills/<skill>")
def get_candidate_by_skill(skill):
    """
    поиск по навыку
    """
    candidates = utils.get_candidate_by_skill(skill)
    return render_template('skill.html', candidates=candidates, skill=skill, count=len(candidates))


if __name__ == "__main__":
    app.run()
