# originally from https://github.com/JonathanNickerson/talon_voice_user_scripts
# and https://github.com/pimentel/talon_user/blob/master/repeat.py

from talon.voice import Context, Rep, RepPhrase, talon
from user.utils import parse_words_as_integer

ctx = Context('repeater')

# TODO: This could be made more intelligent:
#         * Apply a timeout after which the command will not repeat previous actions
#         * Prevent stacking of repetitions upon previous repetitions
def repeat(m):
    repeat_count = parse_words_as_integer(m._words[1:])

    if repeat_count != None and repeat_count >= 2:
        repeater = Rep(repeat_count - 1)
        repeater.ctx = talon
        return repeater(None)

ctx.keymap({
  #  'creek': RepPhrase(1), # how is this different from Rep()?
    'twice': Rep(1),
    'thrice': Rep(2),
    '(rep) (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9) + ': repeat,
    })

