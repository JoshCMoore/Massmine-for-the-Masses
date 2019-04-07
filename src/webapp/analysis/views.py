# analysis/views.py


from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#import matplotlib
#matplotlib.use('agg')
#import matplotlib.pyplot as plt; plt.rcdefaults()
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#import matplotlib.pyplot as plt
#import numpy as np
import io

from analysis.models import Study
from django.views.generic.base import TemplateView
import plotly
from plotly import tools as tls
import plotly.offline
import plotly.graph_objs
from pytz import timezone
title = ''

@login_required
class BarGraph(TemplateView):
        template_name = 'graphH.html'

        def __init__(self, name):
               self.name = name

        def get_context_data(self, **kwargs):	
                context = super().get_context_data(**kwargs)
                objects = ('Random', 'Words', 'Will','Go','Here')
                y_pos = np.arange(len(objects))
                performance = [10,8,6,4,2]
                f = plt.figure(1)
                plt.bar(y_pos, performance, align='center', alpha=0.5)
                plt.xticks(y_pos, objects)
                plt.ylabel('Times used')
                plt.title('Most common words used')
                plt.title(title)
                plotly_fig = tls.mpl_to_plotly(f)
                div_fig = plotly.offline.plot(plotly_fig, auto_open=False, output_type='div')
                context['graph'] = div_fig
                return context


@login_required
class Histogram(TemplateView):
        template_name = 'graphH.html'

        def __init__(self, name):
                self.name = name

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                x = np.random.randn(10000)
                f = plt.figure(200)
                plt.hist(x, color='lightblue')
                plt.xlabel(title)
                plt.ylabel('No. of tweets')
                plt.title(title)
                plotly_fig = tls.mpl_to_plotly(f)
                div_fig = plotly.offline.plot(plotly_fig, auto_open=False, output_type='div')
                context['graph'] = div_fig
                return context

# def get_studies(request):
# 	context ={'studies_html':""} 
# 	user = request.user
# 	for x in Study.objects.all():
# 		if str(x.user) == str(user):
# 			context['studies_html']+=("<li><a href=\"/analysis/view_study/?value="+x.study_id+"\">"+x.study_id[:-10]+"</a></li>")
# 	return render(request, 'analysis/get_studies.html', context)

def get_study(request):
	studyid = request.POST['study_select']
	current_study = Study.objects.get(study_id=studyid).tweets.all()
	return render(request, 'analysis/get_study.html', locals())


@login_required
def tweet_type(request):
    title = 'Tweet Type'
    g = BarGraph(request)
    context = g.get_context_data()
    return render(request, 'analysis/graph.html', context)

@login_required
def graph_times_retweeted(request):
    title = 'Times retweeted'
    g = Histogram(request)
    context = g.get_context_data()
    return render(request, 'analysis/graph.html', context)

@login_required
def graph_times_favorited(request):
    title = 'Times favorited'
    g = Histogram(request)
    context = g.get_context_data()
    return render(request, 'analysis/graph.html', context)

@login_required
def graph(request):
    g = Graph(request)
    context = g.get_context_data()
    return render(request, 'analysis/graph.html', context)


@login_required
class Graph(TemplateView):
    template_name = 'graph.html'
    
    def __init__(self, name):
        self.name = name
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        x = [-1,0,1,3,7,9]
        y = [i**2 -i+2 for i in x]
        stuff_to_display = plotly.graph_objs.Scatter(x=x, y=y, marker={'color': 'blue', 'symbol': 104, 'size': 10}, mode = "lines", name = "Date")
        
        data = plotly.graph_objs.Data([stuff_to_display])
        layout = plotly.graph_objs.Layout(title = "Tweets over time", xaxis={'title': 'date'}, yaxis={'title':'number of tweets'})
        figure  = plotly.graph_objs.Figure(data=data, layout=layout)
        div = plotly.offline.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div
        return context

@login_required
def analysis(request):
	context ={'studies_html':""} 
	user = request.user
	for x in Study.objects.all():
		if str(x.user) == str(user):
			context['studies_html']+=("<option value=\""+x.study_id+"\">"+x.study_id[:-10]+"</option>")
	return render(request, 'analysis/analysis.html', context)

