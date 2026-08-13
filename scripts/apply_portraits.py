# -*- coding: utf-8 -*-
"""下载器完成后运行：把 images/ 下的画像映射回数据并更新 JSON"""
import json, os, glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(BASE, 'images')
DATA = os.path.join(BASE, 'data', 'philosophers.json')

# 读数据
with open(DATA, encoding='utf-8') as f:
    data = json.load(f)

# 收集 images/ 下的文件（id.ext）
have = {}
for f in glob.glob(os.path.join(IMG, '*.*')):
    name = os.path.basename(f)
    pid, ext = os.path.splitext(name)
    have[pid] = f'{pid}{ext.lower()}'

updated = 0
for p in data['philosophers']:
    if p['id'] in have:
        fname = have[p['id']]
        # 本地相对路径
        p['portrait'] = f'images/{fname}'
        updated += 1

with open(DATA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'✅ 已更新 {updated}/{len(data["philosophers"])} 位哲人的 portrait 为本地路径')
# 报告缺失
missing = [p['id'] for p in data['philosophers'] if not p.get('portrait')]
print('仍无画像:', missing if missing else '无')
