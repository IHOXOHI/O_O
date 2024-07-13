def cp(ori,des,ch_lg=0,ch_txt=''):
    fil_ori = open(ori,'r')
    fil_des = open(des,'w')
    l = fil_ori.readline()
    n = 1
    while l != '':
        if n == int(ch_lg):
            text = str(ch_txt)
        else:
            text = str(l)
        fil_des.write(text)
        l = fil_ori.readline()
        n += 1
    fil_des.write('#')
    fil_des.close()
    fil_ori.close()

def view(ori,L1=1,L2=1):
    L1, L2 = int(L1), int(L2)
    fil_ori = open(ori, 'r')
    if L2 == 1:
        l = fil_ori.readline()
        while l != '':
            L2 += 1
            l = fil_ori.readline()
    fil_ori.close()
    fil_ori = open(ori, 'r')
    if L1 != 1:
        l = fil_ori.readline()
        n = 1
        while n != L1:
            n += 1
            l = fil_ori.readline()
    text = ""
    n = 1
    while L1 <= L2:
        ligne = fil_ori.readline()
        text = text + str(n) + " " + ligne
        L1 += 1
        n += 1
    fil_ori.close()
    print(text)
############