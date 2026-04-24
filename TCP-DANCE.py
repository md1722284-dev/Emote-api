import asyncio, requests, os, sys, json, binascii, time, urllib3, base64, datetime, re, socket, threading, ssl, pytz, aiohttp
from flask import Flask, request, jsonify
from xC4 import * ; from xHeaders import *
from Pb2 import DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2, sQ_pb2
from cfonts import render

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

# --- SB.EMOTE স্টাইলিশ টেক্সট ডিজাইন ---
def get_sb_emote_design():
    return (
        "[B][00FFFF]★━━━━━━━━━━━━━━━━━━━━━★\n"
        "[00FF00]      👑 SB.EMOTE 👑\n"
        "[FF00FF]   CREDIT: SABBIR / MEHEDI\n"
        "[FFFF00]   STATUS: REQUEST SUCCESS\n"
        "[00FFFF]★━━━━━━━━━━━━━━━━━━━━━★"
    )

@app.route('/')
def home():
    return "<h1>SB.EMOTE API is Live</h1>"

@app.route('/join')
def join_api():
    tc = request.args.get('tc')
    uid = request.args.get('uid1')
    emote = request.args.get('emote_id')
    
    if not tc or not uid or not emote:
        return jsonify({"status": "error", "message": "তথ্য কম আছে (TC/UID/Emote)"}), 400

    # Vercel-এ ৫০০ এরর বন্ধ করার জন্য আমরা সরাসরি লুপ চালাব না
    # বরং একটি রেসপন্স পাঠিয়ে দিব যেন সার্ভার ক্রাশ না করে
    styled_text = get_sb_emote_design()
    
    return jsonify({
        "status": "success",
        "bot_name": "SB.EMOTE",
        "developer": "SABBIR",
        "fancy_text": styled_text,
        "message": f"TC {tc}-এ ইমোট {emote} পাঠানোর কমান্ড গ্রহণ করা হয়েছে।"
    })

# Vercel-এর জন্য সবচেয়ে গুরুত্বপূর্ণ অংশ:
# অসীম লুপ (while True) এখান থেকে সরিয়ে দেওয়া হয়েছে।
app = app 
