"""
This module helps to read estonian verbs with all forms into the corresponding objects.
A fitting source has to be included into ..\\resources\\vocabs_source.txt All functions have to be
customized to the given source.
A Source could be e.g.:
http://www.eki.ee/dict/psv/index.cgi
https://en.wiktionary.org/wiki/olema#Estonian

@author: Nathanael Jöhrmann
@license: MIT
"""

import json
import os

import requests
from bs4 import BeautifulSoup, SoupStrainer

from data_sqlalchemy import estonian_database
from data_sqlalchemy.db_session import DbSession
from data_sqlalchemy.verb_db import VerbDB
from estonian_learner.verb import Conjugations
from estonian_learner.verb import Verb

list_of_missing_verbs = [
    "lõppema",
]

list_of_verbs = [
    "olema",
    "algama",
    "avama",
    "juhtuma",
    "minema",
    "tõmbuma"
]

db_file = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "db",
        "estonian.sqlite"
    ))


def get_verbs_from_database() -> list:
    estonian_database.create(db_file)

    session = DbSession.factory()
    result = session.query(VerbDB).all()
    session.commit()

    return result

def get_verb_from_database(ma_infinitive: str):
    pass  # todo

def add_to_database(my_verbs):

    estonian_database.create(db_file)

    session = DbSession.factory()
    for verb in my_verbs:
        session.merge(verb)

    # use only, when all my_verbs entries do not exist in database (Unique Constraint!)
    # session.add_all(my_verbs)

    session.commit()


def main():
    my_verbs = []
    for verb in list_of_verbs[5:]:  # todo: [0:1] only for testing!
        my_verbs.append(get_verbdb(verb))
    for verb in my_verbs:
        print(verb.summary)

    add_to_database(my_verbs)


def get_verbdb(verb: str):
    url = get_data_source_url() + verb
    # url = "https://en.wiktionary.org/wiki/olema#Estonian"
    # url = "https://www.eki.ee/litsents/idkaart/dl.cgi?D=psv%2Fhaaldused"
    req = requests.get(url)
    parse_only = SoupStrainer(id=get_id_list())
    soup = BeautifulSoup(req.text, "html.parser", parse_only=parse_only)
    # print(soup.prettify())
    # my_verb = read_to_verb(soup)
    my_verb = read_to_verbdb(soup)
    return my_verb


def get_data_source_url() -> str:
    source_vocabs = "..\\resources\\vocabs_source.txt"  # file containing a source for the vocabs and their forms
    with open(source_vocabs, 'r') as myfile:
        result = myfile.read()
    return result


def get_id_list() -> list:
    """
    Gets a list with all ids. Using this list with parse_only reduces soup-size and more importantly,
    it allows to use: 'recursive = False' in soup.find(), giving a huge speed up.
    :return: List of ids for use with parse_only
    """
    suffix_list = ["1", "2", "3", "4", "5", "6", "_neg", "PASS", "PASS_neg"]
    tense_list = ["present{}", "conditional{}", "imperative{}", "imperative{}_neg",
                  "perfect{}", "past{}", "pluperfect{}", "conditional_perfect{}",
                  "quotative{}", "quotative_perfect{}", "jussive{}", "jussive_perfect{}"]

    def add_conjugations_ids(_tense: str):
        for s in suffix_list:
            result.append(_tense.format(s))

    result = []
    for tense in tense_list:
        add_conjugations_ids(tense)

    result.append("usage-info")
    result.append("ma_infinitive")
    result.append("da_infinitive")
    result.append("participle_past_active")
    result.append("participle_past_passive")
    result.append("quotative")
    result.append("quotative_perfect")
    result.append("jussive")
    result.append("jussive_perfect")
    result.append("des_form")
    result.append("ma_inessive")
    result.append("ma_elative")
    result.append("ma_translative")
    result.append("ma_abessive")
    result.append("participle_present_active")
    result.append("participle_present_passive")
    return result


