import turtle as t

def draw_histogram(a_list):
    w = 40 # histogram width
    m = len(a_list) # number of list members
    t.color("blue")
    t.fillcolor("red")
    for i in range(0, m):
        t.begin_fill()
        t.left(90)
        t.forward(a_list[i])
        t.write(str(a_list[i]))  # text value
        t.right(90)
        t.forward(w)
        t.right(90)
        t.forward(a_list[i])
        t.left(90)
        t.end_fill()
    t.done()
    return
def hello():
    print("This should not be printed.")
    return 0