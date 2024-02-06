import click
from decimal import Decimal

def ft(t):
    a, b = map(int, t.split("/"))
    x, y = a, b
    while b > 0:
        a, b = b, a % b
    x = int(x/a)
    y = int(y/a)
    return str(x)+'/'+str(y)

@click.command()
@click.option('-x', prompt="An equation containing x", help="An equation containing x")
@click.option("-s", default=-1000, help="The smallest number,Default value:-1000")
@click.option("-l", default=1000, help="The largest number,Default value:1000")
@click.option('-p', default="1/42", help="Detection interval,Default value:1/42")
def get(x, s=-1000, l=1000, p="1/42"):
    """This can be done to solve the equations"""
    try:
        pf = eval(p)
        x_ = False
        get = x.split("=")
        for i in range(int((l - s) / pf)):
            x = s + i * pf
            x_1 = Decimal(str(eval(get[0]))).quantize(Decimal("0.000001"), rounding = "ROUND_HALF_UP")
            x_2 = Decimal(str(eval(get[1]))).quantize(Decimal("0.000001"), rounding = "ROUND_HALF_UP")
            if x_1 == x_2:
                x_ = True
                break
        i = int(s/pf + i)
        if x_:
            x = Decimal(str(x)).quantize(Decimal("0.000001"))
            try:
                fz, fm = p.split("/")
                ft_get = str(int(fz)*i)+"/"+str(fm)
                a=ft(ft_get)
                click.echo(a)
            except:
                pass
            click.echo(x)
        else:
            click.echo("Error")
    except:
        click.echo("Error,use:--help")
        
if __name__ == "__main__":
    get()
    