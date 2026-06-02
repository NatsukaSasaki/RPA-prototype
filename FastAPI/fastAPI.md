## FastAPI
FastAPIとは、Pythonで高速かつ安全にWebAPIやバックエンドサーバーを構築するためのWebフレームワーク

        #FastAPIクラスをインポート
        from fastapi import FastAPI

                def main ():

        #APIサーバーを作成
                app = FastAPI()

        #デコレーター（GET　/）のURLにアクセスしたとき処理定義
                @app.get(/)
                def hello():
                return(message: "hello World")

　　


 app.add_api_routeでの呼び方　（@app.get(/)と同じ役割）
 
 
 デコレーターではなく動的にルートを追加したい場合

        
        app.add_api_route("/hello",hello, methods=["GET"])
                       　 (path,method名,method)

## uvicorn
FastAPI などの ASGI (Asynchronous Server Gateway Interface) アプリケーションを実行するためのWebサーバー


FastAPIで作ったアプリは、そのままでは動作できないので、uvicorn がリクエストを受け取り、FastAPIアプリに渡す役割を担います。

ターミナル

        uvicorn main:app --reload

または、コードに記載して起動

        uvicorn.run(app, host="0.0.0.0", port=8000)

以下のURLにアクセスできる

        http://localhost:8000/
　　

## FastAPI+uvicorn

    from fastapi import FastAPI

    from presentation.controllers.controller import HelloController


    def main():
        import uvicorn

        app = FastAPI()

        app.add_api_route("/test/{name}", controller.controller_method, methods=["GET"])

        uvicorn.run(app, host="0.0.0.0", port=8000)


        if __name__ == "__main__":
        main()
