from tkinter import *
import math
import random

PI = math.pi
SIDES_NO = 3
LENGTH = 80
START_P = (300, 300)


def vertex_coor(sides_no, side, start_p):
    """
    :param sides_no:
    :param length:
    :param start_p:
    :return:
    """
    angle = 2 * PI / sides_no
    ver_list = []
    for i in range(sides_no):
        y = math.sin(angle / 2 + angle * i) * side / (2 * math.sin(angle / 2))
        x = math.cos(angle / 2 + angle * i) * side / (2 * math.sin(angle / 2))
        # print("x, y {0} {1}".format(x + start_p[0], y + start_p[1]))
        ver_list.append((x + start_p[0], y + start_p[1]))
    # print(ver_list, "ver list")
    return ver_list


def pattern_1(points, canva, neg):
    """
          o
         ooo
        #ooo#
       ##ooo##
      ####o####

    :param points:
    :param canva:
    :param neg:
    :return:
    """
    out = '#000'
    if neg:
        fill_b = '#fff'
        fill_w = '#000'
    else:
        fill_b = '#000'
        fill_w = '#fff'
    D = points[0]
    A = points[1]
    B = points[2]
    AB_X = A[0] + (B[0] - A[0]) / 2
    AB_Y = A[1] + (B[1] - A[1]) / 2
    AD_X = A[0] + (D[0] - A[0]) / 2
    AD_Y = A[1] + (D[1] - A[1]) / 2
    BD_X = B[0] + (D[0] - B[0]) / 2
    BD_Y = B[1] + (D[1] - B[1]) / 2
    canva.create_polygon([D[0], D[1], AD_X, AD_Y, AB_X, AB_Y, BD_X, BD_Y], outline=out, fill=fill_b, width=2)
    canva.create_polygon([A[0], A[1], AB_X, AB_Y, AD_X, AD_Y], outline=out, fill=fill_w, width=2)
    canva.create_polygon([B[0], B[1], AB_X, AB_Y, BD_X, BD_Y], outline=out, fill=fill_w, width=2)


def pattern_2(points, canva, neg):
    """
          #
         #o#
        #ooo#
       #ooooo#
      ##ooooo##

    :param points:
    :param canva:
    :param neg:
    :return:
    """
    out = '#000'
    if neg:
        fill_b = '#fff'
        fill_w = '#000'
    else:
        fill_b = '#000'
        fill_w = '#fff'
    D = points[0]
    A = points[1]
    B = points[2]
    E_X = A[0] + (B[0] - A[0]) / 4
    E_Y = A[1] + (B[1] - A[1]) / 4
    F_X = A[0] + 3 * (B[0] - A[0]) / 4
    F_Y = A[1] + 3 * (B[1] - A[1]) / 4
    canva.create_polygon([A[0], A[1], E_X, E_Y, D[0], D[1]], outline=out, fill=fill_w, width=2)
    canva.create_polygon([A[0], A[1], E_X, E_Y, D[0], D[1]], outline=out, fill=fill_w, width=2)
    canva.create_polygon([E_X, E_Y, F_X, F_Y, D[0], D[1]], outline=out, fill=fill_b, width=2)
    canva.create_polygon([B[0], B[1], F_X, F_Y, D[0], D[1]], outline=out, fill=fill_w, width=2)


def pattern_3(points, canva, neg):
    """
          #
         oo#
        ooo##
       ##oo##o
      #####oooo

    :param points:
    :param canva:
    :param neg:
    :return:
    """
    out = '#000'
    if neg:
        fill_b = '#fff'
        fill_w = '#000'
    else:
        fill_b = '#000'
        fill_w = '#fff'
    D = points[0]
    A = points[1]
    B = points[2]
    AB_X = A[0] + (B[0] - A[0]) / 2
    AB_Y = A[1] + (B[1] - A[1]) / 2
    AD_X = A[0] + (D[0] - A[0]) / 3
    AD_Y = A[1] + (D[1] - A[1]) / 3
    BD_X = B[0] + (D[0] - B[0]) / 3
    BD_Y = B[1] + (D[1] - B[1]) / 3
    canva.create_polygon([AD_X, AD_Y, AB_X, AB_Y, D[0], D[1]], outline=out, fill=fill_w, width=2)
    canva.create_polygon([BD_X, BD_Y, AB_X, AB_Y, D[0], D[1]], outline=out, fill=fill_b, width=2)
    canva.create_polygon([A[0], A[1], AB_X, AB_Y, AD_X, AD_Y], outline=out, fill=fill_b, width=2)
    canva.create_polygon([B[0], B[1], AB_X, AB_Y, BD_X, BD_Y], outline=out, fill=fill_w, width=2)


