from goto import with_goto

@with_goto
def range(start, stop):
    i = start
    result = []

    label .begin
    print("at .begin")
    if i == stop:
        print("goto end")
        goto .end

    result.append(i)
    i += 1
    print("goto .begin")
    goto .begin

    label .end
    print("at .end")
    return result
