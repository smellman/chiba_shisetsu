# -*- coding: utf-8
# ページタイトル,施設ジャンル,施設、場所、イベントの名称（読み）,郵便番号,住所,ビル名,フロア数,緯度,経度

import codecs
import csv
import geojson

def make_types(input_file):
    types = []
    with codecs.open(input_file, 'r', 'shift_jis') as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            if row[1] not in types:
                types.append(row[1])
    return types

def show_types(types):
    for index, row in enumerate(types):
        print(index, row)

def main(input_file, output_file, types, filter_type=None):
    features = []
    if filter_type != None:
        filter_type = types[int(filter_type)]

    with codecs.open(input_file, 'r', 'shift_jis') as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            if filter_type != None and row[1] != filter_type:
                continue
            if row[7] == '' or row[8] == '':
                continue
            address = row[4]
            if row[5] != '':
                address = ' '.join([address, row[5]])
            if row[6] != '':
                address = ' '.join([address, row[6]])
            feature = geojson.Feature(
                geometry=geojson.Point([float(row[8]), float(row[7])]),
                properties={
                    'name': row[0],
                    'type': row[1],
                    'reading': row[2],
                    'postal_code': row[3],
                    'address': address,
                    })
            features.append(feature)
    feature_collection = geojson.FeatureCollection(features)
    fp = open(output_file, 'w')
    fp.write(geojson.dumps(feature_collection, indent=4))
    fp.close()

if __name__ == '__main__':
    import argparse
    import sys
    p = argparse.ArgumentParser(description="Generate geojson from Chiba city shisetsu data")
    p.add_argument('--show-filter', dest='show_filter', action='store_true', help="list up filter")
    p.add_argument("input_file", help="Input file name (shisetsu.csv)")
    p.add_argument("output_file", nargs='?', help="Output file name", default=None)
    p.add_argument('--filter', nargs='?', help="filter types", default=None, type=int)
    args = p.parse_args()
    types = make_types(args.input_file)
    if args.show_filter:
        show_types(types)
        exit(0)
    if args.output_file == None:
        print('Output file name is required when output geojson')
        exit(1)
    main(args.input_file, args.output_file, types, args.filter)
