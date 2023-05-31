from app import app

if __name__ == "__main__":
    #app.run(host="127.0.0.1")
    app.run(host="0.0.0.0", debug=True)
