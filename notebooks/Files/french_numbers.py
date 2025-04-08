import os.path as op
from random import Random
from math import log10
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


_PAD = "_PAD"
_GO = "_GO"
_EOS = "_EOS"
_UNK = "_UNK"
START_VOCAB = [_PAD, _GO, _EOS, _UNK]

PAD_ID = 0
GO_ID = 1
EOS_ID = 2
UNK_ID = 3


unicode_type = type(u"")
bytes_type = type(b"")


french_digit_names = [
    'un',
    'deux',
    'trois',
    'quatre',
    'cinq',
    'six',
    'sept',
    'huit',
    'neuf',
]

french_ten_names = [
    'dix',
    'vingt',
    'trente',
    'quarante',
    'cinquante',
    'soixante',
    'soixante dix',
    'quatre vingt',
    'quatre vingt dix',
]

french_exceptions = {
    11: 'onze',
    12: 'douze',
    13: 'treize',
    14: 'quatorze',
    15: 'quinze',
    16: 'seize',
    71: 'soixante et onze',
    72: 'soixante douze',
    73: 'soixante treize',
    74: 'soixante quatorze',
    75: 'soixante quinze',
    76: 'soixante seize',
    91: 'quatre vingt onze',
    92: 'quatre vingt douze',
    93: 'quatre vingt treize',
    94: 'quatre vingt quatorze',
    95: 'quatre vingt quinze',
    96: 'quatre vingt seize',
}


def to_french_phrase(number, is_units=True):
    if number >= int(1e6):
        raise NotImplemented('number should be less than a million, got %s', number)
    thousands, thousand_remainder = divmod(number, 1000)
    hundreds, hundred_remainder = divmod(thousand_remainder, 100)
    tens, units = divmod(hundred_remainder, 10)
    if thousands == 1:
        words = ['mille']
    elif thousands > 1:
        words = to_french_phrase(thousands, is_units=False).split()
        words.append('mille')
    else:
        words = []
    if hundreds == 1:
        words.append('cent')
    elif hundreds > 1:
        words.extend([french_digit_names[hundreds - 1], 'cent'])
        if tens == 0 and units == 0 and is_units:
            words[-1] = words[-1] + 's'
    exception = french_exceptions.get(hundred_remainder)
    if exception:
        words.append(exception)
        return " ".join(words)
    if tens > 0:
        words.append(french_ten_names[tens - 1])
        if units == 1 and tens != 8:
            words.append('et')
    if units > 0:
        words.append(french_digit_names[units - 1])
    if hundred_remainder == 80 and is_units:
        words[-1] = words[-1] + 's'
    return " ".join(words)


def generate_translations(low=1, high=int(1e6) - 1, exhaustive=int(1e4), random_seed=0):
    exhaustive = min(exhaustive, high)
    numbers, french_numbers = [], []
    for x in range(low, exhaustive + 1):
        numbers.append(str(x))
        french_numbers.append(to_french_phrase(x))

    rng = Random(random_seed)

    i = int(log10(exhaustive))
    for i in range(int(log10(exhaustive)), int(log10(high)) + 1):
        local_low = 10 ** i
        local_high = min(10 ** (i + 1), high)
        for _ in range(exhaustive):
            x = rng.randint(local_low, local_high)
            numbers.append(str(x))
            french_numbers.append(to_french_phrase(x))
    numbers, french_numbers = shuffle(numbers, french_numbers, random_state=random_seed)
    return numbers, french_numbers


