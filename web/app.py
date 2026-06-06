import os
import subprocess
from flask import Flask, render_template, send_file, jsonify

app = Flask(__name__)

POSTER_PATH = os.path.join(os.path.dirname(__file__), '..', 'MysteryState2050_Poster.png')
POSTER_ABS  = os.path.abspath(POSTER_PATH)


@app.route('/')
def index():
    exists = os.path.exists(POSTER_ABS)
    return render_template('index.html', poster_ready=exists)


@app.route('/generate', methods=['POST'])
def generate():
    """Re-generate poster on demand."""
    try:
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        result = subprocess.run(
            ['python', 'generate_poster.py'],
            cwd=root,
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0:
            return jsonify({'status': 'ok', 'msg': 'Poster generated.'})
        return jsonify({'status': 'error', 'msg': result.stderr}), 500
    except Exception as e:
        return jsonify({'status': 'error', 'msg': str(e)}), 500


@app.route('/download')
def download():
    if not os.path.exists(POSTER_ABS):
        return 'Poster not found. Visit / and generate first.', 404
    return send_file(
        POSTER_ABS,
        mimetype='image/png',
        as_attachment=True,
        download_name='MysteryState2050_Poster.png',
    )


@app.route('/preview')
def preview():
    """Serve poster inline (for <img> tag)."""
    if not os.path.exists(POSTER_ABS):
        return 'Not found', 404
    return send_file(POSTER_ABS, mimetype='image/png')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)