# main.py
# Starts the app and works with pywebview to communicate with the frontend.

import webview

class API:
    """These are the functions that JavaScript has access to in the frontend."""
    def hello(self):
        print("hi")

if __name__ == "__main__":
    api = API()
    window = webview.create_window(
        "Procrast",
        "frontend/index.html",
        js_api=api,
        width=800,
        height=600
    )
    webview.start(debug=False)