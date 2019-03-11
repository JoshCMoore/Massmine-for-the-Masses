# analysis/views.py


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
import io


@login_required
def analysis(request):
    return render(request, 'analysis/analysis.html', {})

@login_required
def create_analysis(request):
	answer = request.POST['analysis_select']
	if answer == "tweet_type":
		return display_tweet_type(request)
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
		#ten newest and oldest?
		return HttpResponse("date?")
	elif answer == "times_retweeted":
		return display_times_retweeted(request)
	elif answer == "times_favorited":
		return display_times_favorited(request)
	elif answer == "location":
		return display_location(request)
	else:
		return HttpResponse("Error")

def display_times_retweeted(request):
        if request.method == 'POST':
                x = np.random.randn(100000)
                f = plt.figure(111)
                plt.hist(x, color='lightblue')
                plt.xlabel('X')
                plt.ylabel('Frequency')
                plt.title('Histogram of Retweets in a Study')
                FigureCanvas(f)
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                plt.close(f)
                response = HttpResponse(buf.getvalue(), content_type='image/png')
                return response
        else:
                return HttpResponse("I'll add error handling here.")

def display_times_favorited(request):
        if request.method == 'POST':
                x = np.random.randn(100000)
                f = plt.figure(111)
                plt.hist(x, color='lightblue')
                plt.xlabel('X')
                plt.ylabel('Frequency')
                plt.title('Histogram of favorites in a Study')
                FigureCanvas(f)
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                plt.close(f)
                response = HttpResponse(buf.getvalue(), content_type='image/png')
                return response
        else:
                return HttpResponse("I'll add error handling here.")


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


