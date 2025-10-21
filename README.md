# AI-Skate: Qwen Browsing Tool

AI-Skate is a powerful tool that leverages the Qwen Vision-Language model to browse and analyze both text and video content. It provides an intuitive interface for understanding documents, videos, and images using advanced AI capabilities.

## Features

- **Text Browsing**: Analyze and ask questions about text documents
- **Video Browsing**: Extract insights from video content by analyzing key frames
- **Image Analysis**: Understand and describe image content
- **Interactive Mode**: User-friendly interactive interface for exploration
- **Batch Processing**: Process files via command-line arguments
- **Flexible Queries**: Ask custom questions or get automatic summaries

## Installation

### Prerequisites

- Python 3.8 or higher
- CUDA-compatible GPU (recommended for optimal performance)
- At least 16GB RAM (32GB recommended for video processing)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/danutaparaficz2/ai-skate.git
cd ai-skate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Configure settings in `config.py` to match your hardware capabilities.

## Usage

### Interactive Mode

Run the main application in interactive mode:

```bash
python main.py --interactive
```

Or simply:

```bash
python main.py
```

This will present you with a menu to choose between text or video browsing.

### Command-Line Mode

#### Browse a Text File

```bash
python main.py --file document.txt --query "What is the main topic of this document?"
```

#### Browse a Video File

```bash
python main.py --file video.mp4 --query "What activities are shown in this video?"
```

#### Browse an Image File

```bash
python main.py --file image.jpg --query "Describe the scene in detail"
```

### Examples

The `examples/` directory contains sample scripts:

```bash
# Text browsing example
python examples/example_text.py

# Video browsing example (requires video/image files)
python examples/example_video.py
```

## API Usage

### Text Browsing

```python
from text_browser import TextBrowser

# Initialize browser
browser = TextBrowser()

# Browse text
result = browser.browse_text(
    "Your text content here",
    query="What are the key points?"
)

if result["success"]:
    print(result["response"])

# Browse a file
result = browser.browse_file("document.txt", query="Summarize this")
```

### Video Browsing

```python
from video_browser import VideoBrowser

# Initialize browser
browser = VideoBrowser()

# Analyze a video
result = browser.browse_video(
    "video.mp4",
    query="What is happening in this video?"
)

if result["success"]:
    print(result["response"])
    print(f"Analyzed {result['num_frames_analyzed']} frames")

# Analyze an image
result = browser.browse_image(
    "image.jpg",
    query="Describe what you see"
)
```

## Configuration

Edit `config.py` to customize settings:

- **QWEN_MODEL_NAME**: Change the Qwen model variant
- **DEVICE**: Set to "cuda" for GPU or "cpu" for CPU
- **MAX_TEXT_LENGTH**: Maximum text length to process
- **MAX_FRAMES**: Number of frames to extract from videos
- **VIDEO_FRAME_SAMPLE_RATE**: Frame sampling rate
- **TEMPERATURE**: Model generation temperature (creativity)

## Supported Formats

### Text Files
- .txt, .md, .log, and other plain text formats

### Video Files
- .mp4, .avi, .mov, .mkv, .flv

### Image Files
- .jpg, .jpeg, .png, .bmp, .gif

## Architecture

The project consists of the following components:

- **config.py**: Configuration settings
- **text_browser.py**: Text browsing functionality
- **video_browser.py**: Video and image browsing functionality
- **main.py**: Main application with CLI and interactive modes
- **examples/**: Example scripts demonstrating usage

## Performance Tips

1. **GPU Acceleration**: Use a CUDA-compatible GPU for faster processing
2. **Video Processing**: Reduce `MAX_FRAMES` in config for faster video analysis
3. **Large Documents**: Text is automatically truncated to `MAX_TEXT_LENGTH`
4. **Batch Processing**: Process multiple files using shell scripts with the CLI interface

## Troubleshooting

### Out of Memory Errors

- Reduce `MAX_FRAMES` in config.py
- Use CPU instead of GPU (slower but uses less memory)
- Process shorter videos or images only

### Model Loading Issues

- Ensure you have enough disk space for model downloads
- Check your internet connection for initial model download
- Verify transformers library is properly installed

### Video Processing Errors

- Ensure OpenCV is properly installed: `pip install opencv-python`
- Check that the video file is not corrupted
- Try converting the video to a supported format (MP4 recommended)

## License

This project uses the Qwen model, which is subject to its own license terms. Please refer to the [Qwen model card](https://huggingface.co/Qwen/Qwen-VL-Chat) for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Acknowledgments

- Built with [Qwen-VL](https://github.com/QwenLM/Qwen-VL) by Alibaba Cloud
- Uses [Transformers](https://github.com/huggingface/transformers) by Hugging Face
- Video processing powered by [OpenCV](https://opencv.org/)