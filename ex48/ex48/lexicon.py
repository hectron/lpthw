def scan(s):
    if not s:
        return "Not a string."

    fragments = s.lower().split()
    direction_words = ['north', 'south', 'east', 'west', 'down',
            'up', 'left', 'right', 'back']
    verbs = ['go', 'stop', 'kill', 'eat']
    stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
    nouns = ['door', 'bear', 'princess', 'cabinet']
    numbers = [x for x in range(10)]

    # We structure the tuple here, and
    # append it to the return sentence
    first_word = ''
    second_word = ''
    sentence = []

    for fragment in fragments:
        if fragment in direction_words:
            first_word = 'direction'
            second_word = fragment

        elif fragment in verbs:
            first_word = 'verb'
            second_word = fragment

        elif fragment in stop_words:
            first_word = 'stop'
            second_word = fragment

        elif fragment in nouns:
            first_word = 'noun'
            second_word = fragment

        elif convert_number(fragment):
            first_word = 'number'
            second_word = convert_number(fragment)
            # we could use fragment.isdigit() and just type cast it to int.
        else:
            first_word = 'error'
            second_word = fragment

        if first_word and second_word:
            sentence.append((first_word, second_word))


    return sentence

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
