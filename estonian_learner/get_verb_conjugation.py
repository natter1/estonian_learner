"""
This module helps to read estonian vocabs with all forms into the corresponding objects.
A fitting source has to be included into ..\\resources\\vocabs_source.txt All functions have to be
customized to the given source.
A Source could be e.g.:
http://www.eki.ee/dict/psv/index.cgi
https://en.wiktionary.org/wiki/olema#Estonian
"""
from bs4 import BeautifulSoup
import requests
from estonian_learner.verb import Verb
from estonian_learner.verb import Conjugations

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


def main():
    my_verbs = []
    source_vocabs = "..\\resources\\vocabs_source.txt"  # file containing a source for the vocabs and their forms
    with open(source_vocabs, 'r') as myfile:
        source = myfile.read()

    for verb in list_of_verbs:
        url = source + verb
        url = "https://en.wiktionary.org/wiki/olema#Estonian"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        print(soup)
        my_verb: Verb = Verb()

        read_infinitives(soup, my_verb)
        read_participles(soup, my_verb)

        my_verb.present = read_conjugations(soup, "present{}")
        my_verb.conditional_mood = read_conjugations(soup, "conditional{}")
        my_verb.imperative_mood = read_conjugations(soup, "imperative{}")
        my_verb.imperative_negative_mood = read_conjugations(soup, "imperative{}_neg")

        my_verb.perfect = read_conjugations(soup, "perfect{}")
        my_verb.past = read_conjugations(soup, "past{}")
        my_verb.plusperfect = read_conjugations(soup, "pluperfect{}")
        my_verb.conditional_perfect_mood = read_conjugations(soup, "conditional_perfect{}")

        my_verb.quotative = read_conjugations(soup, "quotative{}")
        my_verb.quotative.person[3] = read_form_and_translation(soup, "quotative")
        my_verb.quotative_perfect = read_conjugations(soup, "quotative_perfect{}")
        my_verb.quotative_perfect.person[3] = read_form_and_translation(soup, "quotative_perfect")

        my_verb.jussive = read_conjugations(soup, "jussive{}")
        my_verb.jussive.person[3] = read_form_and_translation(soup, "jussive")
        my_verb.jussive_perfect = read_conjugations(soup, "jussive_perfect{}")
        my_verb.jussive_perfect.person[3] = read_form_and_translation(soup, "jussive_perfect")

        my_verb.other["des_form"] = read_form_and_translation(soup, "des_form")
        my_verb.other["ma_inessive"] = read_form_and_translation(soup, "ma_inessive")
        my_verb.other["ma_elative"] = read_form_and_translation(soup, "ma_elative")
        my_verb.other["ma_translative"] = read_form_and_translation(soup, "ma_translative")
        my_verb.other["ma_abessive"] = read_form_and_translation(soup, "ma_abessive")
        my_verb.other["participle_present_active"] = read_form_and_translation(soup, "participle_present_active")
        my_verb.other["participle_present_passive"] = read_form_and_translation(soup, "participle_present_passive")


        soup_usage = soup.find("div", {"id": "usage-info"})
        if soup_usage:
            my_verb.usage_info = soup_usage.text

        my_verbs.append(my_verb)

    for verb in my_verbs:
        print(verb.get_summary())
    # print(my_verbs)



def read_form_and_translation(soup, id):
    form = ""
    translation = ""
    form_soup = soup.find("div", {"id": id})
    if form_soup:
        form = form_soup.find("div", {"class": "meta-form"}).text
        translation = form_soup.find("div", {"class": "meta-translation"}).text
    return form, translation


def read_infinitives(soup, verb):
    verb.infinitive_ma = read_form_and_translation(soup, "ma_infinitive")
    verb.infinitive_da = read_form_and_translation(soup, "da_infinitive")


def read_participles(soup, verb):
    verb.past_active_participle = read_form_and_translation(soup, "participle_past_active")
    verb.past_passive_participle = read_form_and_translation(soup, "participle_past_passive")


def read_conjugations(soup, id):
    result = Conjugations()
    for i in range(1, 7):
        result.person[i] = read_form_and_translation(soup, id.format(i))
        # # form_soup = soup.find("div", {"id": f"{id}{i}"})
        # form_soup = soup.find("div", {"id": id.format(i)})
        # if form_soup:
        #     verb_form = form_soup.find("div", {"class": "meta-form"})
        #     translation = form_soup.find("div", {"class": "meta-translation"})
        #
        #     result.person[i] = verb_form, translation
        #     # result.add_person(verb_form.text, translation.text, i)

    result.negative = read_form_and_translation(soup, id.format("_neg"))
    result.passive = read_form_and_translation(soup, id.format("PASS"))
    result.passive_negative = read_form_and_translation(soup, id.format("PASS_neg"))

    # # PASS_neg
    # form_soup = soup.find("div", {"id": id.format("PASS_neg")})
    # if form_soup:
    #     result.passive_negative = form_soup.find("div", {"class": "meta-form"}).text
    #     result.passive_negative_translation = form_soup.find("div", {"class": "meta-translation"}).text

    return result


if __name__ == "__main__":
    main()

