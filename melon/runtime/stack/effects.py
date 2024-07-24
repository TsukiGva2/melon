def N_NIL(word):
    def N_NIL_word(state):
        n = state.stack.pop()
        word(n)

    return N_NIL_word


def N_N(word):
    def N_N_word(state):
        n = state.stack.pop()
        state.stack.push(word(n))

    return N_N_word


def NIL_N(word):
    def NIL_N_word(state):
        state.stack.push(word())

    return NIL_N_word


def NIL_NIL(word):
    return word
