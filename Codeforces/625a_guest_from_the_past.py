d = int(raw_input())
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

if(a <= (b - c) or b > d):
  qntd = d / a
else :
  if(d >= b):
    qntd = (d - c) / (b - c)
    d -= qntd * (b - c)
    qntd += d / a
  else :
    qntd = 0

print (qntd)