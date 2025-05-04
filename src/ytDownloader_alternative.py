import sys
import os
import subprocess

def list_formats(url):
    """
    List all available formats for the given URL
    """
    print(f"Available formats for: {url}")
    
    cmd = [
        'yt-dlp', 
        '-F',
        url
    ]
    
    try:
        subprocess.run(cmd, check=True, text=True)
    except Exception as e:
        print(f"Error listing formats: {e}")

def download_video(url, output_path, format_code=None):
    """
    Download a YouTube video using yt-dlp
    """
    print(f"Attempting to download: {url}")
    print(f"Output directory: {output_path}")
    
    # Ensure output directory exists
    os.makedirs(output_path, exist_ok=True)
    
    # Format the output path with template for filename
    output_template = os.path.join(output_path, '%(title)s.%(ext)s')
    
    # Build the command
    cmd = [
        'yt-dlp',
        url,
    ]
    
    # Add format selection based on whether a specific format was requested
    if format_code:
        cmd.extend(['-f', format_code])
    else:
        cmd.extend(['-f', '22/18/best'])  # Try standard HD format (22) first, then fallback to others
    
    # Add remaining options
    cmd.extend([
        '--audio-quality', '0',  # Best audio quality
        '-o', output_template,
        '--no-playlist',  # Don't download playlists
        '--verbose',  # Show verbose output for debugging
        '--progress'  # Show progress
    ])
    
    try:
        # Run the command
        process = subprocess.run(cmd, check=True, text=True)
        print("\nDownload completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nError during download: {e}")
        return False
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        return False

if __name__ == "__main__":
    # Check if URL is provided
    if len(sys.argv) < 2:
        print("Error: Please provide a YouTube URL")
        print("Usage: python yt_downloader_alternative.py [YouTube URL] [optional: format code]")
        sys.exit(1)
    
    # Get URL from command line argument
    url = sys.argv[1]
    
    # Check if we should just list formats
    if len(sys.argv) > 2 and sys.argv[2] == "--list-formats":
        list_formats(url)
        sys.exit(0)
    
    # Check if format code is provided
    format_code = None
    if len(sys.argv) > 2:
        format_code = sys.argv[2]
    
    # Download path
    download_path = '/Users/shravankumargajula/Documents/My Folder/YouTubeDownloader'
    
    # Download the video
    download_video(url, download_path, format_code)
