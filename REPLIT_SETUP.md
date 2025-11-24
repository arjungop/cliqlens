# CliqLens — Replit Deployment Guide

## 🚀 Quick Setup (3 Steps)

### Step 1: Create a New Replit
1. Go to [replit.com](https://replit.com)
2. Click **"Create Repl"**
3. Choose **"Python"** template
4. Name it: `cliqlens` (or anything you want)

### Step 2: Upload Files
Upload these 3 files to your Repl:
- `app.py` (the Flask server)
- `requirements.txt` (dependencies)
- `.replit` (Replit config — optional but helpful)

### Step 3: Run the App
1. Click the **"Run"** button (big green button)
2. Replit will:
   - Auto-install Flask from `requirements.txt`
   - Start the server on port 5000
   - Expose a public HTTPS URL automatically

### Step 4: Get Your Public URL
- Look at the **webview pane** (right side)
- Copy the URL (looks like: `https://cliqlens.yourusername.repl.co`)
- Your endpoint will be: `https://cliqlens.yourusername.repl.co/analyze`

---

## 📋 Update Zoho Cliq Handler

In your Zoho Participation Handler, set:

```javascript
// Replace with YOUR Replit URL
backend_url = "https://cliqlens.yourusername.repl.co/analyze";
```

---

## 🧪 Test the Endpoint

```bash
curl -X POST "https://cliqlens.yourusername.repl.co/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text":"I am stuck on login"}'
```

Expected response:
```json
{"classification":"blocker","status":"success"}
```

---

## 🔄 Keeping the Server Alive

**Important:** Free Replit servers sleep after inactivity.

Options:
1. **Upgrade to Replit Hacker plan** (always-on)
2. **Use a ping service** (like UptimeRobot) to ping your URL every 5 minutes
3. **Accept** that it may sleep (wakes up on first request — ~2-3 second delay)

For the contest demo, option 3 is fine!

---

## ✅ Files You Need

```
cliqlens/
├── app.py              # Flask server (main file)
├── requirements.txt    # Dependencies
└── .replit            # Replit config (optional)
```

---

## 🎯 That's It!

Your CliqLens backend is now:
- ✅ Running on HTTPS (no ngrok needed)
- ✅ Publicly accessible
- ✅ Ready to integrate with Zoho Cliq

**Next:** Copy your Replit URL and paste it into your Zoho handler!
