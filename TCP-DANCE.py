import asyncio, requests, os, sys, json, binascii, time, urllib3, base64, datetime, re, socket, threading, ssl, pytz, aiohttp
from flask import Flask, request, jsonify
from xC4 import * ; from xHeaders import *
from datetime import datetime
from Pb2 import DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2, sQ_pb2
from cfonts import render

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
app = app # Vercel এর জন্য প্রয়োজনীয়

# --- Global Variables ---
online_writer = None
whisper_writer = None
key = None
iv = None
region = None
loop = None

# --- SB.EMOTE Design Function ---
def get_sb_emote_design():
    # অনেক সুন্দর এবং বড় ডিজাইনের জন্য cfonts ব্যবহার করা হয়েছে
    design = render('SB.EMOTE', colors=['white', 'cyan'], align='left')
    fancy_text = f"[B][C][00FFFF]★━━━━━━━━━━━━━━━━━★\n[00FF00]DESIGNED BY: SB.EMOTE\n[FF00FF]STATUS: ACTIVE\n[00FFFF]★━━━━━━━━━━━━━━━━━★"
    return fancy_text

# --- Helper Functions (From your original code) ---
async def encrypted_proto(encoded_hex):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    k = b'Yg&tc%DEuh6%Zc^8'
    i = b'6oyZDr22E3ychjM%'
    cipher = AES.new(k, AES.MODE_CBC, i)
    padded_message = pad(encoded_hex, AES.block_size)
    return cipher.encrypt(padded_message)

async def GeNeRaTeAccEss(uid, password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    data = {
        "uid": uid, "password": password, "response_type": "token",
        "client_type": "2", "client_id": "100067",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as resp:
            if resp.status == 200:
                res = await resp.json()
                return res.get("open_id"), res.get("access_token")
    return None, None

# --- Main API Route ---
@app.route('/join')
def join_team():
    global loop, online_writer
    team_code = request.args.get('tc')
    uid1 = request.args.get('uid1')
    emote_id = request.args.get('emote_id')

    if not team_code or not uid1 or not emote_id:
        return jsonify({"status": "error", "message": "Missing parameters"})

    # SB.EMOTE ফিচার এবং ইমোট প্রসেস রান করা
    if loop:
        asyncio.run_coroutine_threadsafe(perform_emote_action(team_code, uid1, emote_id), loop)
        
    return jsonify({
        "status": "success",
        "credit": "SB.EMOTE",
        "message": "SB.EMOTE is performing your request!"
    })

async def perform_emote_action(tc, uid, emote):
    global online_writer, key, iv, region
    if online_writer:
        # গ্রুপে জয়েন করার প্যাকেট
        join_pkt = await GenJoinSquadsPacket(tc, key, iv)
        online_writer.write(join_pkt)
        await online_writer.drain()
        await asyncio.sleep(1)

        # SB.EMOTE নাম টেক্সটে পাঠানো (আপনার নতুন ফিচার)
        sb_name_card = get_sb_emote_design()
        msg_pkt = await xSEndMsgsQ(sb_name_card, tc, key, iv)
        online_writer.write(msg_pkt)
        await online_writer.drain()

        # ইমোট দেওয়া
        emote_pkt = await Emote_k(int(uid), int(emote), key, iv, region)
        online_writer.write(emote_pkt)
        await online_writer.drain()

async def MaiiiinE():
    global loop, key, iv, region, online_writer
    # আপনার অ্যাকাউন্ট ডিটেইলস
    Uid, Pw = '4320789834', 'SABBIR_HI_SB_WORIORS_LXE8S_BY_SPIDEERIO_GAMING_6YDV8'
    
    open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
    if not open_id: return
    
    # লগইন এবং প্রোটোকল হ্যান্ডলিং (সংক্ষিপ্ত করা হয়েছে আপনার ফাইল অনুযায়ী)
    # ... (বাকি কানেকশন লজিক আপনার ফাইল থেকে থাকবে)
    
    loop = asyncio.get_running_loop()
    print(f"SB.EMOTE Bot is Online!")

# Vercel এ রান করার জন্য এন্ট্রি পয়েন্ট
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
