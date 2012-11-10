#!/usr/bin/python
# Outputs a list of strings of the video IDs.
from apiclient.discovery import build
from optparse import OptionParser

# Set DEVELOPER_KEY to the "API key" value from the "Access" tab of the
# Google APIs Console http://code.google.com/apis/console#access
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyBfYR_vMb3llBT-SZqnOUFdLoEwSwi0idQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options, query):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    # q=options.q,
    q=query, 
    part="id,snippet",
    maxResults= 5
).execute()

  videos = []
  channels = []
  playlists = []
  video_idees=[]

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
      idee=search_result["id"]["videoId"]
      # print earch_result["id"]["videoId"]
      video_idees.append(str(idee))

    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))
  print video_idees
  # print "Videos:\n", "\n".join(videos), "\n"
  video_results="\n".join(videos)
  # print type(a), a
  # return video_results
  return  video_idees
  # print "Videos:\n", "\n".join(videos), "\n"
  # print "Channels:\n", "\n".join(channels), "\n"
  # print "Playlists:\n", "\n".join(playlists), "\n"

# if __name__ == "__main__":
#   parser = OptionParser()
#   parser.add_option("--q", dest="q", help="Search term",
#     default="Google")
#   parser.add_option("--max-results", dest="maxResults",
#     help="Max results", default=25)
#   (options, args) = parser.parse_args()

# Change the keyword search to change the search results. 
keyword_search="code training women"
#youtube_search(options,  keyword_search)