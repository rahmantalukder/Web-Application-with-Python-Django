from pytubefix import YouTube
import sys

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = (bytes_downloaded / total_size) * 100
    sys.stdout.write(f"\r⬇️ Downloading... {progress:.2f}%")
    sys.stdout.flush()

url = input("Enter your YouTube link: ").strip()

try:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"\n🎬 Title: {yt.title}")
    stream = yt.streams.get_highest_resolution()
    print("📥 Starting download...")
    stream.download()
    print("\n✅ Download Completed Successfully!")
except Exception as e:
    print("\n❌ Error:", e)
