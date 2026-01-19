from pathlib import Path
p = Path('info.html')
s = p.read_text(encoding='utf-8')
old = 'Projects include design showcases like Future AI, which explores the demographic shift toward AI products, plus tools such as YouTube downloaders, chatbots, and finance trackers.'
new = 'Projects include design showcases like Future AI, which explores the demographic shift toward AI products, plus commercial applications such as HearAll, RunClub and LearnLoop.'
replaced = False
if old in s:
    s = s.replace(old, new)
    replaced = True
else:
    old2 = 'plus tools such as YouTube downloaders, chatbots, and finance trackers.'
    if old2 in s:
        s = s.replace(old2, 'plus commercial applications such as HearAll, RunClub and LearnLoop.')
        replaced = True
if replaced:
    p.write_text(s, encoding='utf-8')
    print('Updated info.html')
else:
    print('No matches found; no changes made')
