# Quick Start Guide

Welcome to AI-Skate! This guide will help you get started quickly.

## Installation

1. Run the setup script:
```bash
./setup.sh
```

2. Activate the virtual environment:
```bash
source venv/bin/activate
```

## Quick Examples

### Interactive Mode (Recommended for First-Time Users)

```bash
python main.py
```

This will launch an interactive menu where you can:
- Browse text documents
- Analyze videos
- Process images

### Text Browsing

Create a sample text file:
```bash
cat > sample.txt << EOF
Artificial Intelligence is transforming the world.
Machine learning enables computers to learn from data.
Deep learning uses neural networks for complex tasks.
EOF
```

Browse it:
```bash
python main.py --file sample.txt --query "What is this about?"
```

### Running Examples

```bash
# Text browsing example
python examples/example_text.py

# Video browsing example (requires video files)
python examples/example_video.py
```

## Common Use Cases

### 1. Document Analysis
```bash
python main.py --file report.pdf.txt --query "Summarize the key findings"
```

### 2. Video Understanding
```bash
python main.py --file meeting_recording.mp4 --query "What was discussed?"
```

### 3. Image Description
```bash
python main.py --file photo.jpg --query "Describe the scene"
```

## Configuration

Edit `config.py` to customize:
- Model selection
- Device (GPU/CPU)
- Processing parameters
- Frame extraction settings

## Troubleshooting

### "Out of memory" errors
- Switch to CPU: Edit `config.py` and set `DEVICE = "cpu"`
- Reduce frames: Set `MAX_FRAMES = 5` in `config.py`

### Model download issues
- Ensure stable internet connection
- Check disk space (models can be several GB)
- May require Hugging Face account for some models

### Import errors
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version` (needs 3.8+)

## Next Steps

1. Try the interactive mode
2. Process your own files
3. Experiment with different queries
4. Adjust configuration for your needs

For more details, see the main README.md file.