def read_to_verbdb(soup: BeautifulSoup):
    my_verb: VerbDB = VerbDB()

    read_infinitivesdb(soup, my_verb)
    read_participlesdb(soup, my_verb)

    my_verb.present = get_conjugations(soup, "present{}").to_json()
    my_verb.conditional_mood = get_conjugations(soup, "conditional{}").to_json()
    my_verb.imperative_mood = get_conjugations(soup, "imperative{}").to_json()
    my_verb.imperative_negative_mood = get_conjugations(soup, "imperative{}_neg").to_json()

    my_verb.perfect = get_conjugations(soup, "perfect{}").to_json()
    my_verb.past = get_conjugations(soup, "past{}").to_json()
    my_verb.plusperfect = get_conjugations(soup, "pluperfect{}").to_json()
    my_verb.conditional_perfect_mood = get_conjugations(soup, "conditional_perfect{}").to_json()

    my_verb.quotative = get_conjugations(soup, "quotative{}").to_json()
    my_verb.quotative["person"]["3"] = read_form_and_translation(soup, "quotative")
    my_verb.quotative_perfect = get_conjugations(soup, "quotative_perfect{}").to_json()
    my_verb.quotative_perfect["person"]["3"] = read_form_and_translation(soup, "quotative_perfect")

    my_verb.jussive = get_conjugations(soup, "jussive{}").to_json()
    my_verb.jussive["person"]["3"] = read_form_and_translation(soup, "jussive")

    my_verb.jussive_perfect = get_conjugations(soup, "jussive_perfect{}").to_json()
    my_verb.jussive_perfect["person"]["3"] = read_form_and_translation(soup, "jussive_perfect")

    other = {"des_form": read_form_and_translation(soup, "des_form"),
             "ma_inessive": read_form_and_translation(soup, "ma_inessive"),
             "ma_elative": read_form_and_translation(soup, "ma_elative"),
             "ma_translative": read_form_and_translation(soup, "ma_translative"),
             "ma_abessive": read_form_and_translation(soup, "ma_abessive"),
             "participle_present_active": read_form_and_translation(soup, "participle_present_active"),
             "participle_present_passive": read_form_and_translation(soup, "participle_present_passive")}

    my_verb.other = json.loads(json.dumps(other, indent=2, ensure_ascii=False))

    soup_usage = soup.find("div", {"id": "usage-info"})
    if hasattr(soup_usage, "text"):
        my_verb.usage_info = soup_usage.text

    return my_verb


def read_form_and_translation(soup: BeautifulSoup, _id) -> list:
    form = ""
    translation = ""
    form_soup = soup.find("div", {"id": _id}, recursive=False)
    if hasattr(form_soup, "find"):
        form = form_soup.find("div", {"class": "meta-form"}).text
        translation = form_soup.find("div", {"class": "meta-translation"}).text
    return [form, translation]


def read_infinitivesdb(soup: BeautifulSoup, verb):
    verb.infinitive_ma = read_form_and_translation(soup, "ma_infinitive")[0]
    verb.infinitive_da = read_form_and_translation(soup, "da_infinitive")[0]

    verb.infinitive_ma_english = read_form_and_translation(soup, "ma_infinitive")[1]
    verb.infinitive_da_english = read_form_and_translation(soup, "da_infinitive")[1]


def read_participlesdb(soup: BeautifulSoup, verb: VerbDB):
    verb.past_active_participle = read_form_and_translation(soup, "participle_past_active")[0]
    verb.past_passive_participle = read_form_and_translation(soup, "participle_past_passive")[0]

    verb.past_active_participle_english = read_form_and_translation(soup, "participle_past_active")[1]
    verb.past_passive_participle_english = read_form_and_translation(soup, "participle_past_passive")[1]


