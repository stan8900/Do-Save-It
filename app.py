import os
from pytube import YouTube
from TikTokApi import TikTokApi
import instaloader

def download_youtube_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(save_path)
        print(f'YouTube video downloaded: {stream.title}')
    except Exception as e:
        print(f"Error downloading YouTube video: {str(e)}")

def download_tiktok_video(url, save_path):
    try:
        api = TikTokApi()
        video = api.video(url=url)
        video_data = video.bytes()
        video_id = video.id
        file_path = os.path.join(save_path, f'tiktok_{video_id}.mp4')
        with open(file_path, 'wb') as f:
            f.write(video_data)
        print(f'TikTok video downloaded: {file_path}')
    except Exception as e:
        print(f"Error downloading TikTok video: {str(e)}")

def download_instagram_content(url, save_path):
    try:
        loader = instaloader.Instaloader(dirname_pattern=save_path)
        profile_name = url.split("/")[-2]
        loader.download_profile(profile_name, profile_pic_only=False)
        print(f'Instagram content downloaded for: {profile_name}')
    except Exception as e:
        print(f"Error downloading Instagram content: {str(e)}")

def download_content_from_url(url, save_path):
    if "youtube.com" in url or "youtu.be" in url:
        download_youtube_video(url, save_path)
    elif "tiktok.com" in url:
        download_tiktok_video(url, save_path)
    elif "instagram.com" in url:
        download_instagram_content(url, save_path)
    else:
        print("Unsupported platform. Please provide a valid YouTube, TikTok, or Instagram URL.")

save_path = './downloads'
os.makedirs(save_path, exist_ok=True)

url = input("Please provide the URL (YouTube, TikTok, or Instagram): ")

download_content_from_url(url, save_path)
