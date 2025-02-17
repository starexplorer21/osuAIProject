from pytubefix import Stream
from pytubefix import YouTube
from tqdm import tqdm


def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
    pbar.update(len(data_chunk))


url = "https://www.youtube.com/watch?v=jp4hS6bZS_c&list=PLowhkVroM7Z1xOPbDZpkxCfrarjZUqhck&index=14"
yt = YouTube(url, on_progress_callback=progress_callback, use_oauth=True, allow_oauth_cache=True)
stream = yt.streams.get_highest_resolution()
print(f"Downloading video to '{stream.default_filename}'")
pbar = tqdm(total=stream.filesize, unit="bytes")
path = stream.download(filename_prefix="/Users/Yile0/PycharmProjects/osutime/osuAIProject/video_clips/")
pbar.close()
print(f"Saved video to {path}")