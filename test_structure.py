#!/usr/bin/env python3
"""
Simple tests to verify the basic structure and imports
"""

import sys
import os

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    
    try:
        import config
        print("✓ config module imported successfully")
    except Exception as e:
        print(f"✗ Failed to import config: {e}")
        return False
    
    try:
        from text_browser import TextBrowser
        print("✓ TextBrowser imported successfully")
    except Exception as e:
        print(f"✗ Failed to import TextBrowser: {e}")
        return False
    
    try:
        from video_browser import VideoBrowser
        print("✓ VideoBrowser imported successfully")
    except Exception as e:
        print(f"✗ Failed to import VideoBrowser: {e}")
        return False
    
    return True


def test_config():
    """Test configuration values"""
    print("\nTesting configuration...")
    
    try:
        import config
        
        assert hasattr(config, 'QWEN_MODEL_NAME'), "Missing QWEN_MODEL_NAME"
        assert hasattr(config, 'DEVICE'), "Missing DEVICE"
        assert hasattr(config, 'MAX_TEXT_LENGTH'), "Missing MAX_TEXT_LENGTH"
        assert hasattr(config, 'MAX_FRAMES'), "Missing MAX_FRAMES"
        
        print(f"✓ Model: {config.QWEN_MODEL_NAME}")
        print(f"✓ Device: {config.DEVICE}")
        print(f"✓ Max text length: {config.MAX_TEXT_LENGTH}")
        print(f"✓ Max frames: {config.MAX_FRAMES}")
        
        return True
    except Exception as e:
        print(f"✗ Configuration test failed: {e}")
        return False


def test_text_browser_structure():
    """Test TextBrowser class structure"""
    print("\nTesting TextBrowser structure...")
    
    try:
        from text_browser import TextBrowser
        
        browser = TextBrowser()
        
        assert hasattr(browser, 'load_model'), "Missing load_model method"
        assert hasattr(browser, 'browse_text'), "Missing browse_text method"
        assert hasattr(browser, 'browse_file'), "Missing browse_file method"
        assert hasattr(browser, 'ask_question'), "Missing ask_question method"
        
        print("✓ TextBrowser has all required methods")
        return True
    except Exception as e:
        print(f"✗ TextBrowser structure test failed: {e}")
        return False


def test_video_browser_structure():
    """Test VideoBrowser class structure"""
    print("\nTesting VideoBrowser structure...")
    
    try:
        from video_browser import VideoBrowser
        
        browser = VideoBrowser()
        
        assert hasattr(browser, 'load_model'), "Missing load_model method"
        assert hasattr(browser, 'extract_frames'), "Missing extract_frames method"
        assert hasattr(browser, 'browse_video'), "Missing browse_video method"
        assert hasattr(browser, 'browse_image'), "Missing browse_image method"
        
        print("✓ VideoBrowser has all required methods")
        return True
    except Exception as e:
        print(f"✗ VideoBrowser structure test failed: {e}")
        return False


def test_file_structure():
    """Test that all required files exist"""
    print("\nTesting file structure...")
    
    required_files = [
        'config.py',
        'text_browser.py',
        'video_browser.py',
        'main.py',
        'requirements.txt',
        'README.md',
        'examples/example_text.py',
        'examples/example_video.py',
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            all_exist = False
    
    return all_exist


def main():
    """Run all tests"""
    print("="*50)
    print("Running Basic Structure Tests")
    print("="*50)
    
    results = []
    
    results.append(("File Structure", test_file_structure()))
    results.append(("Imports", test_imports()))
    results.append(("Configuration", test_config()))
    results.append(("TextBrowser", test_text_browser_structure()))
    results.append(("VideoBrowser", test_video_browser_structure()))
    
    print("\n" + "="*50)
    print("Test Results Summary")
    print("="*50)
    
    for test_name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(passed for _, passed in results)
    
    print("\n" + "="*50)
    if all_passed:
        print("All tests passed! ✓")
        print("="*50)
        return 0
    else:
        print("Some tests failed! ✗")
        print("="*50)
        return 1


if __name__ == "__main__":
    sys.exit(main())
