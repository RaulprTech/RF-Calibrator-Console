from skrf import Network
import matplotlib.pyplot as plt
import os

def select():
    s = input('Elige un parametreo para graficar [s1, s2, s3, s4 o s para graficar todos] ')
    if s == 's':
        n = 5
        m = 5
    elif s == 's1':
        n = 0
        m = 0
    elif s == 's2':
        n = 0
        m = 1
    elif s == 's3':
        n = 1
        m = 0
    elif s == 's4':
        n = 1
        m = 1
    return n, m

def smith_chart(route):
    line = Network(route)
    print(line)
    i = select()
    i[0] != 5 and line.plot_s_smith(m=i[0],n=i[1],  #   Only one param
        r=1,
        chart_type='s',
        show_legend=True,
        draw_labels=True,
        draw_vswr=True)
    i[0] == 5 and line.plot_s_smith(        #     All params
        chart_type='s',
        show_legend=True,
        draw_labels=True,
        draw_vswr=True)
    plt.show()


if __name__ == '__main__':
    smith_chart('./input/Line.s2p')