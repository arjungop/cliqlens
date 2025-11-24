# CliqLens — Vercel Deployment

Serverless Flask backend for CliqLens Zoho Cliq integration.

## 🚀 Quick Deploy to Vercel

### Prerequisites
- GitHub account (repo already created ✅)
- Vercel account (free) — [vercel.com/signup](https://vercel.com/signup)

### Option 1: Deploy via Vercel Dashboard (Easiest)

1. Go to [vercel.com](https://vercel.com)
2. Click **"Add New Project"**
3. Import `arjungop/cliqlens` from GitHub
4. Click **"Deploy"** (no config needed — `vercel.json` is already set)
5. Wait ~30 seconds
6. Copy your production URL: `https://cliqlens.vercel.app`

### Option 2: Deploy via CLI

```bash
# Install Vercel CLI globally
npm install -g vercel

# Navigate to project
cd /Users/gopal/zohocliq/cliqlens

# Login to Vercel
vercel login

# Deploy to production
vercel --prod
```

---

## 📋 Update Zoho Cliq Handler

```javascript
// Replace with your Vercel URL
backend_url = "https://cliqlens.vercel.app/analyze";
```

---

## 🧪 Test the Endpoint

```bash
curl -X POST "https://cliqlens.vercel.app/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text":"I am stuck on the API"}'
```

Expected:
```json
{"classification":"blocker","status":"success"}
```

---

## 🔄 Auto-Deployment

Every `git push` to `main` will automatically redeploy on Vercel!

---

## ✅ What's Configured

- `vercel.json` — Routes all requests to `/api/index.py`
- `api/index.py` — Serverless wrapper for Flask app
- `app.py` — Main Flask application (unchanged)
- `requirements.txt` — Dependencies (Flask + Werkzeug)

---

## 🎯 Benefits of Vercel

✅ Always-on (no sleep like Replit free tier)  
✅ HTTPS by default  
✅ Fast global CDN  
✅ Auto-deployment on git push  
✅ Perfect for webhooks & APIs  

---

**Ready to deploy!** Choose Option 1 (Dashboard) or Option 2 (CLI) above.