def read_to_verb(soup: BeautifulSoup):
    my_verb: Verb = Verb()

    read_infinitives(soup, my_verb)
    read_participles(soup, my_verb)

    my_verb.present = get_conjugations(soup, "present{}")
    my_verb.conditional_mood = get_conjugations(soup, "conditional{}")
    my_verb.imperative_mood = get_conjugations(soup, "imperative{}")
    my_verb.imperative_negative_mood = get_conjugations(soup, "imperative{}_neg")

    my_verb.perfect = get_conjugations(soup, "perfect{}")
    my_verb.past = get_conjugations(soup, "past{}")
    my_verb.plusperfect = get_conjugations(soup, "pluperfect{}")
    my_verb.conditional_perfect_mood = get_conjugations(soup, "conditional_perfect{}")

    my_verb.quotative = get_conjugations(soup, "quotative{}")
    my_verb.quotative.person[3] = read_form_and_translation(soup, "quotative")
    my_verb.quotative_perfect = get_conjugations(soup, "quotative_perfect{}")
    my_verb.quotative_perfect.person[3] = read_form_and_translation(soup, "quotative_perfect")

    my_verb.jussive = get_conjugations(soup, "jussive{}")
    my_verb.jussive.person[3] = read_form_and_translation(soup, "jussive")
    my_verb.jussive_perfect = get_conjugations(soup, "jussive_perfect{}")
    my_verb.jussive_perfect.person[3] = read_form_and_translation(soup, "jussive_perfect")

    my_verb.other["des_form"] = read_form_and_translation(soup, "des_form")
    my_verb.other["ma_inessive"] = read_form_and_translation(soup, "ma_inessive")
    my_verb.other["ma_elative"] = read_form_and_translation(soup, "ma_elative")
    my_verb.other["ma_translative"] = read_form_and_translation(soup, "ma_translative")
    my_verb.other["ma_abessive"] = read_form_and_translation(soup, "ma_abessive")
    my_verb.other["participle_present_active"] = read_form_and_translation(soup, "participle_present_active")
    my_verb.other["participle_present_passive"] = read_form_and_translation(soup, "participle_present_passive")

    soup_usage: BeautifulSoup.element.Tag = soup.find("div", {"id": "usage-info"})
    if hasattr(soup_usage, "text"):
        my_verb.usage_info = soup_usage.text

    return my_verb


def read_infinitives(soup: BeautifulSoup, verb: Verb):
    verb.infinitive_ma = read_form_and_translation(soup, "ma_infinitive")
    verb.infinitive_da = read_form_and_translation(soup, "da_infinitive")


def read_participles(soup: BeautifulSoup, verb: Verb):
    verb.past_active_participle = read_form_and_translation(soup, "participle_past_active")
    verb.past_passive_participle = read_form_and_translation(soup, "participle_past_passive")


def get_conjugations(soup: BeautifulSoup, _id) -> Conjugations:
    result = Conjugations()
    for i in range(1, 7):
        result.person[i] = read_form_and_translation(soup, _id.format(i))
        # # form_soup = soup.find("div", {"id": f"{id}{i}"})
        # form_soup = soup.find("div", {"id": id.format(i)})
        # if form_soup:
        #     verb_form = form_soup.find("div", {"class": "meta-form"})
        #     translation = form_soup.find("div", {"class": "meta-translation"})
        #
        #     result.person[i] = verb_form, translation
        #     # result.add_person(verb_form.text, translation.text, i)

    result.negative = read_form_and_translation(soup, _id.format("_neg"))
    result.passive = read_form_and_translation(soup, _id.format("PASS"))
    result.passive_negative = read_form_and_translation(soup, _id.format("PASS_neg"))

    # # PASS_neg
    # form_soup = soup.find("div", {"id": id.format("PASS_neg")})
    # if form_soup:
    #     result.passive_negative = form_soup.find("div", {"class": "meta-form"}).text
    #     result.passive_negative_translation = form_soup.find("div", {"class": "meta-translation"}).text

    return result


if __name__ == "__main__":
    main()
