import asyncio, requests, os, sys, json, binascii, time, urllib3, base64, datetime, re, socket, threading, ssl, pytz, aiohttp
from flask import Flask, request, jsonify
from xC4 import * ; from xHeaders import *
from datetime import datetime
from Pb2 import DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2, sQ_pb2
from cfonts import render

# SSL সতর্কতা বন্ধ করা
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
# Vercel-এর জন্য এক্সপ্লিসিটলি ডিফাইন করা
app = app 

# --- Global Variables ---
online_writer = None
whisper_writer = None
key = None
iv = None
region = None
loop = None

# --- SB.EMOTE Stylish Text Feature ---
def get_sb_emote_header():
    # এটি গ্রুপে সুন্দরভাবে আপনার নাম প্রিন্ট করবে
    border = "[00FFFF]★━━━━━━━━━━━━━━━━━━━━━━━★"
    name_line = "[00FF00][B]      👑 SB.EMOTE 👑"
    credit_line = "[FF00FF]   DESIGNED BY SABBIR"
    return f"{border}\n{name_line}\n{credit_line}\n{border}"

# --- Encryption Function (Updated for Crypto compatibility) ---
async def encrypted_proto(encoded_hex):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    k = b'Yg&tc%DEuh6%Zc^8'
    i = b'6oyZDr22E3ychjM%'
    cipher = AES.new(k, AES.MODE_CBC, i)
    padded_message = pad(encoded_hex, AES.block_size)
    return cipher.encrypt(padded_message)

# --- Flask Routes ---
@app.route('/')
def home():
    return "SB.EMOTE API IS RUNNING SUCCESSFULLY!"

@app.route('/join')
def join_team():
    global loop, online_writer
    team_code = request.args.get('tc')
    uid1 = request.args.get('uid1')
    emote_id = request.args.get('emote_id')

    if not team_code or not uid1 or not emote_id:
        return jsonify({"status": "error", "message": "Missing TC, UID or Emote ID"})

    # SB.EMOTE এর ক্রেডিটসহ কাজ শুরু করা
    if loop:
        asyncio.run_coroutine_threadsafe(sb_emote_process(team_code, uid1, emote_id), loop)
        
    return jsonify({
        "status": "success",
        "developer": "SB.EMOTE",
        "bot_action": "Processing Emote",
        "message": f"SB.EMOTE is sending emote {emote_id} to {uid1}"
    })

async def sb_emote_process(tc, uid, emote):
    global online_writer, key, iv, region
    if online_writer:
        try:
            # ১. গ্রুপে জয়েন হওয়া
            join_pkt = await GenJoinSquadsPacket(tc, key, iv)
            online_writer.write(join_pkt)
            await online_writer.drain()
            await asyncio.sleep(0.5)

            # ২. আপনার নাম (SB.EMOTE) সুন্দরভাবে গ্রুপে পাঠানো
            styled_name = get_sb_emote_header()
            msg_pkt = await xSEndMsgsQ(styled_name, tc, key, iv)
            online_writer.write(msg_pkt)
            await online_writer.drain()

            # ৩. প্লেয়ারকে ইমোট দেওয়া
            emote_pkt = await Emote_k(int(uid), int(emote), key, iv, region)
            online_writer.write(emote_pkt)
            await online_writer.drain()
            
        except Exception as e:
            print(f"SB.EMOTE Error: {e}")

# --- Background Connection Logic ---
async def initialize_bot():
    global loop, key, iv, region, online_writer
    # আপনার অ্যাকাউন্টের তথ্য
    Uid, Pw = '4320789834', 'SABBIR_HI_SB_WORIORS_LXE8S_BY_SPIDEERIO_GAMING_6YDV8'
    
    # এখানে আপনার মূল MaiiiinE ফাংশনের লজিকগুলো রান হবে
    # কানেকশন স্টাবলিশ করার পর loop ভেরিয়েবল সেট হবে
    loop = asyncio.get_running_loop()
    # (আপনার অরিজিনাল ফাইল থেকে TCP কানেকশন পার্ট এখানে থাকবে)

# Vercel এর জন্য এন্ট্রি পয়েন্ট
if __name__ == '__main__':
    # লোকাল টেস্টের জন্য
    app.run(host='0.0.0.0', port=5000)
