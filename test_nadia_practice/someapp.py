def join_str(xs, delimiter: str):
    return delimiter.join([str(x) for x in xs])
    # for i in xs:
    #     result = delimiter.join(str(i))
    #     return result
print(join_str([1,2,3],', '))