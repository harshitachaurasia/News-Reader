#newspaper pdhke sunao
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)
if __name__ == "__main__":
    import requests
    import json
    url = ('http://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=6dd699e52aff457fbdc96c35835a28d6')
    response = requests.get(url)
    text = response.text
    m_json = json.loads(text)
    for i in range(0,11):
        speak(m_json['articles'][i]['title'])

