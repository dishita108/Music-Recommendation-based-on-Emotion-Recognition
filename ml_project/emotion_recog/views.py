from django.shortcuts import render,redirect
from pandas import *
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from musicemotion import *
from helpers import *

def predict_mood(id_song):
    #Join the model and the scaler in a Pipeline
    pip = Pipeline([('minmaxscaler',MinMaxScaler()),('keras',KerasClassifier(build_fn=base_model,epochs=300,
                                                                             batch_size=200,verbose=0))])
    #Fit the Pipeline
    pip.fit(X2,encoded_y)
    
    #Obtain the features of the song
    preds = get_songs_features(id_song)
    #Pre-process the features to input the Model
    preds_features = np.array(preds[0][6:-2]).reshape(-1,1).T

    #Predict the features of the song
    results = pip.predict(preds_features)
    name_r=[]
    album_r=[]
    artist_r=[]
    urls_r=[]
    mood = np.array(target['mood'][target['encode']==int(results)])
    name_song = preds[0][0]
    artist = preds[0][2]
    print("{0} by {1} is a {2} song".format(name_song,artist,mood[0].upper()))
    if mood[0].upper()=='HAPPY':
        id='4VQMOVhJP7xEKM1y5H4YQM'
        endpoint_p="https://open.spotify.com/embed/playlist/"
        lookup_playlist=f"{endpoint_p}{id}"
        print("\nRecommended playlist of ENERGETIC songs is : ")
        msg = "Recommended playlist of ENERGETIC songs is : "
        print(lookup_playlist)
        print()
        data = read_csv("songs/happy.csv",nrows = 10)
        name_r = data['Name'].tolist()
        album_r = data['Album'].tolist()
        artist_r = data['Artist'].tolist()
        urls_r = []
        for x in name_r:
            sid = get_song_id(x)
            urls_r.append(sid['tracks']['items'][0]['external_urls']['spotify'])
        #for i in range(0,10):

    elif mood[0].upper()=='ENERGETIC':
        id='4VQMOVhJP7xEKM1y5H4YQM'
        endpoint_p="https://open.spotify.com/embed/playlist/"
        lookup_playlist=f"{endpoint_p}{id}"
        print("\nRecommended playlist of ENERGETIC songs is : ")
        msg = "Recommended playlist of ENERGETIC songs is : "
        print(lookup_playlist)
        print()
        data = read_csv("songs/surprised.csv",nrows = 10)
        name_r = data['Name'].tolist()
        album_r = data['Album'].tolist()
        artist_r = data['Artist'].tolist()
        urls_r = []
        for x in name_r:
            sid = get_song_id(x)
            urls_r.append(sid['tracks']['items'][0]['external_urls']['spotify'])


    elif mood[0].upper()=='SAD':
        id='0P5kYTgLdhrMq8UsEg4aYL'
        endpoint_p="https://open.spotify.com/embed/playlist/"
        lookup_playlist=f"{endpoint_p}{id}"
        print("\nRecommended playlist of RELAXING songs is : ")
        msg = "Recommended playlist of RELAXING songs is : "
        print(lookup_playlist)
        data = read_csv("songs/sad.csv",nrows = 10)
        name_r = data['Name'].tolist()
        album_r = data['Album'].tolist()
        artist_r = data['Artist'].tolist()
        urls_r = []
        for x in name_r:
            sid = get_song_id(x)
            urls_r.append(sid['tracks']['items'][0]['external_urls']['spotify'])
    
    else:
        id='0P5kYTgLdhrMq8UsEg4aYL'
        endpoint_p="https://open.spotify.com/embed/playlist/"
        lookup_playlist=f"{endpoint_p}{id}"
        print("\nRecommended playlist of RELAXING songs is : ")
        msg = "Recommended playlist of RELAXING songs is : "
        print(lookup_playlist)
        data = read_csv("songs/neutral.csv",nrows = 10)
        name_r = data['Name'].tolist()
        album_r = data['Album'].tolist()
        artist_r = data['Artist'].tolist()
        urls_r = []
        for x in name_r:
            sid = get_song_id(x)
            urls_r.append(sid['tracks']['items'][0]['external_urls']['spotify'])
    
    combined = zip(name_r,album_r,artist_r,urls_r)
    #'name_r':name_r,'album_r':album_r,'artist_r':artist_r,'urls_r':urls_r,'nums':nums
    return({'name_song':name_song,'artist':artist,'emotion':mood[0].upper(),'lookup_playlist':lookup_playlist,'msg':msg,'combined':combined})


def music_emotion(request):
    if request.method == 'POST':
        song_name = request.POST['SongName']
        id = get_song_id(song_name)
        final_id = id['tracks']['items'][0]['id']
        print(final_id)
        context = {}
        context = predict_mood(final_id)
        return render(request,'success.html',context)
    return render(request,'index.html')

def music_home(request):
    return render(request,'index.html')