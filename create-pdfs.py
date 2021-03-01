import os

chapters = (
    ("introduction", 5),
    ("trees-and-forests", 17),
    ("linlog", 31),
    ("glm", 41),
    ("feature-selection", 43),
    ("kernels", 55),
    ("END", 74)
)


def pairs(x):
    for i in range(len(x)-1):
        yield x[i], x[i+1]

for a, b in pairs(chapters):
    cmd = "pdfjam notes.pdf %d-%d -o pdfs/%s.pdf" % (a[1], b[1]-1, a[0])
    os.system(cmd)
