from youtube_dl import YoutubeDL

#1. Tai 1 video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=uAsV5-Hv-7U'])

#2. Tai nhieu video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=o5IXgZVmV6U', 'https://www.youtube.com/watch?v=Qs-XcmaxaLw'])

#3. Tai audio
# options = {
#     'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=JcOwJh4F40M'])

#4. Tim kiem va tai video dau tien
# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1 # Tell downloader to download only the first entry (video)
# }
# dl = YoutubeDL(options)
# dl.download(['In the End'])

#5. Tim kiem va tai audio dau tien
options = {
    'default_search' : 'ytsearch',
    'max_downloads' : 1,
    'format' : 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Californication'])