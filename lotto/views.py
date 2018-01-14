from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import GuessNumbers
from .forms import PostForm

def index(request):
    lottos = GuessNumbers.objects.all()
    # return HttpResponse("<h1>Hello, Inflearn! </h1>") -> 원래 이렇게 쓰지 않고 아래의 방법을 보통 씀

    return render(request, "lotto/default.html", {"lottos": lottos})
    #lotto라는 templet으로 전달

def post(request):
    if request.method == "POST":
        #Save data
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index')
            # return HttpResponse("Saved OK")
        # return HttpResponse("POST method")

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {"form": form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, "lotto/detail.html", {"lotto": lotto})
