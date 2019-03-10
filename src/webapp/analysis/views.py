
# analysis/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def analysis(request):
    return render(request, 'analysis/analysis.html', {})

@login_required
def create_analysis(request):
	if request.method == 'POST':
		return HttpResponse("This is where I'll show analyses")
	else:
		return HttpResponse("I'll add error handling here.")
