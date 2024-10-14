from pytube import YouTube

# Function to download video
def download_video(url, save_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Print video title
        print(f"Title: {yt.title}")
        
        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified path
        print("Downloading...")
        video_stream.download(output_path=save_path)
        
        print("Download completed!")
    
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the directory to save the video: ")
    
    download_video(video_url, save_path)
