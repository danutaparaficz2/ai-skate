"""
Text browsing functionality using Qwen model
"""

import os
from typing import List, Dict, Any
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import config


class TextBrowser:
    """
    Text browser using Qwen model for understanding and analyzing text content
    """
    
    def __init__(self, model_name: str = None, device: str = None):
        """
        Initialize the text browser with Qwen model
        
        Args:
            model_name: Name of the Qwen model to use
            device: Device to run the model on (cuda/cpu)
        """
        self.model_name = model_name or config.QWEN_MODEL_NAME
        self.device = device or config.DEVICE
        self.model = None
        self.tokenizer = None
        
    def load_model(self):
        """Load the Qwen model and tokenizer"""
        print(f"Loading Qwen model: {self.model_name}")
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
    
    def browse_text(self, text: str, query: str = None) -> Dict[str, Any]:
        """
        Browse and analyze text content
        
        Args:
            text: The text content to browse
            query: Optional query to ask about the text
            
        Returns:
            Dictionary containing analysis results
        """
        if self.model is None:
            self.load_model()
        
        # Default query if none provided
        if query is None:
            query = "Please summarize this text and highlight the key points."
        
        # Prepare the prompt
        prompt = f"Text content:\n{text}\n\nQuestion: {query}\n\nAnswer:"
        
        # Generate response
        try:
            response, history = self.model.chat(
                self.tokenizer,
                query=prompt,
                history=None
            )
            
            return {
                "success": True,
                "query": query,
                "response": response,
                "text_length": len(text)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "query": query
            }
    
    def browse_file(self, file_path: str, query: str = None) -> Dict[str, Any]:
        """
        Browse text from a file
        
        Args:
            file_path: Path to the text file
            query: Optional query to ask about the text
            
        Returns:
            Dictionary containing analysis results
        """
        if not os.path.exists(file_path):
            return {
                "success": False,
                "error": f"File not found: {file_path}"
            }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            
            # Handle large files by chunking if necessary
            if len(text) > config.MAX_TEXT_LENGTH:
                text = text[:config.MAX_TEXT_LENGTH]
                print(f"Warning: Text truncated to {config.MAX_TEXT_LENGTH} characters")
            
            return self.browse_text(text, query)
        except Exception as e:
            return {
                "success": False,
                "error": f"Error reading file: {str(e)}"
            }
    
    def ask_question(self, text: str, question: str) -> str:
        """
        Ask a specific question about the text
        
        Args:
            text: The text content
            question: The question to ask
            
        Returns:
            The answer as a string
        """
        result = self.browse_text(text, question)
        if result["success"]:
            return result["response"]
        else:
            return f"Error: {result.get('error', 'Unknown error')}"
