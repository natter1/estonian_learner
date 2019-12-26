"""

"""

# class Word:
#     pass


class Conjugations:
    def __init__(self):
        self.person = {}

        self.negative = ("", "")
        self.passive = ("", "")
        self.passive_negative = ("", "")

    def summary(self):
        result = ""
        sep = "  "
        for i in range(1, 7):
            result += sep.join([f"{i}P", self.person[i][0], self.person[i][1]]) + "\n"
        result += sep.join(["negative", self.negative[0], self.negative[1]]) + "\n"
        result += sep.join(["passive", self.passive[0], self.passive[1]]) + "\n"
        result += sep.join(["passive negative", self.passive_negative[0], self.passive_negative[1]]) + "\n"
        return result

    def add_person(self, original, translation, index):
        self.person[index] = original
        self.person_translation[index] = translation


class Verb:
    def __init__(self):
        self.infinitive_ma = ("", "")
        self.infinitive_da = ("", "")
        self.past_active_participle = ("", "")
        self.past_passive_participle = ("", "")

        self.present = Conjugations()
        self.conditional_mood = Conjugations()
        self.imperative_mood = Conjugations()
        self.imperative_negative_mood = Conjugations()

        self.perfect = Conjugations()
        self.past = Conjugations()
        self.plusperfect = Conjugations()
        self.conditional_perfect_mood = Conjugations()

        self.quotative = Conjugations()
        self.quotative_perfect = Conjugations()
        self.jussive = Conjugations()
        self.jussive_perfect = Conjugations()

        self.other = {}

        self.usage_info = ""

    def get_summary(self):
        result = "\n---------------------------------------------------------"

        result += "\nUsage info:\n"
        result += self.usage_info + "\n"

        result += "\nInfinitive (-ma  -da  translation)\n"
        result += self.infinitive_ma[0] + "  " + self.infinitive_da[0] + "  " + self.infinitive_ma[1] + "\n"

        result += "\nPast active participle\n"
        result += self.past_active_participle[0] + "  " + self.past_active_participle[1] + "\n"

        result += "\nPast passive participle\n"
        result += self.past_passive_participle[0] + "  " + self.past_passive_participle[1] + "\n"

        result += "\nPresent tense\n"
        result += self.present.summary()

        result += "\nConditional mood\n"
        result += self.conditional_mood.summary()

        result += "\nImperative mood\n"
        result += self.imperative_mood.summary()

        result += "\nImperative negative mood\n"
        result += self.imperative_negative_mood.summary()

        result += "\nPerfect tense\n"
        result += self.perfect.summary()

        result += "\nPast tense\n"
        result += self.past.summary()

        result += "\nPlusperfect tense\n"
        result += self.plusperfect.summary()

        result += "\nConditional perfect mood\n"
        result += self.conditional_perfect_mood.summary()

        result += "\nQuotative tense\n"
        result += self.quotative.summary()

        result += "\nQuotative perfect tense\n"
        result += self.quotative_perfect.summary()

        result += "\nJussive tense\n"
        result += self.jussive.summary()

        result += "\nJussive perfect tense\n"
        result += self.jussive_perfect.summary()

        result += "\nOther\n"
        for key in self.other:
            result += key + "  " + self.other[key][0] + "  " + self.other[key][1] + "\n"

        result += "---------------------------------------------------------\n"
        return result
