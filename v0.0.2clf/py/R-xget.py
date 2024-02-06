import time
from tqdm import tqdm
from decimal import Decimal

def get_try(x_text):
    s = 1
    i = 1
    p = 1
    x = s + i * p
    get = x_text.split("=")
    x_1 = Decimal(str(eval(get[0]))).quantize(Decimal("0.000001"), rounding="ROUND_HALF_UP")
    x_2 = Decimal(str(eval(get[1]))).quantize(Decimal("0.000001"), rounding="ROUND_HALF_UP")

def get(x_text, s, l, p_):
    p = eval(p_)
    x_ = False
    ii = None
    for i in tqdm(range(int((l - s) / p))):
        if ii:
            pass
        else:
            x = s + i * p
            get = x_text.split("=")
            x_1 = Decimal(str(eval(get[0]))).quantize(Decimal("0.000001"), rounding="ROUND_HALF_UP")
            x_2 = Decimal(str(eval(get[1]))).quantize(Decimal("0.000001"), rounding="ROUND_HALF_UP")
            if x_1 == x_2:
                x_ = True
                ii = i
                xx = Decimal(str(x)).quantize(Decimal("0.000001"), rounding="ROUND_HALF_UP")
                xc = x
    if x_ and "/" in p_:
        return xx, ft(str(int(s/p+ii))+"/"+p_.split("/")[1])
    elif x_ and not "/" in p_:
        return xx, str(int(xc))+"/1"
    else:
        return None

def ft(t):
    a, b = map(int, t.split("/"))
    x, y = a, b
    while b > 0:
        a, b = b, a % b
    x = int(x/a)
    y = int(y/a)
    return str(x)+'/'+str(y)

r = "\033[1;31;1m"
g = "\033[1;32;1m"
y = "\033[1;33;1m"
b = "\033[1;34;1m"
p = "\033[1;35;1m"
c = "\033[1;36;1m"
gr = "\033[1;37;1m"
w = "\033[1;39;1m"

def gett():
    global exit_, small, large, precision, r, g, y, b, p, c, gr, w, count
    gets = input(w+">>> "+g)
    print(w, end="")
    if gets == r"\help" or gets == r"\h":
        print(b+r"\h \help      -- 获取帮助")
        print(r"\a \about     -- 关于此程序")
        print(r"\e \exit      -- 退出程序")
        print(r"\s \small     -- 修改最小值,默认值为"+g+str(dv[0])+b+",目前值为"+g+str(small)+b)
        print(r"\l \large     -- 修改最小值,默认值为"+g+str(dv[1])+b+",目前值为"+g+str(large)+b)
        print(r"\p \precision -- 修改检测精度,默认值为"+g+dv[2]+b+",目前值为"+g+precision+b)
        print(r"\x \xget      -- 输入方程并获取结果")

    elif gets == r"\about" or gets == r"\a":
        print(b+r"R-xget v0.0.2clf(v0.0.2colorful) by:Cuber_AHZ")
        print(r"可以解方程,并具有"+g+"彩"+r+"色"+y+"的"+b+"界"+p+"面")

    elif gets == r"\exit" or gets == r"\e":
        exit_ = True

    elif gets == r"\small" or gets == r"\s":
        try:
            small_s = input(w+">>> "+g)
            small_ = int(small_s)
            if small_ > large:
                small, large = large, small_
            elif small_ == large:
                print(y+"[Warn]最小值不能等于最大值")
            else:
                small = small_
        except:
            print(r+"[Error]最小值修改失败,'"+small_s+"'不是一个数值")
        print(b+"small     -- "+g+"{}".format(small))
        print(b+"large     -- "+g+"{}".format(large))
        print(b+"precision -- "+g+"{}".format(precision))

    elif gets == r"\large" or gets == r"\l":
        try:
            large_s = input(w+">>> "+g)
            large_ = int(large_s)
            if small > large_:
                small, large = large_, small
            elif small == large_:
                print(y+"[Warn]最大值不能等于最小值")
            else:
                large = large_
        except:
            print(r+"[Error]最大值修改失败,'"+large_s+"'不是一个数值")
        print(b+"small     -- "+g+"{}".format(small))
        print(b+"large     -- "+g+"{}".format(large))
        print(b+"precision -- "+g+"{}".format(precision))

    elif gets == r"\precision" or gets == r"\p":
        try:
            precision_ = input(w+">>> "+g)
            precision_try = eval(precision_)
            precision = precision_
        except:
            print(r+"[Error]精度修改失败,'"+precision_+"'不是一个精度")
        print(b+"small     -- "+g+"{}".format(small))
        print(b+"large     -- "+g+"{}".format(large))
        print(b+"precision -- "+g+"{}".format(precision))

    elif gets == r"\xget" or gets == r"\x":
        equation = input(w+">>> "+g)
        print(w, end="")
        try:
            get_try(equation)
            x, t = get(equation, small, large, precision)
        except:
            print(r+"[Error]方程结果获取失败,尝试调整最小值、最大值和精度")
        try:
            time.sleep(0.1)
            print(b+"x={}={}".format(str(x), t))
        except:
            pass

    elif "x" in gets and "=" in gets:
        try:
            get_try(gets)
            x, t = get(gets, small, large, precision)
        except:
            print(r+"[Error]方程结果获取失败")
        try:
            time.sleep(0.1)
            print(b+"x={}={}".format(str(x), t))
        except:
            pass

    else:
        count += 1
        if count % 3 == 0:
            count = 0
            print(b+"输入"+g+r"\h"+b+"或"+g+r"\help"+b+"来获取帮助")
            print("可直接输入方程")
        else:
            print(r+"[Error]'"+gets+"'无法执行")

if __name__ == "__main__":
    count = 0
    exit_ = False
    print(y+"----*  R-xget v0.0.2clf  *----")

    try:
        with open("dv.txt", "r") as read:
            dv = read.read().split("\n")
        try_1 = int(dv[0])
        try_2 = int(dv[1])
        try_3 = dv[2].split("/")
        if try_1 > try_2:
            dv = [dv[1], dv[0], dv[2]]
        if try_1 == try_2:
            dv = [-1000, 1000, "1/42"]
    except:
        dv = [-1000, 1000, "1/42"]
    small, large, precision = int(dv[0]), int(dv[1]), dv[2]

    while True:
        try:
            gett()
            if exit_:
                print(y+"----*  R-xget v0.0.2clf  *----")
                break
        except:
            print("\n")
            print(y+"----*  R-xget v0.0.2clf  *----"+w)
            break
