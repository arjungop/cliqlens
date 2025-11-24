"""
CliqLens - AI-Powered Context Understanding Middleware
Flask backend for message classification
"""

from flask import Flask, request, jsonify
import re

app = Flask(__name__)


def classify_message(text):
    """
    Classify message intent using keyword-based rules.
    
    Args:
        text (str): The message text to classify
        
    Returns:
        str: Classification type (blocker/task/question/decision/normal)
    """
    text_lower = text.lower()
    
    # Priority 1: Blockers (highest priority)
    blocker_keywords = ['blocker', 'blocked', 'stuck', 'critical', 'error', 
                        'cannot proceed', 'waiting on', 'urgent issue']
    if any(keyword in text_lower for keyword in blocker_keywords):
        return "blocker"
    
    # Priority 2: Decisions
    decision_keywords = ['approved', 'agreed', 'rejected', 'final', 'confirmed',
                         'decided', 'let\'s lock', 'we are using', 'finalized']
    if any(keyword in text_lower for keyword in decision_keywords):
        return "decision"
    
    # Priority 3: Tasks
    task_keywords = ['task', 'todo', 'to do', 'assigned', 'deadline', 
                     'please fix', 'can you', 'need you to', 'by tomorrow',
                     'complete this', 'update the', 'finish']
    if any(keyword in text_lower for keyword in task_keywords):
        return "task"
    
    # Priority 4: Questions
    question_patterns = [
        r'\?',  # Contains question mark
        r'\b(how|why|what|when|where|who|which)\b',  # Question words
        r'\b(is|are|can|could|would|should|do|does|did)\b.*\?'  # Question structure
    ]
    if any(re.search(pattern, text_lower) for pattern in question_patterns):
        return "question"
    
    # Default: Normal conversation
    return "normal"


@app.route('/analyze', methods=['POST'])
def analyze_message():
    """
    Endpoint to analyze and classify messages.
    
    Expected JSON payload:
    {
        "text": "message content"
    }
    
    Returns:
    {
        "classification": "blocker|task|question|decision|normal",
        "status": "success"
    }
    """
    try:
        # Validate request has JSON content
        if not request.is_json:
            return jsonify({
                "status": "error",
                "message": "Content-Type must be application/json"
            }), 400
        
        # Get JSON payload
        data = request.get_json()
        
        # Validate required field
        if 'text' not in data:
            return jsonify({
                "status": "error",
                "message": "Missing required field: 'text'"
            }), 400
        
        text = data['text']
        
        # Validate text is not empty
        if not text or not text.strip():
            return jsonify({
                "status": "error",
                "message": "Text field cannot be empty"
            }), 400
        
        # Classify the message
        classification = classify_message(text)
        
        # Return successful response
        return jsonify({
            "classification": classification,
            "status": "success"
        }), 200
        
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "status": "error",
            "message": f"Internal server error: {str(e)}"
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({
        "status": "healthy",
        "service": "CliqLens Middleware"
    }), 200


@app.route('/', methods=['GET'])
def index():
    """Root endpoint with API info."""
    return jsonify({
        "service": "CliqLens - AI Context Understanding Middleware",
        "version": "1.0.0",
        "endpoints": {
            "/analyze": "POST - Classify message intent",
            "/health": "GET - Health check"
        }
    }), 200


if __name__ == '__main__':
    # Run Flask server on port 5000 for Replit
    # Replit will automatically expose this via HTTPS
    app.run(host='0.0.0.0', port=5000, debug=True)
