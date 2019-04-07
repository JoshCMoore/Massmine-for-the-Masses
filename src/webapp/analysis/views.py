# analysis/views.py


import enchant
import string
import re
import os
import tempfile
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt; plt.rcdefaults()
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from django_tables2 import RequestConfig
import django_tables2
import io

from analysis.models import Study
from query.models import Tweet
from django.views.generic.base import TemplateView
import plotly
from plotly import tools as tls
import plotly.offline
import plotly.graph_objs
from pytz import timezone
from collections import defaultdict
from textblob import TextBlob
title = ''
studyId = ''

@login_required
class BarGraph(TemplateView):
        template_name = 'graphH.html'
       
        def __init__(self, name):
               self.name = name

        def get_context_data(self, **kwargs):	
                context = super().get_context_data(**kwargs)
                stopFile = open('/home/momo/django/webapp/analysis/stopwords.txt','r')
                stopWords = stopFile.read().splitlines()
                stopList = set(stopWords)
                isNumber = re.compile('^[0-9]+$')
                global studyId
                list = Study.objects.all()
                offset = len(studyId)- 10
                addStop = studyId[:offset]
                alsoAddStop = addStop.lower()
                stopList.add(addStop)
                stopList.add(alsoAddStop)
                stopPlural = addStop + 's'
                stopList.add(stopPlural)
                stopPlural = addStop + '\'s'
                stopList.add(stopPlural)
                stopPlural = addStop + 's\''
                stopList.add(stopPlural)
                stopPlural = addStop.lower() + 's'
                stopList.add(stopPlural)
                stopPlural = addStop.lower() + '\'s'
                stopList.add(stopPlural)
                stopPlural = addStop.lower() + 's\''
                stopList.add(stopPlural)
                arr = []
                twList = Study.objects.get(study_id= studyId).tweets.all()


                for y in twList:
                     tempText = y.text
                     arr.append(tempText)
                texts = []
                d = enchant.Dict("en_US")
                isNumber = re.compile('^[0-9]+$') 
                for text in arr:
                    textwords = []
                    for word in text.lower().split():
                        word = re.sub(r'[^\w\s]','',word)
                        word = re.sub(r'\.+$','',word)
                        if word == '' or isNumber.search(word) == True or d.check(word) == False or word in addStop:
                            word = ''
                        if word not in stopList and word!='':
                            textwords.append(word)
                        texts.append(textwords)

                frequency = defaultdict(int)
                for text in texts:
                    for token in text:
                        frequency[token] += 1
                top5 = []
                numTimes = []
                for x in range(0,5):
                    topWord = sorted(frequency, key=frequency.get, reverse=True)[x]
                    numTimes.append(frequency[topWord])
                    top5.append(topWord)

                titleG = 'Most associated words with: ' + addStop
                data = [
                       plotly.graph_objs.Bar(
                            x=top5,
                            y=numTimes,
                            opacity = 0.5
                       )
                ]
                layout = plotly.graph_objs.Layout(
                       autosize=True,
                       title=titleG
                )

                plotly_fig = plotly.graph_objs.Figure(data=data, layout=layout) 
                div_fig = plotly.offline.plot(plotly_fig, auto_open=False, output_type='div')
                context['graph'] = div_fig
                return context

@login_required
class SentAnalysis(TemplateView):
        template_name = 'graphH.html'

        def __init__(self, name):
               self.name = name

        def get_context_data(self, **kwargs):	
                context = super().get_context_data(**kwargs)
                global studyId
                list = Study.objects.all()
                offset = len(studyId)- 10
                keyWord = studyId[:offset]
                arr = []
                twList = Study.objects.get(study_id = studyId).tweets.all()

                pos = 0
                neg = 0
                neutral = 0 
                for y in twList:
                     tempText = y.text
                     arr.append(tempText)
                for x in arr:
                     tb = TextBlob(x)
                     if tb.sentiment[0]<0:
                         neg += 1 
                     elif tb.sentiment[0]==0:
                         neutral += 1
                     else:              
                         pos +=1

                analysis = [pos,neg,neutral]                 

                titleG = 'Overall sentiment of: ' + keyWord
                data = [
                       plotly.graph_objs.Bar(
                            x=['positive','negative','neutral'],
                            y=analysis,
                            opacity = 0.5
                       )
                ]
                layout = plotly.graph_objs.Layout(
                       autosize=True,
                       title=titleG
                )

                plotly_fig = plotly.graph_objs.Figure(data=data, layout=layout) 
                div_fig = plotly.offline.plot(plotly_fig, auto_open=False, output_type='div')
                context['graph'] = div_fig
                return context

@login_required
def sent_analysis(request):
    global studyId
    studyId = request.POST['study_select']
    title = 'Sentiment Analysis'
    g = SentAnalysis(request)
    context = g.get_context_data()
    return render(request, 'analysis/graph.html', context)

@login_required
def freq_word(request):
    global studyId
    studyId = request.POST['study_select']
    title = 'Frequent Words'
    g = BarGraph(request)
    context = g.get_context_data()
    return render(request, 'analysis/graph.html', context)

@login_required
def graph(request):
    g = Graph(request)
    context = g.get_context_data()
    return render(request, 'analysis/graph.html', context)

       
class StudyTable(django_tables2.Table):
	class Meta:
		model = Tweet
		template_name = 'django_tables2/bootstrap.html'


def get_study(request):
	studyid = request.POST['study_select']
	current_study = StudyTable(Study.objects.get(study_id=studyid).tweets.all())
	RequestConfig(request, paginate=False).configure(current_study)
	return render(request, 'analysis/get_study.html', locals())

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
	if answer == "tweet_sent":
		return sent_analysis(request)
	elif answer == "freq_words":
		return freq_word(request)
	elif answer == "date":
		return graph(request)
	elif answer == "view_tweets":
		return get_study(request)
	else:
		return HttpResponse("Error")

"""
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

"""
