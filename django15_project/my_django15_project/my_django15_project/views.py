from django.shortcuts import render
import requests

#def home(request):
#    is_cached = ('resp_data' in request.session)
#    if not is_cached:
#        url = 'http://api.ipstack.com/171.78.248.55?access_key=bb46dbab39e26bc623b9cbc21f501f5e'
#        response = requests.get(url)
#        request.session['resp_data'] = response.json()

#    resp_data = request.session['resp_data']

#    return render(request, 'home.html', {
#            'ip': resp_data['ip'],
#            'latitude': resp_data['latitude'],
#            'longitude': resp_data['longitude'],
#            'country': resp_data['country_name'],
#            'is_cached': is_cached
#    })

def home(request):
#    is_cached = ('resp_data' in request.session)
#    if not is_cached:
    url = 'http://api.ipstack.com/171.78.248.55?access_key=bb46dbab39e26bc623b9cbc21f501f5e'
    response = requests.get(url)
    resp_data = response.json()

    return render(request, 'home.html', {
            'ip': resp_data['ip'],
            'latitude': resp_data['latitude'],
            'longitude': resp_data['longitude'],
            'country': resp_data['country_name']
    })
