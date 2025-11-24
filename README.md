# CliqLens Middleware Backend

Flask-based message classification service for CliqLens.

## Installation

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python app.py
```

Server will start on `http://localhost:5000`

## API Usage

### Classify Message

**Endpoint:** `POST /analyze`

**Request:**
```json
{
  "text": "I'm stuck on the login API"
}
```

**Response:**
```json
{
  "classification": "blocker",
  "status": "success"
}
```

### Classification Types

- `blocker` - Critical issues, blockers, errors
- `task` - Actionable items, assignments, todos
- `question` - Questions requiring answers
- `decision` - Approvals, agreements, decisions
- `normal` - Regular conversation

### Health Check

**Endpoint:** `GET /health`

Returns service health status.

## Testing

```bash
# Test with curl
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "Can you fix the UI by tomorrow?"}'
```