@login_required
def create_analysis(request):
	answer = request.POST['analysis_select']
	if answer == "tweet_type":
		return tweet_type(request)
	elif answer == "freq_words":
		return display_freq_words(request)
	elif answer == "freq_hashtags":
		return display_freq_hashtags(request)
	elif answer == "act_authors":
		return display_act_authors(request)
	elif answer == "pop_authors":
		return display_pop_authors(request)
	elif answer == "men_accounts":
		return display_ment_accounts(request)
	elif answer == "lang":
		return display_lang(request)
	elif answer == "device":
		return display_device(request)
	elif answer == "date":
		return graph(request)
	elif answer == "times_retweeted":
		return graph_times_retweeted(request) 
	elif answer == "times_favorited":
		return graph_times_favorited(request)
	elif answer == "location":
		return display_location(request)
	elif answer == "view_tweets":
		return get_study(request)
	else:
		return HttpResponse("Error")

def display_tweet_type(request):
	objects = ('Post', 'Retweet', 'Response')
	y_pos = np.arange(len(objects))
	performance = [10,8,6]
	canvas = plt.figure(1)
	plt.bar(y_pos, performance, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel('Number of tweets')
	plt.title('Most common tweet type')
	FigureCanvas(canvas)
	buf = io.BytesIO()
	plt.savefig(buf, format='png')
	plt.close(canvas)
	response = HttpResponse(buf.getvalue(), content_type='image/png')
	return response

def display_freq_words(request):
        objects = ('Random', 'Words', 'Will','Go','Here')
        y_pos = np.arange(len(objects))
        performance = [10,8,6,4,2]
        canvas = plt.figure(1)
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Times used')
        plt.title('Most common words used')
        FigureCanvas(canvas)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(canvas)
        response = HttpResponse(buf.getvalue(), content_type='image/png')
        return response

def display_freq_hashtags(request):
        objects = ('Random', 'Hashtags', 'Will','Go','Here')
        y_pos = np.arange(len(objects))
        performance = [10,8,6,4,2]
        canvas = plt.figure(1)
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Times used')
        plt.title('Most common hashtags used')
        FigureCanvas(canvas)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(canvas)
        response = HttpResponse(buf.getvalue(), content_type='image/png')
        return response

def display_act_authors(request):
        objects = ('Random', 'Names', 'Will','Go','Here')
        y_pos = np.arange(len(objects))
        performance = [10,8,6,4,2]
        canvas = plt.figure(1)
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Number of posts')
        plt.title('Most active authors in study')
        FigureCanvas(canvas)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(canvas)
        response = HttpResponse(buf.getvalue(), content_type='image/png')
        return response

def display_pop_authors(request):
        objects = ('Random', 'Names', 'Will','Go','Here')
        y_pos = np.arange(len(objects))
        performance = [10,8,6,4,2]
        canvas = plt.figure(1)
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Number of followers')
        plt.title('Most popular authors in study')
        FigureCanvas(canvas)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(canvas)
        response = HttpResponse(buf.getvalue(), content_type='image/png')
        return response

def display_ment_accounts(request):
        objects = ('Random', 'TwitterIds', 'Will','Go','Here')
        y_pos = np.arange(len(objects))
        performance = [10,8,6,4,2]
        canvas = plt.figure(1)
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Number of mentions')
        plt.title('Most mentioned accounts in study')
        FigureCanvas(canvas)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(canvas)
        response = HttpResponse(buf.getvalue(), content_type='image/png')
        return response

def display_lang(request):
        objects = ('Different', 'Languages', 'Will','Go','Here')
        y_pos = np.arange(len(objects))
        performance = [10,8,6,4,2]
        canvas = plt.figure(1)
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Number of tweets')
        plt.title('Most used laguages in a study')
        FigureCanvas(canvas)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(canvas)
        response = HttpResponse(buf.getvalue(), content_type='image/png')
        return response

def display_device(request):
        objects = ('Different', 'Devices', 'Will','Go','Here')
        y_pos = np.arange(len(objects))
        performance = [10,8,6,4,2]
        canvas = plt.figure(1)
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Number of tweets')
        plt.title('Most used devices in a study')
        FigureCanvas(canvas)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(canvas)
        response = HttpResponse(buf.getvalue(), content_type='image/png')
        return response

def display_location(request):
        objects = ('Different', 'Locations', 'Will','Go','Here')
        y_pos = np.arange(len(objects))
        performance = [10,8,6,4,2]
        canvas = plt.figure(1)
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Number of tweets')
        plt.title('Most common tweet locations in a study')
        FigureCanvas(canvas)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(canvas)
        response = HttpResponse(buf.getvalue(), content_type='image/png')
        return response


