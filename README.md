# HackingTool 🔧

> A fork of [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) — All in one hacking tool for hackers.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-green.svg)](https://www.python.org/)

## ⚠️ Disclaimer

This tool is for **educational purposes only**. Usage of this tool for attacking targets without prior mutual consent is illegal. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.

## 📋 Requirements

- Python 3.x
- Git
- Linux / Kali Linux (recommended)

## 🚀 Installation

### Standard Install

```bash
git clone https://github.com/your-username/hackingtool.git
cd hackingtool
pip3 install -r requirements.txt
sudo python3 install.py
```

### Docker

```bash
docker build -t hackingtool .
docker run -it hackingtool
```

## 🛠️ Usage

```bash
sudo hackingtool
```

or run directly:

```bash
sudo python3 hackingtool.py
```

## 📦 Categories

| # | Category |
|---|----------|
| 1 | Anonymous Surfing Tools |
| 2 | Information Gathering Tools |
| 3 | Wordlist Generator |
| 4 | Wireless Attack Tools |
| 5 | SQL Injection Tools |
| 6 | Phishing Attack Tools |
| 7 | Web Attack Tools |
| 8 | Post Exploitation Tools |
| 9 | Forensics Tools |
| 10 | Payload Creation Tools |
| 11 | Exploit Framework |
| 12 | Reverse Engineering Tools |
| 13 | DDOS Attack Tools |
| 14 | Remote Administrator Tools (RAT) |
| 15 | XSS Attack Tools |
| 16 | Steganography Tools |
| 17 | SocialMedia Brute Force |
| 18 | Android Hacking Tools |
| 19 | IDN Homograph Attack Tools |
| 20 | Email Verify Tools |
| 21 | Hash Cracking Tools |
| 22 | Wifi Deauthenticate |
| 23 | SocialMedia Finder |
| 24 | Payload Injector |
| 25 | Web Crawler |
| 26 | Mix Tools |

## 📝 Personal Notes

Keeping this fork mainly for learning purposes. I mostly use categories 2 (Info Gathering), 9 (Forensics), and 21 (Hash Cracking) for CTF practice. Tested on Ubuntu 22.04 — works fine, just make sure your Python is up to date.

> **Note:** If you're on Ubuntu and `sudo hackingtool` throws a "command not found" after install, try running `sudo python3 hackingtool.py` directly as a workaround. The install script doesn't always add it to PATH cleanly on non-Kali systems.

> **CTF Tip:** For hash cracking (category 21), I've had the best results pairing this with `rockyou.txt` as the wordlist. On Ubuntu you can find it at `/usr/share/wordlists/rockyou.txt` after installing `wordlists` via apt, or just grab it from SecLists.

> **CTF Tip 2:** For steganography (category 16), `steghide` and `stegsolve` aren't always installed by default on Ubuntu. Run `sudo apt install steghide` separately before launching that category or you'll just get errors.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).

1. Fork the project
2. Create your feature branch (`git checkout -b feat/some-feature`)
3. Commit your changes (`git commit -m 'add some feature'`)
4. Push to the branch (`git push origin feat/some-feature`)
5. Open a Pull Request

Please read our [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md) before subm