# ベースイメージとしてPython 3.13を使用
FROM python:3.13

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY . .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements/test.txt

# ポートを公開
EXPOSE 50051
