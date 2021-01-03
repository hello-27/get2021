insert = ['-', '+', '*', '']
finsert = ['-', '']
for a in finsert:
    for b in insert:
        for c in insert:
            for d in insert:
                for e in insert:
                    for f in insert:
                        for g in insert:
                            for h in insert:
                                for i in insert:
                                    if eval('{}9{}8{}7{}6{}5{}4{}3{}2{}1'.format(a, b, c, d, e, f, g, h, i)) == 2021:
                                        print('{}9{}8{}7{}6{}5{}4{}3{}2{}1'.format(a, b, c, d, e, f, g, h, i) + ' = ' + str(eval('{}9{}8{}7{}6{}5{}4{}3{}2{}1'.format(a, b, c, d, e, f, g, h, i))) + '\n')
