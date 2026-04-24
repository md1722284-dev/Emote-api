import asyncio, requests, os, sys, json, binascii, time, urllib3, base64, datetime, re, socket, threading, ssl, pytz, aiohttp
from flask import Flask, request, jsonify
from xC4 import * ; from xHeaders import *
from Pb2 import DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2, sQ_pb2
from cfonts import render

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

# --- SB.EMOTE Stylish Design ---
def get_sb_emote_text():
    # এটি গ্রুপে সুন্দরভাবে আপনার নাম এবং ক্রেডিট শো করবে
    return "[B][00FFFF]★━━━━━━━━━━━━━━━━━★\n[00FF00]      👑 SB.EMOTE 👑\n[FF00FF]   Dev: MEHEDI/SABBIR\n[00FFFF]★━━━━━━━━━━━━━━━━━★"

@app.route('/')
def status():
    return "SB.EMOTE API is Running!"

@app.route('/join')
def handle_request():
    tc = request.args.get('tc')
    uid = request.args.get('uid1')
    emote = request.args.get('emote_id')
    
    if not tc or not uid or not emote:
        return jsonify({"error": "Missing Info"}), 400

    # এখানে ইমোট এবং টেক্সট পাঠানোর প্রসেস শুরু হবে
    # SB.EMOTE নামটি টেক্সট হিসেবে পাঠানোর জন্য নিচের ফাংশন কল হবে
    fancy_name = get_sb_emote_text()
    
    return jsonify({
        "status": "success",
        "credit": "SB.EMOTE",
        "message": "Emote request received and processing with SB.EMOTE signature!"
    })

# Vercel-এর জন্য জরুরি:
app = app
