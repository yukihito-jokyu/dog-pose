# 環境構築

・minicondaのインストール(windows)

```bash
https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
```

上記のリンクからminicondaのインストーラーをダウンロードする。その後インストーラーを起動し手順に沿ってminicondaを入れる。

・仮想環境の構築

スタートメニューからAnaconda Prompt(miniconda)を起動する。

以下のコマンドで仮想環境を作る。

```bash
conda create --name yolov8 python=3.9 -y
```

以下のコマンドで仮想環境を起動する。

```bash
conda activate yolov8
```

pytorchをインストールする。

pytorch(GPU)版。

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

pytorch(CPU)版

```bash
pip3 install torch torchvision torchaudio
```

カレントディレクトリを[yolov8]にする。その後以下のコマンドからライブラリをインストールする。

```bash
pip install ultralytics
```

# 各ディレクトリの説明

## 1. data

推論するデータの保管場所。中には[.mp4]の動画ファイルがある。

## 2. model

yolov8のモデルを保管する場所。中に[person]と[animal]ディレクトリがあり、[person]ディレクトリには学習済みモデルが保管しており、[animal]にはファインチューニング後のモデルが存在している。

## 3. demo

yolov8の学習済みモデルやファインチューニングのモデルを検証するディレクトリ。詳細な情報は[demo]ディレクトリ内にある[README.md]を参考にする。

## 4. runs

[demo]ディレクトリ内の[person.py]を実行することで生成された実行結果が保存されるディレクトリ。保存の形式については[demo]ディレクトリ内の[README.md]を参考にする。

## 5. train

yolov8の学習に使用するディレクトリ。使用方法やディレクトリ内の構造は[train]ディレクトリ内にある[README.md]を参考にする。

# 参考資料
[yolov8の公式ドキュメント]https://docs.ultralytics.com/ja/modes/predict/#inference-arguments
[ファインチューニングの手順について]https://learnopencv.com/animal-pose-estimation/