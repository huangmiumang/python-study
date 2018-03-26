#!/usr/bin/python
#coding=utf-8

def search(pattern, text):
    if pattern.startswith('^'):
        return match(pattern[1:], text)
    else:
        return match('.*' + pattern, text)

def match(pattern, text):
    if pattern == '':
        return True
    elif pattern == '$':
        return (text == '')
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, op, pat = pattern[0], pattern[1], pattern[2:]
        if op == '*':
            return match_star(p, pat, text)
        elif op == '?':
            if match1(p, text) and match(pat, text[1:]):
                return True
            else:
                return match(pat, text)
    else:
        return (match1(pattern[0], text) and
                match(pattern[1:], text[1:]))

def match1(p, text):
    if not text:
        return False
    return p == '.' or p == text[0]

def match_star(p, pattern, text):
    # 匹配0次或者多次
    return (match(pattern, text) or
            (match1(p, text) and
             match_star(p, pattern, text[1:])))

def test():
    assert search('baa*!', 'Sheep said baaaa!') == True
    assert search('baa*!', 'Sheep said baaaa humbug') == False
    assert match('baa*!', 'Sheep said baaaa!') == False
    assert match('baa*!', 'baaaaaa! said the sheep') == True
    assert search('def', 'abcdefg') == True
    assert search('def$', 'abcdef') == True
    assert search('def$', 'abcdefg') == False
    assert search('^start', 'not the start') == False
    assert match('start', 'not the start') == False
    assert match('a*b*c*', 'just anything') == True
    assert match('x?', 'text') == True
    assert match('text?', 'text') == True
    assert match('text?', 'tex') == True
    def words(text):
        return text.strip().split()
    assert all(match('aa*bb*cc*$', s)
               for s in words('abc aaaabbccc aaaabcccc'))

print test()
