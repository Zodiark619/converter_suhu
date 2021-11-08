from django.shortcuts import render

# Create your views here.
def index(request):
    number=float(request.GET.get("number"))
    initial=number
    type=request.GET.get("type")
    result_type=request.GET.get('result_type')
    if request.GET.get("type")=="C":
        if request.GET.get("result_type")=="C":
            number=number
        elif request.GET.get("result_type")=="F":
            number=(9/5)*number+32
        elif request.GET.get("result_type")=="K":
            number=number+273.15
        elif request.GET.get("result_type")=="R":
            number=(4/5)*number
    if request.GET.get("type")=="F":
        if request.GET.get("result_type")=="F":
            number=number
        elif request.GET.get("result_type")=="C":
            number=(5/9)*(number-32)
        elif request.GET.get("result_type")=="K":
            number=number+459.67*5/9
        elif request.GET.get("result_type")=="R":
            number=(4/9)*(number-32)
    if request.GET.get("type")=="K":
        if request.GET.get("result_type")=="K":
            number=number
        elif request.GET.get("result_type")=="F":
            number=((9/5)*number)-459.67
        elif request.GET.get("result_type")=="C":
            number=number-273.15
        elif request.GET.get("result_type")=="R":
            number=(4/5)*(number-273)
    if request.GET.get("type")=="R":
        if request.GET.get("result_type")=="R":
            number=number
        elif request.GET.get("result_type")=='F':
            number=(2.25*number)+32
        elif request.GET.get("result_type")=="K":
            number=(number/0.8)+273.15
        elif request.GET.get("result_type")=="C":
            number=number/0.8
    return render(request,'meong1/index.html',{'number':number,'initial':initial,'type':type,'result_type':result_type})
