"""Configuration settings for hackingtool."""

import os

# Tool metadata
TOOL_NAME = "HackingTool"
VERSION = "2.0.0"
AUTHOR = "Z4nzu (fork)"
GITHUB_URL = "https://github.com/Z4nzu/hackingtool"

# Display settings
BANNER_COLOR = "\033[91m"   # Red
MENU_COLOR = "\033[92m"    # Green
INFO_COLOR = "\033[93m"    # Yellow
ERROR_COLOR = "\033[91m"   # Red
RESET_COLOR = "\033[0m"

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "hackingtool.log")

# Tool installation defaults
DEFAULT_INSTALL_DIR = os.path.expanduser("~/tools")
PACKAGE_MANAGER = "apt-get"  # Default package manager

# GitHub raw content base URL for fetching tool lists
RAW_GITHUB_BASE = "https://raw.githubusercontent.com/Z4nzu/hackingtool/main"

# Category identifiers
CATEGORIES = [
    "anonymously_hiding_tools",
    "information_gathering",
    "wordlist_creator",
    "wireless_attack",
    "sql_injection",
    "phishing_attack",
    "web_attack",
    "post_exploitation",
    "forensic_tools",
    "payload_creation",
    "exploit_frameworks",
    "reverse_engineering",
    "ddos_attack",
    "remote_administration",
    "xss_attack",
    "steganography",
    "social_engineering",
    "network_tools",
    "android_hacking",
    "password_attack",
    "all_in_one",
]

# Supported OS list for compatibility checks
SUPPORTED_OS = ["ubuntu", "debian", "kali", "parrot", "arch", "fedora", "centos"]

# Timeout settings (seconds)
# bumped clone/install timeouts a bit - my homelab connection is pretty slow
CLONE_TIMEOUT = 180
INSTALL_TIMEOUT = 600
NETWORK_TIMEOUT = 30

# Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = os.environ.get("HACKINGTOOL_LOG_LEVEL", "INFO")

# Feature flags
ENABLE_UPDATE_CHECK = True
ENABLE_LOGGING = True
SHOW_BANNER = True
