from django.shortcuts import render# render template(flask)のと同じ。HTMLファイルを読むときに使う

def index(request):
    return render(request, "demo_app/index.html", {})
