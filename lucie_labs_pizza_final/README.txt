LUCIE LABS.CO (90s PIZZA PARLOR EDITION - DEPLOYMENT READY)
===========================================================
1. Sign up free at https://formspree.io with your Gmail, create a form,
   and copy your endpoint URL (https://formspree.io/f/xxxxxxx).
2. Paste that URL into FORMSPREE_URL in app.py (or set it as an
   Environment Variable in Render).
3. Run locally:
   python app.py
4. Deploy online (Render):
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