def prepare_datasets(data_dir, low=0, high=int(1e6) - 1, exhaustive=int(1e4), random_seed=0):
    fr_train_token = op.join(data_dir, "fr_train.token")
    fr_train_text = op.join(data_dir, "fr_train.txt")
    fr_dev_token = op.join(data_dir, "fr_dev.token")
    fr_dev_text = op.join(data_dir, "fr_dev.txt")
    fr_vocab_path = op.join(data_dir, "fr.vocab")

    digits_train_token = op.join(data_dir, "digits_train.token")
    digits_train_text = op.join(data_dir, "digits_train.txt")
    digits_dev_token = op.join(data_dir, "digits_dev.token")
    digits_dev_text = op.join(data_dir, "digits_dev.txt")
    digits_vocab_path = op.join(data_dir, "load_vocabulary")

    filenames = [fr_train_token, digits_train_token,
                 fr_dev_token, digits_dev_token,
                 fr_vocab_path, digits_vocab_path]

    if all(op.exists(fn) for fn in filenames):
        print("Reusing existing number translation dataset from %s." % data_dir)
        return filenames

    print("Generating number translation dataset in %s..." % data_dir)
    numbers, french_numbers = generate_translations(
        low=low, high=high, exhaustive=exhaustive, random_seed=random_seed)
    num_train, num_dev, fr_train, fr_dev = train_test_split(
        numbers, french_numbers, test_size=0.1, random_state=random_seed)

    fr_vocab, rev_fr_vocab = build_vocabulary(fr_train, word_level=True)
    num_vocab, rev_num_vocab = build_vocabulary(num_train, word_level=False)

    save_vocabulary(rev_fr_vocab, fr_vocab_path)
    save_vocabulary(rev_num_vocab, digits_vocab_path)

    save_sentences(fr_train, fr_vocab, fr_train_token, fr_train_text)
    save_sentences(fr_dev, fr_vocab, fr_dev_token, fr_dev_text)

    save_sentences(num_train, num_vocab, digits_train_token, digits_train_text, word_level=False)
    save_sentences(num_dev, num_vocab, digits_dev_token, digits_dev_text, word_level=False)

    return filenames


def tokenize(sentence, word_level=True):
    if word_level:
        return sentence.split()
    else:
        return [sentence[i:i + 1] for i in range(len(sentence))]


def save_sentences(sentences, vocab, token_filename, text_filename,
                   word_level=True, encoding='utf-8'):
    with open(token_filename, 'wb') as token_f,\
         open(text_filename, 'wb') as text_f:
        for sentence in sentences:
            if isinstance(sentence, unicode_type):
                sentence = sentence.encode(encoding)
            text_f.write(sentence)
            text_f.write(b'\n')
            tokens = tokenize(sentence, word_level=word_level)
            token_ids = [vocab.get(t, UNK_ID) for t in tokens]
            token_f.write(b" ".join(str(t).encode(encoding) for t in token_ids))
            token_f.write(b"\n")


def save_vocabulary(rev_vocab, filename, encoding='utf-8'):
    with open(filename, 'wb') as f:
        for token in rev_vocab:
            f.write(token.encode(encoding))
            f.write(b'\n')


def load_vocabulary(filename, encoding='utf-8'):
    vocab, rev_vocab = {}, []
    with open(filename, 'rb') as f:
        for line in f:
            rev_vocab.append(line.decode(encoding).strip())
    for i, token in enumerate(rev_vocab):
        vocab[token] = i
    return vocab, rev_vocab


def build_vocabulary(sentences, word_level=True):
    rev_vocabulary = START_VOCAB[:]
    unique_tokens = set()
    for sentence in sentences:
        tokens = tokenize(sentence, word_level=word_level)
        unique_tokens.update(tokens)
    rev_vocabulary += sorted(unique_tokens)
    vocabulary = {}
    for i, token in enumerate(rev_vocabulary):
        vocabulary[token] = i
    return vocabulary, rev_vocabulary


def sentence_to_token_ids(sentence, vocabulary, word_level=True):
    tokens = tokenize(sentence, word_level=word_level)
    return [vocabulary.get(token, UNK_ID) for token in tokens]


def token_ids_to_sentence(token_ids, rev_vocabulary, word_level=True):
    sep = " " if word_level else ""
    return sep.join(rev_vocabulary[idx] for idx in token_ids if idx > 2)
