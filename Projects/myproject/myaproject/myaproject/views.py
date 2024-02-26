from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse("404, Page not found! <br><br> <button onClick="" href='';"">Go to Homepage</button>")