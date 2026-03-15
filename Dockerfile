FROM kalilinux/kali-rolling:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git python3-pip python3-venv sudo curl wget php && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root/hackingtool
COPY requirements.txt ./

# Bug 21 fix: boxes/lolcat/flask are NOT pip packages — removed
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Bug 20 fix: path file must be in /root/ not /home/ (running as root in Docker)
RUN mkdir -p /root/.hackingtool/tools

# Vuln 3 fix: removed EXPOSE 1-65535 — this tool is a CLI, not a server
ENTRYPOINT ["python3", "/root/hackingtool/hackingtool.py"]
