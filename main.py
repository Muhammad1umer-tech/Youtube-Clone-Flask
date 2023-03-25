from flask import Flask, render_template
import requests

app = Flask(__name__)

CHANNELS = {
  'qazi': 'UCqrILQNl5Ed9Dz6CGMyvMTQ',
  'mrbeast': 'UCX6OQ3DkcsbYNE6H8uQQuVA',
  'mkbhd': 'UCBJycsmduvYEL83R_U4JriQ',
  'pm': 'UC3DkFux8Iv-aYnTRWzwaiBA',
}

data = {
        'content': [
          {
            'type': 'video', 
            'video': {
                    'thumbnails': [
                    {
                      'url': 'blah'
                    }
                    ],
                    'title': 'Build Titter Web3 Clone with React Native!',
                    'isliveNow': False, 
                   },
          },
        ],
        'cursorNext': 'blah'
       }
# print(data['content'][0]['video']['title'])



@app.route('/')
def index():
  url = "https://youtube138.p.rapidapi.com/channel/videos/"

  querystring = {"id":CHANNELS['qazi'],"hl":"en","gl":"US"}

  headers = {
	 "X-RapidAPI-Key": "16d3a267c2mshf26389efcb7ee35p1a5c11jsn35300d49cd7b",
	 "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = response.json()
  contents = data['contents'];
  video = [con['video'] for con in contents if con['video']['publishedTimeText']]
  print(video)
  
  return render_template('index.html', videos = video)
  
app.run(host='0.0.0.0', port=81)