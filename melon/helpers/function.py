def apply(f):
    if callable(f):
        return f()
    print(f"non-callable {type(f).__name__} {f}")
    return f
