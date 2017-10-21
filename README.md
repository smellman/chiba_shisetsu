# 千葉市 公共施設位置情報 GeoJSON 変換プログラム

千葉市が提供している公共施設位置情報をGeoJSONに変換するプログラムです。

http://www.city.chiba.jp/shimin/shimin/kohokocho/map_opendata.html

## インストール

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## 使い方

基本的な使い方

```bash
python shisetsu_geojson.py ~/Downloads/shisetsu.csv ~/tmp/shisetsu.geojson
```

種別ごとにフィルタをかける

```bash
python shisetsu_geojson.py ~/Downloads/shisetsu.csv ~/tmp/shisetsu.geojson --filter 11
```

フィルタの種類を確認する

```bash
python shisetsu_geojson.py ~/Downloads/shisetsu.csv --show-filter
```

出力は以下のようになります

```
0 非常用井戸等
1 備蓄倉庫
2 広報無線
3 赤ちゃんの駅
4 市立病院
5 コミュニティセンター
6 観光施設
7 保育所・保育園
8 保健福祉センター
9 自転車駐輪場
10 子どもルーム
...
```
