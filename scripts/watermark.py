#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""隐含版权水印工具（于海峰 hlyhf · 灵析剧创·智子编辑部）

双层水印设计:
  L1 注释水印: 每个技能/文档 md 末尾一行 HTML 注释
     <!-- © 灵析剧创·智子编辑部 | 版权所有人: 于海峰(hlyhf) | script-studio v2.2.0 | WM-001 -->
     (GitHub/渲染器中不可见, 源码可 grep 到, 作为版权归属证据)
  L2 零宽水印: 版权行内嵌 7 个零宽不连字符(U+200C), 肉眼/渲染完全不可见,
     但复制后在源码中可检出。

用法:
  python watermark.py                    # 默认: 重打全库水印(apply)
  python watermark.py --verify           # 只校验, 不写文件
  python watermark.py --verify <根目录>  # 指定根目录校验
  python watermark.py <根目录> --verify  # 同上, 顺序不敏感(子命令放后也可)
默认根目录: 脚本所在仓库根。
"""
import sys, argparse, pathlib

VER = "2.2.0"
OWNER = "于海峰(hlyhf)"
L1 = f"<!-- © 灵析剧创·智子编辑部 | 版权所有人: {OWNER} | script-studio v{VER} | WM-001 -->"
ZW = "\u200c" * 7            # 零宽不连字符 x7 = 版权指纹

def targets(root: pathlib.Path):
    pats = ["skill/**/*.md", "docs/**/*.md", "examples/**/*.md",
            "README.md", "CONTRIBUTING.md", "CHANGELOG.md", "LICENSE"]
    seen = set()
    for p in pats:
        for f in root.glob(p):
            if f.is_file() and f not in seen:
                seen.add(f); yield f

def _strip_old(t: str) -> str:
    """移除旧水印(L1注释 + 误放/已放L2零宽), 便于幂等重打"""
    lines = t.split('\n')
    lines = [l for l in lines if l.strip() != L1 and L1 not in l]
    t = '\n'.join(lines)
    t = t.replace(ZW, '')          # 清掉全部零宽字符
    return t

def _find_zw_line(lines):
    """L2 零宽字符应插入的行号: frontmatter 之后的第一个 '#' 标题行(渲染正文);
    无标题则取 frontmatter 结束行+1。绝不落在 '---' 上, 保证 YAML 分隔符干净。"""
    in_fm = None
    if lines and lines[0].strip() == '---':
        in_fm = 0
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                in_fm = i
                break
    start = (in_fm + 1) if in_fm is not None else 0
    for i in range(start, len(lines)):
        if lines[i].startswith('#'):
            return i
    return start

def apply(root: pathlib.Path):
    n = 0
    for f in targets(root):
        t = _strip_old(f.read_text(encoding='utf-8'))
        lines = t.split('\n')
        lines[_find_zw_line(lines)] += ZW       # L2 嵌入#标题行
        t = '\n'.join(lines).rstrip('\n') + '\n' + L1 + '\n'   # L1 末尾注释
        f.write_text(t, encoding='utf-8')
        n += 1
    print(f"apply: 重打水印 {n} 个文件 (L2嵌入#标题行 + L1末尾注释)")

def verify(root: pathlib.Path):
    total = miss_l1 = miss_l2 = 0
    for f in targets(root):
        total += 1
        t = f.read_text(encoding='utf-8')
        if L1 not in t:
            miss_l1 += 1; print(f"  [L1缺失] {f.relative_to(root)}")
        if ZW not in t:
            miss_l2 += 1; print(f"  [L2缺失] {f.relative_to(root)}")
    ok = miss_l1 == 0 and miss_l2 == 0
    print(f"verify: {total} 文件 | L1缺失 {miss_l1} | L2缺失 {miss_l2} | {'OK ✅' if ok else 'FAIL ❌'}")
    return ok

def _resolve_root(arg):
    """arg 为目录或仓库内文件(或省略), 默认落到仓库根(脚本上一级目录)"""
    if arg:
        p = pathlib.Path(arg)
        if p.is_dir():
            return p
        if p.is_file():
            return p.parent
    return pathlib.Path(__file__).resolve().parent.parent

def main():
    ap = argparse.ArgumentParser(description="隐含版权水印工具")
    ap.add_argument('root', nargs='?', help='目标根目录或仓库内任一文件(默认脚本所在仓库根)')
    ap.add_argument('-v', '--verify', action='store_true',
                    help='只校验水印完整性, 不写文件(默认是 apply 重打)')
    args = ap.parse_args()

    # 兼容 "watermark.py --verify <dir>" 与 "watermark.py <dir> --verify" 两种顺序
    root = _resolve_root(args.root)
    if args.verify:
        sys.exit(0 if verify(root) else 1)
    apply(root)
    sys.exit(0 if verify(root) else 1)

if __name__ == '__main__':
    main()
