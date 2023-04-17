import random, math

def show(x,s):
    for i in range(s):
        for j in range(s):
            if x[i][j] == 0:
                print("-",end="")
            if x[i][j] == 1:
                print("m",end="")
        print()



def mid(tre_x, tre_y, ply_x, ply_y):
    print("plyer_pos",ply_x,ply_y)
    r = ply_x - tre_x    #x
    u = ply_y - tre_y    #y
    d = math.sqrt(r**2 + u**2)
    print("宝までの距離は",d)
    return  d



def chara(ply_x, ply_y,x,s):
    m = input("移動したい方向")
    if m == "d":
        if ply_x >= 4:
            print("again")
            ply_x,ply_y = chara(ply_x, ply_y,x,s)
            return ply_x ,ply_y
        else:
            ply_x = ply_x + 1
            return ply_x, ply_y
    elif m == "a":
        if ply_x <= 0:
            print("again")
            ply_x,ply_y = chara(ply_x, ply_y,x,s)
            return ply_x ,ply_y
        else:
            ply_x = ply_x - 1
            return ply_x, ply_y
    elif m == "s":
        if ply_y >= 4:
            print("again")
            ply_x,ply_y = chara(ply_x, ply_y,x,s)
            return ply_x ,ply_y
        else:
            ply_y = ply_y + 1
            return ply_x, ply_y
    elif m == "w":
        if ply_y <= 0:
            print("again") 
            ply_x,ply_y = chara(ply_x, ply_y,x,s)
            return ply_x ,ply_y
        else:
            ply_y = ply_y - 1
            return ply_x, ply_y
    else:
        print("again") 
        ply_x,ply_y = chara(ply_x, ply_y,x,s)
        return ply_x ,ply_y


def stop():
    h = input("やめますか？")
    if h == "y":
        return True


s = 5
x =[[0 for i in range(s)]for i in range(s)]

t = 3
tre_x = random.randrange(0, t)  #宝_x
tre_y = random.randrange(0, t)  #宝_y

p = 3
ply_x = random.randrange(0, p)  #player_x
ply_y = random.randrange(0, p)  #player_y
x[ply_y][ply_x] = 1


d = mid(tre_x, tre_y, ply_x, ply_y)
show(x,s)
x[ply_y][ply_x] = 0


print("宝は",t,"×",t,"の範囲にあります")
while d != 0:
    if stop():
        print("stopped")
        break
    ply_x, ply_y = chara(ply_x, ply_y,x,s)
    x[ply_y][ply_x] = 1
    show(x,s)
    x[ply_y][ply_x] = 0
    d = mid(tre_x, tre_y, ply_x, ply_y)
print("nice")
