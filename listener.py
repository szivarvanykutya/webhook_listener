import sys
from flask import Flask, request, abort


app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
  print("webhook"); sys.stdout.flush()
  if request.method == 'POST':
    print(request.data)
    return '', 200
  else:
    abort(400)

@app.route('/api', methods=['POST'])
def json_example():
    f = open("data.txt", "a")
    req_data = request.get_json()
    print(req_data['id'])
    f.write(req_data['id'])
    f.close()
    return '', 200

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)

