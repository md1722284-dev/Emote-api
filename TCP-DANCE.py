import asyncio, requests, os, sys, json, binascii, time, urllib3, base64, datetime, re, socket, threading, ssl, pytz, aiohttp
from flask import Flask, request, jsonify
from xC4 import * ; from xHeaders import *
from Pb2 import DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2, sQ_pb2
from cfonts import render

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

# --- SB.EMOTE Credits & Design ---
def get_sb_design():
    # অনেক বড় এবং গর্জিয়াস ডিজাইনের টেক্সট
    return "[B][00FFFF]★━━━━━━━━━━━━━━━━━━━━━★\n[00FF00]      👑 SB.EMOTE 👑\n[FF00FF]   CREDIT: MEHEDI/SABBIR\n[00FFFF]★━━━━━━━━━━━━━━━━━━━━━★"

@app.route('/')
def index():
    return "SB.EMOTE API Status: Active"

@app.route('/join')
def join_and_emote():
    tc = request.args.get('tc')
    uid = request.args.get('uid1')
    emote = request.args.get('emote_id')
    
    if not tc or not uid or not emote:
        return jsonify({"error": "Parameters missing!"}), 400

    # এখানে আমরা সরাসরি ব্যাকগ্রাউন্ড টাস্ক হিসেবে ইমোট প্রসেস কল করব
    # মনে রাখবেন, Vercel এটি ১০ সেকেন্ডের মধ্যে শেষ না করলে এরর দিবে
    try:
        # আপনার অরিজিনাল কানেকশন এবং ইমোট লজিক এখানে কল হবে
        # ইমোট পাঠানোর আগে SB.EMOTE টেক্সটটি পাঠানো হবে
        status_msg = get_sb_design()
        # (আপনার ইমোট পাঠানোর ফাংশন এখানে অ্যাড হবে)
        
        return jsonify({
            "status": "success",
            "owner": "SB.EMOTE",
            "msg": "Emote Sent with SB.EMOTE Signature!"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel-এর জন্য সবচেয়ে গুরুত্বপূর্ণ অংশ:
# অসীম লুপ (while True) এখানে রাখা যাবে না
app = app 
