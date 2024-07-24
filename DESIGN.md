# Melon - Redesigning Stackish

Melon **__(MEtaprogamming Language, and cONcatenative)__** is a project aimed
at redesigning my last project (stackish), while reutilizing
core features (like being concatenative).

Among reutilized features are: The structure, the REPL and compiler/runtime
logic.

## Rationale

The Melon programming language has the same purpose of the
Stackish language, focusing on running completely as an
interactive language.

## Why and How?

This project started out with the intention of building a custom
shell, which instead of a common Shell scripting language, used
a dialect of forth. Forth's expressive nature, aligned with the
almost forth-like pipeline workflow of the shell seemed like the
perfect match, but, my goal wasn't really achieved with Stackish.

## A total mess

Stackish turned out exactly the way i __didn't__ want it.
Lots of bugs, weird strategies for everything, unclear design choices
and straight up implementation flaws deep within the language, maintaining
such a project is simply impossible.

So, i started up a github repo, willing to rebuild the project (Melon!),
just hoping i can do at least 1% better this time.

# Language design overview

Now, to the interesting stuff, code!

Melon has only 2 main types:

### Literals

Number -> A default python float
String -> Default python strings

### Words

Everything else is a word! part of the fun
of the minimalistic design is to have everything else be valid,
this is both for easier implementation and easier programming, but
it can be a pain to maintain. Which is not the focus of this
project.

A code example:

```lisp
melon> fun: say-hello 'hello! output ;
melon> say-hello
hello!

melon> fun: say next quote output ;
melon> say ola!
ola!

```

### Functions are `fun` in Melon!

In melon, words are defined with `FUN: <name> <operations> ;`

Melon also has macros, which are syntactic sugar for a more
complex operation we will see later (mode switching)

relevant example session (along with some docs):

```lisp
melon> 'on debug
Debug set to 'on

melon> macro maker
melon>    fun: 'what?? output ;
melon> endmacro
Defined Macro maker

melon> maker f
Defined f

melon> f
what??

melon> expand-last
__________________________________

call MAKER:

    [FUN:] 'what?? OUTPUT [;]

call fun:

    NEXT CREATE [COMPILE]

...

melon> 'next help
__________________________________
NEXT ( -- n )

Pushes a single word from
*compilation stream* to the
stack.

example:

melon> next foo
melon> peek
foo

melon> 'create help
__________________________________
CREATE ( n -- )

Creates a new word entry, the new
word's name is dropped from the
stack.

example:

melon> 'foo create
Defined foo

melon> words
output create peek words ... foo


melon> 'compile help
__________________________________
COMPILE ( -- )

Sets runtime state to compile.
This means every word from now on
will be compiled and inserted into
the newest word entry's code.

commonly used in conjunction with
`[` and `]` to define functions
which create functions.

example:

melon> 'foo create
Defined foo

melon> COMPILE
In Compilation mode

melon> 'bar output
melon> # no output, we're in compile mode
melon> INTERPRET
Exit Compilation mode

melon> foo
bar

Note:

COMPILE/INTERPRET can't be used
as-is inside function definitions,
because they can't be compiled.

If compilation is necessary,
simply surround the call with `[`
and `]`, e.g. [compile]/[interpret].
This will compile the instructions,
allowing the definition of functions
which create functions.

---------------------------------
```


