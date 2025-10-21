"""
Configuration settings for Qwen browsing application
"""

# Model configuration
QWEN_MODEL_NAME = "Qwen/Qwen-VL-Chat"  # Qwen Vision-Language model for multimodal tasks
DEVICE = "cuda"  # Use "cuda" for GPU or "cpu" for CPU

# Text browsing settings
MAX_TEXT_LENGTH = 4096  # Maximum text length for processing
CHUNK_SIZE = 2048  # Size of text chunks for large documents

# Video browsing settings
VIDEO_FRAME_SAMPLE_RATE = 30  # Sample 1 frame every N frames
MAX_FRAMES = 10  # Maximum number of frames to process per video
VIDEO_SUPPORTED_FORMATS = ['.mp4', '.avi', '.mov', '.mkv', '.flv']

# Image settings
IMAGE_SUPPORTED_FORMATS = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
MAX_IMAGE_SIZE = (1024, 1024)  # Maximum image dimensions

# Generation parameters
TEMPERATURE = 0.7
TOP_P = 0.9
MAX_NEW_TOKENS = 512