def pattern_4(points, canva, neg):
    """
          #
         ###
        oo#oo
       ooooooo
      ooooooooo

    :param points:
    :param canva:
    :param neg:
    :return:
    """
    out = '#000'
    if neg:
        fill_b = '#000'
        fill_w = '#fff'
    else:
        fill_b = '#fff'
        fill_w = '#000'
    D = points[0]
    A = points[1]
    B = points[2]
    M_X = D[0] - (D[0] - (A[0] + (B[0] - A[0]) / 2)) / 2
    M_Y = D[1] - (D[1] - (A[1] + (B[1] - A[1]) / 2)) / 2
    AD_X = A[0] + 2 * (D[0] - A[0]) / 3
    AD_Y = A[1] + 2 * (D[1] - A[1]) / 3
    BD_X = B[0] + 2 * (D[0] - B[0]) / 3
    BD_Y = B[1] + 2 * (D[1] - B[1]) / 3
    canva.create_polygon([D[0], D[1], AD_X, AD_Y, M_X, M_Y, BD_X, BD_Y], outline=out, fill=fill_b, width=2)
    canva.create_polygon([AD_X, AD_Y, A[0], A[1], B[0], B[1], BD_X, BD_Y, M_X, M_Y], outline=out, fill=fill_w, width=2)

def pattern_5(points, canva, neg):
    """
          o
         ooo
        #####
       ######
      #########

    :param points:
    :param canva:
    :param neg:
    :return:
    """
    out = '#000'
    if neg:
        fill_b = '#fff'
        fill_w = '#000'
    else:
        fill_b = '#000'
        fill_w = '#fff'
    D = points[0]
    A = points[1]
    B = points[2]
    AD_X = A[0] + (D[0] - A[0]) / 2
    AD_Y = A[1] + (D[1] - A[1]) / 2
    BD_X = B[0] + (D[0] - B[0]) / 2
    BD_Y = B[1] + (D[1] - B[1]) / 2
    canva.create_polygon([D[0], D[1], AD_X, AD_Y, BD_X, BD_Y], outline=out, fill=fill_b, width=2)
    canva.create_polygon([A[0], A[1], B[0], B[1], BD_X, BD_Y, AD_X, AD_Y], outline=out, fill=fill_w, width=2)



def create_shape(sides_no, length, start_p):
    verts = vertex_coor(sides_no, length, start_p)
    mirror = int(len(verts) / 2)

    for i in range(len(verts)):
        if i == len(verts) - 1:
            j = 0
        else:
            j = i + 1
        canv.create_line(verts[i][0], verts[i][1], verts[j][0], verts[j][1], fill="#15001c", width=3)

    pattern_list = [pattern_1, pattern_2, pattern_3, pattern_4, pattern_5]
    #pattern_list = [pattern_list[0]]
    #pattern_5(((start_p[0], start_p[1]), verts[0], verts[1]), canv, True)

    for i in range(mirror):
        sid = random.choice(pattern_list)

        if i % 2 == 0:
            negativ = True
            sid(((start_p[0], start_p[1]), verts[i], verts[i + 1]), canv, negativ)
            negativ = False
        else:
            negativ = False
            sid(((start_p[0], start_p[1]), verts[i], verts[i + 1]), canv, negativ)
            negativ = True
        j = i + mirror
        k = j + 1
        # print(j, k)
        if k == 2 * mirror:
            k = 0
        sid(((start_p[0], start_p[1]), verts[j], verts[k]), canv, negativ)


        # pattern_1(((300, 300), verts[i], verts[j]), canv, negativ)
        # pattern_list[0](((300, 300), verts[i], verts[j]), canv, negativ)
        # pattern_1(((300, 300), verts[i], verts[j]), canv, negativ)


master = Tk()
canv = Canvas(master, width=1000, height=1000)
canv.pack()
for i in range(2):
    l = [x for x in range(4, 12, 2)]
    sid = random.choice(l)
    xx = random.randint(100, 500)
    yy = random.randint(100, 500)
    len_sid = random.randint(10, 150)
    #create_shape(sid, len_sid, (xx, yy))
    #print(sid, len_sid, (xx, yy))

for j in range(4):
    for i in range(int(500/100)):
        create_shape(4+j*2, 90-10*j, (100+200*i, 100+230*j))


#create_shape(16, 50, (300, 300))

mainloop()
