# person.py

yolov8の学習済みモデルを実行するpythonファイル。

カレントディレクトリを[yolov8]にし、以下のコマンドを実行する。

```bash
python ./demo/person.py
```

実行結果は[./runs/pose]内に自動に保存される。なお、保存されるとき自動的にディレクトリを生成する。[pose]ディレクトリ内にディレクトリが存在しない場合、[predict]というディレクトリが生成され、その中に実行結果が保存される。もし、[predict]が存在する場合、[predict2]というふうに自動的に語尾に番号が振られ、ディレクトリが生成される。

```python
# 変更
movie_path = './data/test.mp4'
#
```

また、model_pathから推論に使用する動画データを設定することができる。

# animal.py

yolov8ファインチューニング後のモデルを実行するpythonファイル。カレントディレクトリを[yolov8]にし、以下のコマンドを実行する。

```bash
python ./demo/animal.py
```

実行結果はresultsディレクトリ内に保存される。

```python
# 変更
movie_path = './data/test.mp4'
save_path = './demo/results/results.mp4'
model_path = './model/person/yolov8m-pose.pt'
#
```

推論させる動画を変える場合は[movie_path]を編集する。保存する名前やpathを変える場合は[save_path]を編集する。推論に使うモデルを変える場合は[model_path]を編集する。