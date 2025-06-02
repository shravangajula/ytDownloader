import sys
import os
import subprocess

def list_formats(url):
    """
    List all available formats for the given URL
    """
    print(f"Available formats for: {url}")
    cmd = ['yt-dlp', '-F', url]
    
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
    
    os.makedirs(output_path, exist_ok=True)
    
    output_template = os.path.join(output_path, '%(title)s.%(ext)s')

    cmd = [
        'yt-dlp',
        url,
        '-f', format_code if format_code else '22/18/best',  # Default formats fallback
        '--audio-quality', '0',
        '-o', output_template,
        '--no-playlist',
        '--verbose',
        '--progress'
    ]
    
    try:
        subprocess.run(cmd, check=True, text=True)
        print("\n✅ Download completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error during download: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python yt_downloader.py [YouTube URL] [optional: format code or --list-formats] [optional: output directory]")
        sys.exit(1)

    url = sys.argv[1]

    # Handle list-formats option
    if len(sys.argv) > 2 and sys.argv[2] == "--list-formats":
        list_formats(url)
        sys.exit(0)

    # Optional format code
    format_code = sys.argv[2] if len(sys.argv) > 2 else None

    # Optional output directory
    output_dir = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.getcwd(), 'YouTubeDownloads')

    # Run the download
    download_video(url, output_dir, format_code)
