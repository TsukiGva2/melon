# Melon - Redesigning Stackish

A language for fun concurrency!

Melon is a concatenative programming language
designed for concurrent programming, here are the
three basic points i thought about in the development

- **Don't get in the way**

__The user has a shell, and can use it normally__

```
melon> ls
. .. .git/ melon/ repl/

melon> echo "hey!" # ok maybe not this because syntax
hey!
```

- **...But still be powerful when the user needs it!**

```
melon> task: two number? 2 = 'Two! put ;
melon> two
Starting task TWO

melon> 2
melon:task:TWO> Two!

melon> cancel
melon> 2
melon>
```

