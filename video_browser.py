"""
Video browsing functionality using Qwen VL model
"""

import os
import cv2
from typing import List, Dict, Any, Optional
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import torch
import config


class VideoBrowser:
    """
    Video browser using Qwen VL model for understanding and analyzing video content
    """
    
    def __init__(self, model_name: str = None, device: str = None):
        """
        Initialize the video browser with Qwen VL model
        
        Args:
            model_name: Name of the Qwen VL model to use
            device: Device to run the model on (cuda/cpu)
        """
        self.model_name = model_name or config.QWEN_MODEL_NAME
        self.device = device or config.DEVICE
        self.model = None
        self.tokenizer = None
        
    def load_model(self):
        """Load the Qwen VL model and tokenizer"""
        print(f"Loading Qwen VL model: {self.model_name}")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_name, 
                trust_remote_code=True
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                device_map=self.device,
                trust_remote_code=True,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
            ).eval()
            print("Model loaded successfully!")
        except Exception as e:
            print(f"Error loading model: {e}")
            print("Note: You may need to install additional dependencies or use a different model")
            raise
    
    def extract_frames(self, video_path: str, num_frames: int = None) -> List[Image.Image]:
        """
        Extract frames from a video file
        
        Args:
            video_path: Path to the video file
            num_frames: Number of frames to extract (default from config)
            
        Returns:
            List of PIL Image objects
        """
        num_frames = num_frames or config.MAX_FRAMES
        
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
        
        # Open video
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video: {video_path}")
        
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        print(f"Video info: {total_frames} frames, {fps} fps")
        
        # Calculate frame indices to sample
        if total_frames <= num_frames:
            frame_indices = list(range(total_frames))
        else:
            # Sample frames evenly throughout the video
            step = total_frames // num_frames
            frame_indices = [i * step for i in range(num_frames)]
        
        frames = []
        for idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if ret:
                # Convert BGR to RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Convert to PIL Image
                pil_image = Image.fromarray(frame_rgb)
                # Resize if needed
                if pil_image.size[0] > config.MAX_IMAGE_SIZE[0] or pil_image.size[1] > config.MAX_IMAGE_SIZE[1]:
                    pil_image.thumbnail(config.MAX_IMAGE_SIZE, Image.Resampling.LANCZOS)
                frames.append(pil_image)
        
        cap.release()
        print(f"Extracted {len(frames)} frames from video")
        return frames
    
    def browse_video(self, video_path: str, query: str = None) -> Dict[str, Any]:
        """
        Browse and analyze video content
        
        Args:
            video_path: Path to the video file
            query: Optional query to ask about the video
            
        Returns:
            Dictionary containing analysis results
        """
        if self.model is None:
            self.load_model()
        
        # Check file extension
        _, ext = os.path.splitext(video_path.lower())
        if ext not in config.VIDEO_SUPPORTED_FORMATS:
            return {
                "success": False,
                "error": f"Unsupported video format: {ext}. Supported: {config.VIDEO_SUPPORTED_FORMATS}"
            }
        
        # Default query if none provided
        if query is None:
            query = "Please describe what's happening in this video."
        
        try:
            # Extract frames from video
            frames = self.extract_frames(video_path)
            
            if not frames:
                return {
                    "success": False,
                    "error": "No frames could be extracted from the video"
                }
            
            # Save frames temporarily for Qwen VL to process
            temp_frame_paths = []
            temp_dir = "/tmp/qwen_video_frames"
            os.makedirs(temp_dir, exist_ok=True)
            
            for i, frame in enumerate(frames):
                temp_path = os.path.join(temp_dir, f"frame_{i}.jpg")
                frame.save(temp_path)
                temp_frame_paths.append(temp_path)
            
            # Create query with multiple images
            query_with_images = query
            for i, frame_path in enumerate(temp_frame_paths):
                query_with_images = f"<img>{frame_path}</img> " + query_with_images
            
            # Generate response using Qwen VL
            response, history = self.model.chat(
                self.tokenizer,
                query=query_with_images,
                history=None
            )
            
            # Clean up temp files
            for temp_path in temp_frame_paths:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
            
            return {
                "success": True,
                "query": query,
                "response": response,
                "num_frames_analyzed": len(frames),
                "video_path": video_path
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "query": query
            }
    
    def browse_image(self, image_path: str, query: str = None) -> Dict[str, Any]:
        """
        Browse and analyze a single image
        
        Args:
            image_path: Path to the image file
            query: Optional query to ask about the image
            
        Returns:
            Dictionary containing analysis results
        """
        if self.model is None:
            self.load_model()
        
        # Default query if none provided
        if query is None:
            query = "Please describe what you see in this image."
        
        try:
            # Load and resize image if needed
            image = Image.open(image_path)
            if image.size[0] > config.MAX_IMAGE_SIZE[0] or image.size[1] > config.MAX_IMAGE_SIZE[1]:
                image.thumbnail(config.MAX_IMAGE_SIZE, Image.Resampling.LANCZOS)
            
            # Create query with image
            query_with_image = f"<img>{image_path}</img> {query}"
            
            # Generate response
            response, history = self.model.chat(
                self.tokenizer,
                query=query_with_image,
                history=None
            )
            
            return {
                "success": True,
                "query": query,
                "response": response,
                "image_path": image_path
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "query": query
            }
