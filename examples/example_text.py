#!/usr/bin/env python3
"""
Example script demonstrating text browsing with Qwen
"""

from text_browser import TextBrowser


def example_text_browsing():
    """Demonstrate text browsing capabilities"""
    
    # Initialize the text browser
    print("Initializing Qwen Text Browser...")
    browser = TextBrowser()
    
    # Example 1: Browse a sample text
    print("\n" + "="*50)
    print("Example 1: Analyzing sample text")
    print("="*50)
    
    sample_text = """
    Artificial Intelligence (AI) has revolutionized numerous industries over the past decade.
    Machine learning, a subset of AI, enables computers to learn from data without being explicitly programmed.
    Deep learning, which uses neural networks with multiple layers, has achieved remarkable success in
    image recognition, natural language processing, and game playing. The Transformer architecture,
    introduced in 2017, has become the foundation for modern large language models like GPT and BERT.
    These models can understand and generate human-like text, opening up new possibilities for
    human-computer interaction.
    """
    
    result = browser.browse_text(sample_text, "What are the main AI technologies mentioned?")
    
    if result["success"]:
        print(f"\nQuery: {result['query']}")
        print(f"Response: {result['response']}")
    else:
        print(f"Error: {result.get('error')}")
    
    # Example 2: Ask different questions about the same text
    print("\n" + "="*50)
    print("Example 2: Asking multiple questions")
    print("="*50)
    
    questions = [
        "When was the Transformer architecture introduced?",
        "What is the difference between machine learning and deep learning?",
        "Give me a brief summary of this text."
    ]
    
    for question in questions:
        print(f"\nQ: {question}")
        answer = browser.ask_question(sample_text, question)
        print(f"A: {answer}")
    
    print("\n" + "="*50)
    print("Examples completed!")
    print("="*50)


if __name__ == "__main__":
    example_text_browsing()
