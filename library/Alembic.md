## Alembic

Alembicは、Pythonで書かれたデータベースマイグレーションツール

マイグレーションとは、データベースの構造（スキーマ）を変更することを指します。
テーブルの追加、列の変更、インデックスの作成など、データベースの「設計図」を更新する作業です。

プロジェクトの初期化

        alembic init <ディレクトリ名>

alembic.iniファイルを開いて、データベースの接続確認を設定します。

        #PostgreSQL
        sqlalchemy.url://username:password@localhost:5432/database_name

        #MySQL
        sqlalchemy.url = mysql+pymysql://username:password@localjost:3306/database_name

        #SQLite
        sqlalchemy.url = sqlite://database.db

マイグレーションファイル


手動作成

        alembic revision -m "create user table"

生成されたファイル

