# Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         AI-Skate System                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────┐              ┌──────────────────┐        │
│  │ Interactive Mode │              │   CLI Mode       │        │
│  │  (main.py)       │              │  (main.py)       │        │
│  └──────────────────┘              └──────────────────┘        │
│           │                                 │                   │
│           └─────────────┬───────────────────┘                   │
│                         │                                       │
└─────────────────────────┼───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Application Layer                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────┐       ┌──────────────────────┐       │
│  │   TextBrowser        │       │   VideoBrowser       │       │
│  │  (text_browser.py)   │       │  (video_browser.py)  │       │
│  │                      │       │                      │       │
│  │ • browse_text()      │       │ • browse_video()     │       │
│  │ • browse_file()      │       │ • browse_image()     │       │
│  │ • ask_question()     │       │ • extract_frames()   │       │
│  │ • load_model()       │       │ • load_model()       │       │
│  └──────────────────────┘       └──────────────────────┘       │
│           │                                 │                   │
│           └─────────────┬───────────────────┘                   │
│                         │                                       │
└─────────────────────────┼───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Model Layer                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │            Qwen/Qwen-VL-Chat Model                       │  │
│  │         (HuggingFace Transformers)                       │  │
│  │                                                          │  │
│  │  • Text Understanding & Generation                      │  │
│  │  • Image Analysis                                       │  │
│  │  • Vision-Language Reasoning                            │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Data Processing Layer                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   OpenCV     │  │     PIL      │  │ Text Files   │         │
│  │ (Video       │  │ (Image       │  │ (Documents)  │         │
│  │  Processing) │  │  Processing) │  │              │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Configuration Layer (`config.py`)
- Central configuration management
- Model selection
- Device configuration (GPU/CPU)
- Processing parameters
- Format specifications

### 2. Application Layer

#### TextBrowser (`text_browser.py`)
**Purpose**: Analyze and understand text content

**Key Methods**:
- `load_model()`: Initialize Qwen model
- `browse_text(text, query)`: Analyze text with custom query
- `browse_file(file_path, query)`: Analyze text file
- `ask_question(text, question)`: Q&A interface

**Features**:
- Automatic text truncation for large documents
- UTF-8 encoding support
- Error handling and recovery

#### VideoBrowser (`video_browser.py`)
**Purpose**: Analyze video and image content

**Key Methods**:
- `load_model()`: Initialize Qwen VL model
- `extract_frames(video_path, num_frames)`: Extract key frames
- `browse_video(video_path, query)`: Analyze video content
- `browse_image(image_path, query)`: Analyze single image

**Features**:
- Smart frame sampling (evenly distributed)
- Automatic image resizing
- Multiple format support
- Temporary frame storage

### 3. User Interface Layer

#### Interactive Mode
- Step-by-step guided workflow
- Menu-driven interface
- Options for text or video browsing
- Input validation and error handling

#### CLI Mode
- Direct file processing
- Command-line arguments
- Auto-detection of file type
- Batch processing support

### 4. Model Integration

**Qwen Model**:
- Vision-Language model from Alibaba Cloud
- Supports both text and image understanding
- Hosted on HuggingFace
- Loaded via Transformers library

**Processing Flow**:
1. User provides input (text/video/image)
2. Application layer processes input
3. Model layer performs inference
4. Results returned to user

## Data Flow

### Text Browsing Flow
```
User Input → TextBrowser → Qwen Model → Response
    ↓
[Text/File] → [Load & Process] → [Generate] → [Display]
```

### Video Browsing Flow
```
User Input → VideoBrowser → Frame Extraction → Qwen VL → Response
    ↓              ↓              ↓              ↓
[Video File] → [Load Video] → [Extract] → [Analyze] → [Display]
                               [Frames]    [w/ Model]
```

## File Organization

```
ai-skate/
├── Core Application
│   ├── config.py           # Configuration
│   ├── text_browser.py     # Text analysis
│   ├── video_browser.py    # Video/image analysis
│   └── main.py             # Main application
│
├── Setup & Installation
│   ├── requirements.txt    # Dependencies
│   └── setup.sh            # Installation script
│
├── Documentation
│   ├── README.md           # User guide
│   ├── QUICKSTART.md       # Quick start
│   ├── IMPLEMENTATION.md   # Technical summary
│   └── ARCHITECTURE.md     # This file
│
├── Examples & Testing
│   ├── examples/
│   │   ├── example_text.py
│   │   └── example_video.py
│   └── test_structure.py
│
└── Configuration
    └── .gitignore
```

## Technology Stack

- **Language**: Python 3.8+
- **ML Framework**: PyTorch
- **Model Library**: HuggingFace Transformers
- **Video Processing**: OpenCV
- **Image Processing**: PIL/Pillow
- **Model**: Qwen/Qwen-VL-Chat

## Design Principles

1. **Modularity**: Separate concerns (text vs video, UI vs logic)
2. **Flexibility**: Multiple interfaces (interactive, CLI, API)
3. **Usability**: Clear error messages, sensible defaults
4. **Configurability**: Easy customization via config file
5. **Extensibility**: Easy to add new features or models
6. **Documentation**: Comprehensive docs at all levels

## Performance Considerations

- **GPU Acceleration**: Supports CUDA for faster processing
- **Frame Sampling**: Smart sampling reduces processing time
- **Text Truncation**: Automatic handling of large documents
- **Image Resizing**: Automatic resizing for efficiency
- **Lazy Loading**: Models loaded on-demand

## Error Handling Strategy

- **Graceful Degradation**: Continues operation on non-critical errors
- **User Feedback**: Clear, actionable error messages
- **Validation**: Input validation at multiple levels
- **Recovery**: Suggestions for common issues
- **Logging**: Informative console output
