# abc = 'With three\n\n\n\n\n\n words'
# str2 = "dev.lubinets@gmail.com;mr.lubinets@gmail.com"
# stuff = abc.split()
# print(abc)
# print(stuff)
#
# for w in stuff:
#     print(w)
#
# for w in str2.split(";"):
#     print(w)

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
print(pieces)
print(parts)
print(n)

ddd = dict()
ddd[0] = 21
print(ddd)
dictE = {}
print(f"empty dict: {dictE}")

dictNonEmpty = {"email": "deef@gmial.com", "course": 1}
print(dictNonEmpty)


counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))