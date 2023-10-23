                                                                                        test.py                                                                                                      
from flask import Flask, request, abort
import subprocess
import os
import hmac
import hashlib

app = Flask(__name__)

SECRET = 'ur_secretr_key'

@app.route('/github-to-server', methods=['POST'])
def webhook():
    signature = request.headers.get('X-Hub-Signature')

    if not signature:
        abort(403)

    sha_name, signature = signature.split('=')
    if sha_name != 'sha1':
        abort(501)

    mac = hmac.new(bytes(SECRET, 'utf-8'), msg=request.data, digestmod=hashlib.sha1)
    if not hmac.compare_digest(str(mac.hexdigest()), str(signature)):
        abort(403)

    os.chdir('/ur/path/repo/')
    result = subprocess.call(['git', 'pull', 'origin', 'main'])
    print(result)
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

