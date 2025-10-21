#!/usr/bin/env python3
"""
Main application for Qwen browsing - supports text and video browsing
"""

import argparse
import sys
import os
from text_browser import TextBrowser
from video_browser import VideoBrowser
import config


def browse_text_interactive():
    """Interactive text browsing mode"""
    browser = TextBrowser()
    
    print("\n=== Qwen Text Browser ===")
    print("Enter your text or path to a text file, then ask questions about it.")
    print("Type 'quit' to exit.\n")
    
    while True:
        print("\nOptions:")
        print("1. Browse text directly")
        print("2. Browse text file")
        print("3. Quit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '3' or choice.lower() == 'quit':
            print("Goodbye!")
            break
        
        elif choice == '1':
            print("\nEnter your text (press Enter twice when done):")
            lines = []
            while True:
                line = input()
                if line == "" and lines and lines[-1] == "":
                    break
                lines.append(line)
            text = "\n".join(lines[:-1])  # Remove last empty line
            
            if not text.strip():
                print("No text entered. Please try again.")
                continue
            
            query = input("\nWhat would you like to know about this text? (press Enter for summary): ").strip()
            if not query:
                query = None
            
            print("\nProcessing...")
            result = browser.browse_text(text, query)
            
            if result["success"]:
                print(f"\n--- Response ---")
                print(result["response"])
            else:
                print(f"\nError: {result.get('error', 'Unknown error')}")
        
        elif choice == '2':
            file_path = input("\nEnter path to text file: ").strip()
            
            if not os.path.exists(file_path):
                print(f"File not found: {file_path}")
                continue
            
            query = input("What would you like to know about this file? (press Enter for summary): ").strip()
            if not query:
                query = None
            
            print("\nProcessing...")
            result = browser.browse_file(file_path, query)
            
            if result["success"]:
                print(f"\n--- Response ---")
                print(result["response"])
            else:
                print(f"\nError: {result.get('error', 'Unknown error')}")
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def browse_video_interactive():
    """Interactive video browsing mode"""
    browser = VideoBrowser()
    
    print("\n=== Qwen Video Browser ===")
    print("Enter path to a video file or image to analyze it.")
    print("Type 'quit' to exit.\n")
    
    while True:
        print("\nOptions:")
        print("1. Browse video file")
        print("2. Browse image file")
        print("3. Quit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '3' or choice.lower() == 'quit':
            print("Goodbye!")
            break
        
        elif choice == '1':
            video_path = input("\nEnter path to video file: ").strip()
            
            if not os.path.exists(video_path):
                print(f"File not found: {video_path}")
                continue
            
            query = input("What would you like to know about this video? (press Enter for description): ").strip()
            if not query:
                query = None
            
            print("\nProcessing video...")
            result = browser.browse_video(video_path, query)
            
            if result["success"]:
                print(f"\n--- Response ---")
                print(result["response"])
                print(f"\nAnalyzed {result['num_frames_analyzed']} frames from the video.")
            else:
                print(f"\nError: {result.get('error', 'Unknown error')}")
        
        elif choice == '2':
            image_path = input("\nEnter path to image file: ").strip()
            
            if not os.path.exists(image_path):
                print(f"File not found: {image_path}")
                continue
            
            query = input("What would you like to know about this image? (press Enter for description): ").strip()
            if not query:
                query = None
            
            print("\nProcessing image...")
            result = browser.browse_image(image_path, query)
            
            if result["success"]:
                print(f"\n--- Response ---")
                print(result["response"])
            else:
                print(f"\nError: {result.get('error', 'Unknown error')}")
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Qwen Browsing Tool - Browse text and video content using Qwen AI"
    )
    parser.add_argument(
        '--mode',
        choices=['text', 'video', 'auto'],
        default='auto',
        help='Browsing mode (default: auto)'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='File to browse'
    )
    parser.add_argument(
        '--query',
        type=str,
        help='Question to ask about the content'
    )
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Run in interactive mode'
    )
    
    args = parser.parse_args()
    
    # Interactive mode
    if args.interactive or (not args.file and not args.query):
        if args.mode == 'text':
            browse_text_interactive()
        elif args.mode == 'video':
            browse_video_interactive()
        else:
            print("\n=== Qwen Browsing Tool ===")
            print("Choose a browsing mode:")
            print("1. Text Browser")
            print("2. Video/Image Browser")
            choice = input("\nEnter your choice (1-2): ").strip()
            
            if choice == '1':
                browse_text_interactive()
            elif choice == '2':
                browse_video_interactive()
            else:
                print("Invalid choice.")
                sys.exit(1)
        return
    
    # File-based mode
    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: File not found: {args.file}")
            sys.exit(1)
        
        # Determine file type
        _, ext = os.path.splitext(args.file.lower())
        
        if ext in config.VIDEO_SUPPORTED_FORMATS:
            print(f"Browsing video: {args.file}")
            browser = VideoBrowser()
            result = browser.browse_video(args.file, args.query)
        elif ext in config.IMAGE_SUPPORTED_FORMATS:
            print(f"Browsing image: {args.file}")
            browser = VideoBrowser()
            result = browser.browse_image(args.file, args.query)
        else:
            print(f"Browsing text file: {args.file}")
            browser = TextBrowser()
            result = browser.browse_file(args.file, args.query)
        
        if result["success"]:
            print("\n--- Response ---")
            print(result["response"])
        else:
            print(f"\nError: {result.get('error', 'Unknown error')}")
            sys.exit(1)


if __name__ == "__main__":
    main()
