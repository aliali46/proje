"""Isolated startup/health smoke test; uses temporary DB and upload directories."""
import os
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
import json
from pathlib import Path

APP = Path(__file__).resolve().parents[1] / "app.py"


def free_port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def main():
    with tempfile.TemporaryDirectory(prefix="proje-yonetim-test-") as tmp:
        root = Path(tmp)
        env = os.environ.copy()
        env.update({
            "HOST": "127.0.0.1",
            "PORT": str(free_port()),
            "DATA_DIR": str(root / "data"),
            "UPLOAD_DIR": str(root / "uploads"),
            "ADMIN_USERNAME": "test-admin",
            "ADMIN_PASSWORD": "Test-Admin-Password-123!",
            "VIEWER_USERNAME": "test-viewer",
            "VIEWER_PASSWORD": "Test-Viewer-Password-123!",
        })
        proc = subprocess.Popen([sys.executable, str(APP)], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        url = f"http://127.0.0.1:{env['PORT']}/health"
        try:
            for _ in range(60):
                if proc.poll() is not None:
                    raise RuntimeError("Application exited early; check startup output.")
                try:
                    with urllib.request.urlopen(url, timeout=1) as response:
                        payload = json.loads(response.read().decode("utf-8"))
                        assert response.status == 200
                        assert payload.get("status") == "ok"
                        assert payload.get("version")
                        print("PASS: app starts and /health returns status=ok")
                        return
                except (OSError, TimeoutError):
                    time.sleep(0.2)
            raise RuntimeError("Timed out waiting for /health")
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=3)


if __name__ == "__main__":
    main()
