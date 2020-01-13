from pyvabamorf.morf import Vabamorf
from pyvabamorf.morf import analyze, synthesize
# from pprint import pprint
# pprint(analyze('Tüünete öötööde allmaaraudteejaam'))
my_vab: Vabamorf = Vabamorf.instance()
print(my_vab.synthesize('pood', form='pl p', partofspeech='S', phonetic=False))

print (my_vab.analyze("olla", guess=False, disambiguate=False, propername=False))

print("\n\n")

cases = [
    ('n', 'nimetav'),
    ('g', 'omastav'),
    ('p', 'osastav'),
    ('ill', 'sisseütlev'),
    ('in', 'seesütlev'),
    ('el', 'seestütlev'),
    ('all', 'alaleütlev'),
    ('ad', 'adessiiv (alalütlev)'),
    ('abl', 'ablatiiv (alaltütlev)'),
    ('tr', 'translatiiv (saav)'),
    ('ter', 'rajav'),
    ('es', 'olev'),
    ('ab', 'abessiiv (ilmaütlev)'),
    ('kom', 'komitatiiv (kaasaütlev)')]

def synthesize_all_s(word):
    case_rows = []
    sing_rows = []
    plur_rows = []
    for case, name in cases:
        case_rows.append(name)
        sing_rows.append(', '.join(synthesize(word, 'sg ' + case, 'S')))
        plur_rows.append(', '.join(synthesize(word, 'pl ' + case, 'S')))
    print(case_rows)
    print(sing_rows)
    print(plur_rows)

    from tabulate import tabulate
    print(tabulate(zip(case_rows, sing_rows, plur_rows), headers=["case", "singular", "plural"]))

# synthesize_all_s("kuusk")


forms = [
    ('ma', 'supiin aktiiv jaatav kõne sisseütlev'),
    ('da', 'infinitiiv jaatav kõne')
    ]

def synthesize_all_v(word):
    form_rows = []
    verb_rows = []
    for short, description in forms:
        form_rows.append(description)
        verb_rows.append(', '.join(synthesize(word, short, guess=False)))
    print(form_rows)
    print(verb_rows)

    from tabulate import tabulate
    print(tabulate(zip(form_rows, verb_rows), headers=["form", "verb"]))

synthesize_all_v("olema")


