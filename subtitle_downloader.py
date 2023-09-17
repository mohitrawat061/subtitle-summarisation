from youtube_transcript_api import YouTubeTranscriptApi

def get_subtitle(link):
    res = YouTubeTranscriptApi.get_transcript(link, languages=['en', 'en-US'])

    file1 = open("data.txt", "w")

    for entry in res:
        file1.write(" ".join(entry['text'].split()))