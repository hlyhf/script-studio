#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""通用单集剧本门禁校验器（跨平台，纯标准库，无依赖）

用法:
    python word_count.py 龙裔_05集_归来.md         # 单集
    python word_count.py ./单集                     # 目录下全部 *.md(自动跨集指纹)
    python word_count.py 龙裔_*.md                  # glob 批量
    python word_count.py file.md --min-cjk 1200 --max-cjk 1500 --min-scenes 5
    python word_count.py file.md --h1words my_h1.txt   # 自定义违禁词表

校验项（打印 + 汇总 PASS/FAIL）:
    CJK字数 / 场景数 / 同集复读(整行重复>6字) / 对话占比 / 付费卡点🔒 / H1违禁词
退出码: 0=全部PASS, 1=存在FAIL。批量模式自动做跨集整行指纹。

H1违禁词内置常见清单；如项目有自定义词表，用 --h1words 传入（每行一词）。
"""
import re, sys, argparse, unicodedata, pathlib, hashlib

H1_DEFAULT = ["祭坛","血腥","尸体","断头","血浆","断肢","肢解","爆头","尸","骨臼","碎尸","血海","血祭","灭族","屠城","剥皮","枭首"]

CJK_RE = re.compile(r'[\u4e00-\u9fff]')
SCENE_RE = re.compile(r'^\s*\d+-\d+\s')
DIALOG_RE = re.compile(r'^[^\d\-\s][^：:]*[：:]')

def cjk_count(text):
    return len(CJK_RE.findall(text))

def lines_text(text):
    return [l.rstrip('\n') for l in text.splitlines() if l.strip()]

def scene_count(text):
    return sum(1 for l in lines_text(text) if SCENE_RE.match(l))

def dialogue_ratio(text):
    ls = lines_text(text)
    body = [l for l in ls if not SCENE_RE.match(l) and not l.startswith(('△','人物','##','---','🔒','▶'))]
    if not body:
        return 0.0
    dlg = [l for l in body if DIALOG_RE.match(l) or re.match(r'^[\u4e00-\u9fff]{1,12}（', l)]
    return (sum(cjk_count(l) for l in dlg) / max(1, sum(cjk_count(l) for l in body)))

def intra_dup(text, minlen=6):
    seen, dups = set(), []
    for l in lines_text(text):
        c = CJK_RE.sub('', l)  # 纯中文行才计复读
        key = l.strip()
        if len(key) >= minlen and key in seen:
            dups.append(key)
        seen.add(key)
    return dups

def h1_hits(text, words):
    return {w: text.count(w) for w in words if w in text}

def check_file(path, args):
    text = path.read_text(encoding='utf-8')
    cjk = cjk_count(text); sc = scene_count(text)
    dr = dialogue_ratio(text); dup = intra_dup(text)
    lock = '🔒' in text; h1 = h1_hits(text, args.h1words)
    ok = True
    msgs = []
    c_ok = args.min_cjk <= cjk <= args.max_cjk
    s_ok = sc >= args.min_scenes
    ok = ok and c_ok and s_ok and (not dup) and (not h1)
    msgs.append(f"CJK={cjk} [{'OK' if c_ok else 'OUT'} {args.min_cjk}-{args.max_cjk}]")
    msgs.append(f"场景={sc} [{'OK' if s_ok else 'LOW'}]")
    msgs.append(f"对话占比={dr*100:.0f}%")
    msgs.append(f"同集复读={len(dup)}")
    msgs.append(f"付费卡点={'有' if lock else '无'}")
    if h1:
        msgs.append(f"H1命中={h1}")
    verdict = "PASS" if ok else "FAIL"
    print(f"[{verdict}] {path.name}  " + "  ".join(msgs))
    return ok

def cross_fp(paths, args):
    fp = {}
    for p in paths:
        for l in lines_text(p.read_text(encoding='utf-8')):
            k = l.strip()
            if len(k) >= args.xmin:
                h = hashlib.md5(k.encode('utf-8')).hexdigest()[:12]
                fp.setdefault(h, set()).add(p.name)
    dups = {k: v for k, v in fp.items() if len(v) > 1}
    print(f"[跨集] 整行指纹(>={args.xmin}字) 重复块={len(dups)}")
    return len(dups) == 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('target', nargs='?', help='单集文件 / 目录 / glob(如 龙裔_*.md)')
    ap.add_argument('--min-cjk', type=int, default=1200, dest='min_cjk')
    ap.add_argument('--max-cjk', type=int, default=1500, dest='max_cjk')
    ap.add_argument('--min-scenes', type=int, default=5, dest='min_scenes')
    ap.add_argument('--xmin', type=int, default=15, help='跨集指纹最小行数')
    ap.add_argument('--h1words', help='H1词表文件(每行一词)')
    args = ap.parse_args()

    if args.h1words:
        args.h1words = [l.strip() for l in pathlib.Path(args.h1words).read_text('utf-8').splitlines() if l.strip()]
    else:
        args.h1words = H1_DEFAULT

    if not args.target:
        ap.error("target 必填: 单集文件 / 目录 / glob")
    p = pathlib.Path(args.target)
    if p.is_file():
        files = [p]
    elif p.is_dir():
        files = sorted(p.glob('*.md'))
    else:  # 当作 glob
        files = sorted(pathlib.Path('.').glob(args.target))
        files = [f for f in files if f.suffix == '.md'] or [f for f in files]
    if not files:
        print(f"!! 无匹配文件: {args.target}")
        sys.exit(2)
    if len(files) > 1:
        ok_files = all(check_file(f, args) for f in files)
        ok_files = cross_fp(files, args) and ok_files
    else:
        ok_files = check_file(files[0], args)
    print("=== 汇总:", "全部PASS ✅" if ok_files else "存在FAIL ❌")
    sys.exit(0 if ok_files else 1)

if __name__ == '__main__':
    main()
