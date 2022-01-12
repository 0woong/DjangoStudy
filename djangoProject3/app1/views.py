from django.shortcuts import render

# Create your views here.
def start(request):
    print('request받아서 board함수 호출됨')
    # html에 넣고 싶은 데이터
    n1 = 100
    n2 = 300
    result = 100 + 300
    data = {'name' : 'park', 'age' : 100, 'n1' : n1, 'n2' : n2, 'result' : result}
    return render(request, 'app1/start.html', data)