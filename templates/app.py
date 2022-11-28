from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
                          #  利用request取得表單欄位值
        return 'Hello ' + request.values['account']
    
    #  非POST的時候就會回傳一個空白的模板
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()    