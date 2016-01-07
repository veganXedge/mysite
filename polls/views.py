from django.http import HttpResponse

def index(request):	#needs a URLconf in polls directory
	return HttpResponse("Hello, world. You're at the polls index.")
