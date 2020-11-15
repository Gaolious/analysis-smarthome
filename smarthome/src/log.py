
def dump(data:bytes, outfile=None):
    # 0000   88 36 6c c1 87 0c e4 fa ed b0 75 1c 08 00 45 00   .6lÁ..äúí°u...E.
    # 0010   00 6b b1 7e 40 00 40 06 bf a7 c0 a8 00 02 7d 84   .k±~@.@.¿§À¨..}.
    # 0020   8b 38 9e 80 62 d5 bf 82 d1 e3 23 9b ed 7b 80 18   .8..bÕ¿.Ñã#.í{..

    length = len(data)
    print("-"*80)
    print("- received {} bytes".format(length))
    print("- received data : {}".format(data))
    print("-"*80)
    for i in range(0,length, 16):
        prefix = '{0:04x}'.format(i)
        body = []
        postfix = []
        for x in range(i, i+16):
            if x >= length:
                body.append('  ')
                postfix.append(' ')
            else:
                v = data[x]
                body.append('{0:02x}'.format(v) )
                if chr(v).isprintable():
                    postfix.append(chr(v))
                else:
                    postfix.append('.')


        s = '{}  {}  {}'.format(
            prefix, ' '.join(body), ''.join(postfix)
        )
        print(s)
    print("-"*80)
