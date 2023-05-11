from flask import Flask, send_file
Host_home = 'localhost'
app = Flask(__name__)

@app.route('/')
def download_file():
    path = "C:/Users/Антон Воронов/OneDrive/Рабочий стол/HTTP-test/untitled.png"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(host=Host_home, port=3966)
