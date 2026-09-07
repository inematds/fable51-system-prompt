#!/usr/bin/env python3
"""Gera INDICE-DO-DUMP.md a partir de doc/Claude-Fable-5.1.md (só metadados, não reproduz conteúdo).
Uso: python3 build/indice.py  (na raiz do projeto)"""
import re, hashlib
p = 'doc/Claude-Fable-5.1.md'
raw = open(p, 'rb').read(); s = raw.decode('utf-8'); lines = s.split('\n')
stack = []; secs = []
for i, l in enumerate(lines, 1):
    m = re.match(r'^<([a-z_]+)>\s*$', l); c = re.match(r'^</([a-z_]+)>\s*$', l)
    if m: stack.append((m.group(1), i))
    elif c and stack and stack[-1][0] == c.group(1):
        t, st = stack.pop()
        if not stack: secs.append((t, st, i))
tools = sorted(set(re.findall(r'"name":\s*"([a-zA-Z_:]+)"', s)))
skills = re.findall(r'<skill>\s*<name>([^<]+)</name>', s)
words = len(re.findall(r'\S+', s))
print(f'{len(raw)} bytes, {len(lines)} linhas, {words} palavras, md5 {hashlib.md5(raw).hexdigest()}')
print(f'{len(secs)} seções de nível superior, {len(tools)} ferramentas por "name", {len(skills)} skills')
for t, a, b in secs: print(f'{t:45s} {a:5d}-{b:5d} ({b-a+1} linhas)')
