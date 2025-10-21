#!/usr/bin/env python3
"""
Example script demonstrating video browsing with Qwen
"""

from video_browser import VideoBrowser
import os


def example_video_browsing():
    """Demonstrate video browsing capabilities"""
    
    # Initialize the video browser
    print("Initializing Qwen Video Browser...")
    browser = VideoBrowser()
    
    # Note: This example requires actual video files to work
    # Replace these paths with your actual video/image files
    
    print("\n" + "="*50)
    print("Example: Video/Image Browsing")
    print("="*50)
    
    # Example with a video file (you need to provide your own)
    video_path = "sample_video.mp4"  # Replace with actual path
    
    if os.path.exists(video_path):
        print(f"\nAnalyzing video: {video_path}")
        result = browser.browse_video(video_path, "What activities are shown in this video?")
        
        if result["success"]:
            print(f"\nQuery: {result['query']}")
            print(f"Response: {result['response']}")
            print(f"Frames analyzed: {result['num_frames_analyzed']}")
        else:
            print(f"Error: {result.get('error')}")
    else:
        print(f"\nVideo file not found: {video_path}")
        print("Please provide a valid video file path to test this feature.")
    
    # Example with an image file (you need to provide your own)
    image_path = "sample_image.jpg"  # Replace with actual path
    
    if os.path.exists(image_path):
        print(f"\n\nAnalyzing image: {image_path}")
        result = browser.browse_image(image_path, "Describe what you see in detail.")
        
        if result["success"]:
            print(f"\nQuery: {result['query']}")
            print(f"Response: {result['response']}")
        else:
            print(f"Error: {result.get('error')}")
    else:
        print(f"\nImage file not found: {image_path}")
        print("Please provide a valid image file path to test this feature.")
    
    print("\n" + "="*50)
    print("Note: This example requires actual video/image files.")
    print("Please update the paths in this script with your own files.")
    print("="*50)


if __name__ == "__main__":
    example_video_browsing()