#
# Form 	Description 	Example
# b 	kindel kõneviis olevik 3. isik ainsus aktiiv jaatav kõne 	loeb
# d 	kindel kõneviis olevik 2. isik ainsus aktiiv jaatav kõne 	loed
# da 	infinitiiv jaatav kõne 	lugeda
# des 	gerundium jaatav kõne 	lugedes
# ge 	käskiv kõneviis olevik 2. isik mitmus aktiiv jaatav kõne 	lugege
# gem 	käskiv kõneviis olevik 1. isik mitmus aktiiv jaatav kõne 	lugegem
# gu 	käskiv kõneviis olevik 3. isik mitmus aktiiv jaatav kõne 	(nad) lugegu
# gu 	käskiv kõneviis olevik 3. isik ainsus aktiiv jaatav kõne 	(ta) lugegu
# ks 	tingiv kõneviis olevik 1. isik mitmus aktiiv jaatav kõne 	(me) loeks
# ks 	tingiv kõneviis olevik 1. isik ainsus aktiiv jaatav kõne 	(ma) loeks
# ks 	tingiv kõneviis olevik 2. isik mitmus aktiiv jaatav kõne 	(te) loeks
# ks 	tingiv kõneviis olevik 2. isik ainsus aktiiv jaatav kõne 	(sa) loeks
# ks 	tingiv kõneviis olevik 3. isik mitmus aktiiv jaatav kõne 	(nad) loeks
# ks 	tingiv kõneviis olevik 3. isik ainsus aktiiv jaatav kõne 	(ta) loeks
# ksid 	tingiv kõneviis olevik 2. isik ainsus aktiiv jaatav kõne 	(sa) loeksid
# ksid 	tingiv kõneviis olevik 3. isik mitmus aktiiv jaatav kõne 	(nad) loeksid
# ksime 	tingiv kõneviis olevik 1. isik mitmus aktiiv jaatav kõne 	(me) loeksime
# ksin 	tingiv kõneviis olevik 1. isik ainsus aktiiv jaatav kõne 	(ma) loeksin
# ksite 	tingiv kõneviis olevik 2. isik mitmus aktiiv jaatav kõne 	(te) loeksite
# ma 	supiin aktiiv jaatav kõne sisseütlev 	lugema
# maks 	supiin aktiiv jaatav kõne saav 	lugemaks
# mas 	supiin aktiiv jaatav kõne seesütlev 	lugemas
# mast 	supiin aktiiv jaatav kõne seestütlev 	lugemast
# mata 	supiin aktiiv jaatav kõne ilmaütlev 	lugemata
# me 	kindel kõneviis olevik 1. isik mitmus aktiiv jaatav kõne 	loeme
# n 	kindel kõneviis olevik 1. isik ainsus aktiiv jaatav kõne 	loen
# neg 	eitav kõne 	ei
# neg ge 	käskiv kõneviis olevik 2. isik mitmus aktiiv eitav kõne 	ärge
# neg gem 	käskiv kõneviis olevik 1. isik mitmus aktiiv eitav kõne 	ärgem
# neg gu 	käskiv kõneviis olevik 3. isik mitmus aktiiv eitav kõne 	(nad) ärgu
# neg gu 	käskiv kõneviis olevik 3. isik ainsus aktiiv eitav kõne 	(ta) ärgu
# neg gu 	käskiv kõneviis olevik passiiv eitav kõne 	ärgu
# neg ks 	tingiv kõneviis olevik 1. isik mitmus aktiiv eitav kõne 	(me) poleks
# neg ks 	tingiv kõneviis olevik 1. isik ainsus aktiiv eitav kõne 	(ma) poleks
# neg ks 	tingiv kõneviis olevik 2. isik mitmus aktiiv eitav kõne 	(te) poleks
# neg ks 	tingiv kõneviis olevik 2. isik ainsus aktiiv eitav kõne 	(sa) poleks
# neg ks 	tingiv kõneviis olevik 3. isik mitmus aktiiv eitav kõne 	(nad) poleks
# neg ks 	tingiv kõneviis olevik 3. isik ainsus aktiiv eitav kõne 	(ta) poleks
# neg me 	käskiv kõneviis olevik 1. isik mitmus aktiiv eitav kõne 	ärme
# neg nud 	kindel kõneviis lihtminevik 1. isik mitmus aktiiv eitav kõne 	(me) polnud
# neg nud 	kindel kõneviis lihtminevik 1. isik ainsus aktiiv eitav kõne 	(ma) polnud
# neg nud 	kindel kõneviis lihtminevik 2. isik mitmus aktiiv eitav kõne 	(te) polnud
# neg nud 	kindel kõneviis lihtminevik 2. isik ainsus aktiiv eitav kõne 	(sa) polnud
# neg nud 	kindel kõneviis lihtminevik 3. isik mitmus aktiiv eitav kõne 	(nad) polnud
# neg nud 	kindel kõneviis lihtminevik 3. isik ainsus aktiiv eitav kõne 	(ta) polnud
# neg nuks 	tingiv kõneviis minevik 1. isik mitmus aktiiv eitav kõne 	(me) polnuks
# neg nuks 	tingiv kõneviis minevik 1. isik ainsus aktiiv eitav kõne 	(ma) polnuks
# neg nuks 	tingiv kõneviis minevik 2. isik mitmus aktiiv eitav kõne 	(te) polnuks
# neg nuks 	tingiv kõneviis minevik 2. isik ainsus aktiiv eitav kõne 	(sa) polnuks
# neg nuks 	tingiv kõneviis minevik 3. isik mitmus aktiiv eitav kõne 	(nad) polnuks
# neg nuks 	tingiv kõneviis minevik 3. isik ainsus aktiiv eitav kõne 	(ta) polnuks
# neg o 	käskiv kõneviis olevik 2. isik ainsus aktiiv eitav kõne 	ära
# neg o 	kindel kõneviis olevik 1. isik mitmus aktiiv eitav kõne 	(me) pole
# neg o 	kindel kõneviis olevik 1. isik ainsus aktiiv eitav kõne 	(ma) pole
# neg o 	kindel kõneviis olevik 2. isik mitmus aktiiv eitav kõne 	(te) pole
# neg o 	kindel kõneviis olevik 2. isik ainsus aktiiv eitav kõne 	(sa) pole
# neg o 	kindel kõneviis olevik 3. isik mitmus aktiiv eitav kõne 	(nad) pole
# neg o 	kindel kõneviis olevik 3. isik ainsus aktiiv eitav kõne 	(ta) pole
# neg vat 	kaudne kõneviis olevik 1. isik mitmus aktiiv eitav kõne 	(me) polevat
# neg vat 	kaudne kõneviis olevik 1. isik ainsus aktiiv eitav kõne 	(ma) polevat
# neg tud 	kesksõna minevik passiiv eitav kõne 	poldud
# neg vat 	kaudne kõneviis olevik 2. isik mitmus aktiiv eitav kõne 	(te) polevat
# neg vat 	kaudne kõneviis olevik 2. isik ainsus aktiiv eitav kõne 	(sa) polevat
# neg vat 	kaudne kõneviis olevik 3. isik mitmus aktiiv eitav kõne 	(nad) polevat
# neg vat 	kaudne kõneviis olevik 3. isik ainsus aktiiv eitav kõne 	(ta) polevat
# nud 	kesksõna minevik aktiiv jaatav kõne 	lugenud
# nuks 	tingiv kõneviis minevik 1. isik mitmus aktiiv jaatav kõne 	(me) lugenuks
# nuks 	tingiv kõneviis minevik 1. isik ainsus aktiiv jaatav kõne 	(ma) lugenuks
# nuks 	tingiv kõneviis minevik 2. isik mitmus aktiiv jaatav kõne 	(te) lugenuks
# nuks 	tingiv kõneviis minevik 2. isik ainsus aktiiv jaatav kõne 	(sa) lugenuks
# nuks 	tingiv kõneviis minevik 3. isik mitmus aktiiv jaatav kõne 	(nad) lugenuks
# nuks 	tingiv kõneviis minevik 3. isik ainsus aktiiv jaatav kõne 	(ta) lugenuks
# nuksid 	tingiv kõneviis minevik 2. isik ainsus aktiiv jaatav kõne 	(sa) lugenuksid
# nuksid 	tingiv kõneviis minevik 3. isik mitmus aktiiv jaatav kõne 	(nad) lugenuksid
# nuksime 	tingiv kõneviis minevik 1. isik mitmus aktiiv jaatav kõne 	lugenuksime
# nuksin 	tingiv kõneviis minevik 1. isik ainsus aktiiv jaatav kõne 	lugenuksin
# nuksite 	tingiv kõneviis minevik 2. isik mitmus aktiiv jaatav kõne 	lugenuksite
# nuvat 	kaudne kõneviis minevik 1. isik mitmus aktiiv jaatav kõne 	(me) lugenuvat
# nuvat 	kaudne kõneviis minevik 1. isik ainsus aktiiv jaatav kõne 	(ma) lugenuvat
# nuvat 	kaudne kõneviis minevik 2. isik mitmus aktiiv jaatav kõne 	(te) lugenuvat
# nuvat 	kaudne kõneviis minevik 2. isik ainsus aktiiv jaatav kõne 	(sa) lugenuvat
# nuvat 	kaudne kõneviis minevik 3. isik mitmus aktiiv jaatav kõne 	(nad) lugenuvat
# nuvat 	kaudne kõneviis minevik 3. isik ainsus aktiiv jaatav kõne 	(ta) lugenuvat
# o 	käskiv kõneviis olevik 2. isik ainsus aktiiv jaatav kõne 	loe
# s 	kindel kõneviis lihtminevik 3. isik ainsus aktiiv jaatav kõne 	luges
# sid 	kindel kõneviis lihtminevik 2. isik ainsus aktiiv jaatav kõne 	(sa) lugesid
# sid 	kindel kõneviis lihtminevik 3. isik mitmus aktiiv jaatav kõne 	(nad) lugesid
# sime 	kindel kõneviis lihtminevik 1. isik mitmus aktiiv jaatav kõne 	lugesime
# sin 	kindel kõneviis lihtminevik 1. isik ainsus aktiiv jaatav kõne 	lugesin
# site 	kindel kõneviis lihtminevik 2. isik mitmus aktiiv jaatav kõne 	lugesite
# ta 	kindel kõneviis olevik passiiv eitav kõne 	loeta
# tagu 	käskiv kõneviis olevik passiiv jaatav kõne 	loetagu
# taks 	tingiv kõneviis olevik passiiv jaatav kõne 	loetaks
# takse 	kindel kõneviis olevik passiiv jaatav kõne 	loetakse
# tama 	supiin passiiv jaatav kõne 	loetama
# tav 	kesksõna olevik passiiv jaatav kõne 	loetav
# tavat 	kaudne kõneviis olevik passiiv jaatav kõne 	loetavat
# te 	kindel kõneviis olevik 2. isik mitmus aktiiv jaatav kõne 	loete
# ti 	kindel kõneviis lihtminevik passiiv jaatav kõne 	loeti
# tud 	kesksõna minevik passiiv jaatav kõne 	loetud
# tuks 	tingiv kõneviis minevik passiiv jaatav kõne 	loetuks
# tuvat 	kaudne kõneviis minevik passiiv jaatav kõne 	loetuvat
# v 	kesksõna olevik aktiiv jaatav kõne 	lugev
# vad 	kindel kõneviis olevik 3. isik mitmus aktiiv jaatav kõne 	loevad
# vat 	kaudne kõneviis olevik 1. isik mitmus aktiiv jaatav kõne 	(me) lugevat
# vat 	kaudne kõneviis olevik 1. isik ainsus aktiiv jaatav kõne 	(ma) lugevat
# vat 	kaudne kõneviis olevik 2. isik mitmus aktiiv jaatav kõne 	(te) lugevat
# vat 	kaudne kõneviis olevik 2. isik ainsus aktiiv jaatav kõne 	(sa) lugevat
# vat 	kaudne kõneviis olevik 3. isik mitmus aktiiv jaatav kõne 	(nad) lugevat
# vat 	kaudne kõneviis olevik 3. isik ainsus aktiiv jaatav kõne 	(ta) lugevat