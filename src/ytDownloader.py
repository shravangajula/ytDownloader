from pytube import YouTube 
from sys import argv
import os

# Check if URL is provided
if len(argv) < 5:
    print("Error: Please provide a YouTube URL")
    print("Usage: python3 ytDownloader.py [YouTube URL]")
    exit(1)

# Get URL from command line argument
link = argv[1] 

try:
    # Create YouTube object with additional parameters to avoid HTTP errors
    yt = YouTube(
        link,
        use_oauth=False,
        allow_oauth_cache=True
    )
    
    # Ensure the download directory exists
    download_path = '/Users/userid/Documents/FolderName/SubFolderName'
    os.makedirs(download_path, exist_ok=True)
    
    print("Fetching video information...")
    
    # Try to get video information
    try:
        print("Title:", yt.title)
        print("Views:", yt.views)
    except:
        print("Could not fetch video details, but will try to download anyway.")
    
    print("Getting available streams...")
    
    # Get all streams and find the best one
    streams = yt.streams.filter(progressive=True)
    
    if not streams:
        print("No progressive streams found. Trying to find any available stream...")
        streams = yt.streams.filter(file_extension='mp4')
    
    if not streams:
        print("No streams available for this video.")
        exit(1)
    
    # Get the highest resolution available
    highest_res_stream = streams.get_highest_resolution()
    
    if highest_res_stream:
        print(f"Found stream: {highest_res_stream.resolution}, {highest_res_stream.mime_type}")
        print(f"Downloading to: {download_path}")
        
        # Download the video
        file_path = highest_res_stream.download(download_path)
        
        print(f"Download completed! File saved at: {file_path}")
    else:
        print("Could not find a suitable stream to download.")
    
except Exception as e:
    print(f"An error occurred: {e}")
    print("This might be due to YouTube API changes or restrictions.")
    print("Try updating pytube with: pip install --upgrade pytube")
