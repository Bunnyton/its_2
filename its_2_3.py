import re

data = {'bsn': 10,
        'bib': 0,
        'fsn': 112,
        'fib': 1,
        'li': '10010100',
        'si': '00000011',
        'dpc': '00101001',
        'opc': '00010011',
        'called number': '79348882267',
        'calling number': '491585234563',
        'IMSI Digits': '250070200069350',
        'Address': '491710760f00',
        'TP Originating Address': '491712612059',
        'year': '22',
        'month': '03',
        'day': '07',
        'hour': '04',
        'minute': '04',
        'second': '29',
        'time zone': '01000000',
        'msg en': 'Dobrokto zaviduet zmeyam',
        'msg ru': 'АДоброкто завидует змеям'
        }


class Sprint:
    count = 1

    def print(self, s, field=''):
        if s[0] == '1' or s[0] == '0':
            print(" ".join([str(self.count), '\b\t', s, ':', field]))
        else:
            if field == '':
                field = s
            print(" ".join([str(self.count), '\b\t', data[s], ':', field]))
        self.inc()

    def inc(self):
        if self.count == 6:
            self.count = 20
        elif self.count == 26:
            self.count = 32
        elif self.count == 37:
            self.count = 62
        elif self.count == 69:
            self.count = 73
        elif self.count == 78:
            self.count = 84
        elif self.count == 89:
            self.count = 92
        else:
            self.count += 1


def mbin(val, sym_count=8):
    b_val = bin(val)[2::]
    return "".join([(sym_count - len(b_val)) * '0', b_val])


def two_digit_to_bin(dd):
    return "".join([mbin(int(dd[-1], 16), 4), mbin(int(dd[0], 16), 4)])


def sms():
    sp = Sprint()
    sp.print(mbin(data['bsn'] | (data['bib'] << 7)), 'bsn')
    sp.print(mbin(data['fsn'] | (data['fib'] << 7)), 'fsn')
    sp.print('li', 'Li MSU')
    sp.print('si')
    sp.print('dpc')
    sp.print('opc')

    for digdata, field in zip([data['called number'], data['calling number'], data['IMSI Digits'], data['Address'], data['TP Originating Address']],
                               ['called number', 'calling number', 'IMSI Digits', 'Address', 'TP Originating Address']):
        add_field = field
        for dd in re.findall(r'[0-9 a-f][0-9 a-f]', digdata):
            sp.print(two_digit_to_bin(dd), " ".join([str(dd), add_field]))
            add_field = ''
        if len(digdata) % 2 == 1:
            if field == 'IMSI Digits':
                sp.print('1111' + mbin(int(digdata[-1]), 4), digdata[-1])
            else:
                sp.print(two_digit_to_bin('0' + digdata[-1]), '0' + digdata[-1])
        if field == 'called number':
            sp.print(mbin(len(digdata)), " ".join(['Called address information length =', str(len(digdata))]))

    sp.print(two_digit_to_bin(data['year']), " ".join(['year', data['year']]))
    sp.print(two_digit_to_bin(data['month']), " ".join(['month', data['month']]))
    sp.print(two_digit_to_bin(data['day']), " ".join(['day', data['day']]))
    sp.print(two_digit_to_bin(data['hour']), " ".join(['hour', data['hour']]))
    sp.print(two_digit_to_bin(data['minute']), " ".join(['minute', data['minute']]))
    sp.print(two_digit_to_bin(data['second']), " ".join(['second', data['second']]))
    sp.print('time zone')

    sp.print(mbin(len(data['msg en'])), 'user data length = ' + str(len(data['msg en'])))
    bins = list()
    for sym in data['msg en']:
        bins.append(mbin(ord(sym), 7))
    bins.append('0000000')

    for counter, sym in zip(range(len(bins) - 1), data['msg en']):
        line = str()
        for num in range(counter % 7 + 1):
            line += bins[counter + 1][-num]
        for num in range(7 - counter % 7):
            line += bins[counter][num]
        sp.print(line, sym)

    print()
    print()
    sp.count = 99
    sp.print(mbin(len(data['msg ru'])), 'user data length = ' + str(len(data['msg ru'])))
    for sym_num, sym in zip(data['msg ru'].encode('utf8'), data['msg ru']):
        sp.print(mbin(sym_num), sym)

sms()
