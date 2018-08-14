def is_inside(diem, hinh):
    x = diem[0]
    y = diem[1]
    xA = hinh[0] + hinh[2]
    yB = hinh[1] + hinh[3]
    if hinh[0] <= x <=xA and hinh[1] <= y <= yB:
        return True
    else:
        return False

if is_inside([100, 120], [140, 60, 100, 200]) is True:
    print("Chuan roi")
else:
    print("Loi")