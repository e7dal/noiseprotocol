from .constants import TOKEN_E, TOKEN_S, TOKEN_EE, TOKEN_ES, TOKEN_SE, TOKEN_SS, TOKEN_PSK


class Pattern(object):
    """
    TODO document
    """
    # As per specification, if both parties have pre-messages, the initiator is listed first. To reduce complexity,
    # pre_messages shall be a list of two lists:
    # the first for the initiator's pre-messages, the second for the responder
    pre_messages = [
        [],
        []
    ]
    # TODO Comment
    tokens = []

    def __init__(self):
        self.has_pre_messages = any(map(lambda x: len(x) > 0, self.pre_messages))

    def get_initiator_pre_messages(self) -> list:
        return self.pre_messages[0]

    def get_responder_pre_messages(self) -> list:
        return self.pre_messages[1]


# One-way patterns

class PatternN(Pattern):
    pre_messages = [
        [],
        [TOKEN_S]
    ]
    tokens = [
        [TOKEN_E, TOKEN_ES]
    ]


class PatternK(Pattern):
    pre_messages = [
        [TOKEN_S],
        [TOKEN_S]
    ]
    tokens = [
        [TOKEN_E, TOKEN_ES, TOKEN_SS]
    ]


class PatternX(Pattern):
    pre_messages = [
        [],
        [TOKEN_S]
    ]
    tokens = [
        [TOKEN_E, TOKEN_ES, TOKEN_S, TOKEN_SS]
    ]


# Interactive patterns

class PatternNN(Pattern):
    tokens = [
        [TOKEN_E],
        [TOKEN_E, TOKEN_EE]
    ]


class PatternKN(Pattern):
    pre_messages = [
        [TOKEN_S],
        []
    ]
    tokens = [
        [TOKEN_E],
        [TOKEN_E, TOKEN_EE, TOKEN_SE]
    ]


class PatternNK(Pattern):
    pre_messages = [
        [],
        [TOKEN_S]
    ]
    tokens = [
        [TOKEN_E, TOKEN_ES],
        [TOKEN_E, TOKEN_EE]
    ]


class PatternKK(Pattern):
    pre_messages = [
        [TOKEN_S],
        [TOKEN_S]
    ]
    tokens = [
        [TOKEN_E, TOKEN_ES, TOKEN_SS],
        [TOKEN_E, TOKEN_EE, TOKEN_SE]
    ]


class PatternNX(Pattern):
    tokens = [
        [TOKEN_E],
        [TOKEN_E, TOKEN_EE, TOKEN_S, TOKEN_ES]
    ]


class PatternKX(Pattern):
    pre_messages = [
        [TOKEN_S],
        []
    ]
    tokens = [
        [TOKEN_E],
        [TOKEN_E, TOKEN_EE, TOKEN_SE, TOKEN_S, TOKEN_ES]
    ]


class PatternXN(Pattern):
    tokens = [
        [TOKEN_E],
        [TOKEN_E, TOKEN_EE],
        [TOKEN_S, TOKEN_SE]
    ]


class PatternIN(Pattern):
    tokens = [
        [TOKEN_E, TOKEN_S],
        [TOKEN_E, TOKEN_EE, TOKEN_SE]
    ]


class PatternXK(Pattern):
    pre_messages = [
        [],
        [TOKEN_S]
    ]
    tokens = [
        [TOKEN_E, TOKEN_ES],
        [TOKEN_E, TOKEN_EE],
        [TOKEN_S, TOKEN_SE]
    ]


class PatternIK(Pattern):
    pre_messages = [
        [],
        [TOKEN_S]
    ]
    tokens = [
        [TOKEN_E, TOKEN_ES, TOKEN_S, TOKEN_SS],
        [TOKEN_E, TOKEN_EE, TOKEN_SE]
    ]


class PatternXX(Pattern):
    tokens = [
        [TOKEN_E],
        [TOKEN_E, TOKEN_EE, TOKEN_S, TOKEN_ES],
        [TOKEN_S, TOKEN_SE]
    ]


class PatternIX(Pattern):
    tokens = [
        [TOKEN_E, TOKEN_S],
        [TOKEN_E, TOKEN_EE, TOKEN_SE, TOKEN_S, TOKEN_ES]
    ]