calls = 0
def string_info(string):
    global calls
    calls += 1
    print([len(string), string.upper(), string.lower()])

def is_contains(string, list_to_search):
    global calls
    calls += 1

    list_to_search = [word.casefold() for word in list_to_search]
    if string.casefold() in list_to_search:
        print(True)
    else:
        print(False)
string_info('University')
string_info('StUdEnTs')
is_contains('SUn', ['SUnset', 'Sunny', 'sun'])
is_contains('Hate', ['Hater', 'hating', 'Hateless'])
print(calls)

































# print(string_info('University'))
# print(string_info('AppLe'))












