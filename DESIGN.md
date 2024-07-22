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

```forth
melon> fun: say-hello 'hello!' output ;
melon> say-hello
hello!

melon> fun: say next quote output ;
melon> say ola!
ola!

```

