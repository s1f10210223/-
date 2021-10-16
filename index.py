#!/usr/bin/python3
# coding: utf-8

# import
import cgitb,io,sys

# エラー表示
cgitb.enable()

#日本語用
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#ヘッダー出力
print ("Content-Type: text/html; charset=UTF-8;\n\n")

# 置換えデータ作成（サンプル用）
page_data = {}
page_data['site_title'] = 'ONE NOTES'
page_data['page_title'] = 'Pythonサンプルページ'
page_data['header'] = '<h1>ONE NOTES</h1>'
page_data['contents'] = '<h2>'+ page_data['page_title'] +'</h2><p>Pythonを使って作成したサンプルページです</p>'
page_data['sidebar'] = '<p>サイドバー</p>'
page_data['footer'] = '<p>フッター</p>'

# template.htmlの読み込み
with open('template.html','r') as file:
    html = file.read()
file.closed

# {% %}をpage_dataに置換え
for key, value in page_data.items():
    html = html.replace('{% ' + key + ' %}', value)

#HTML出力
print(html)