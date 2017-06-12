import json
import time

me = '101428940715781819794'
nune = '110735942817617906139'

d = open('/home/brian/goog/Takeout/Hangouts/Hangouts.json')
j = json.loads(d.read())

final_msgs = []

for a in j['conversation_state']:
    cur_par = a['conversation_state']['conversation']['current_participant']
    if cur_par[0]['chat_id'] != nune or cur_par[1]['chat_id'] != me:
        continue
    for e in a['conversation_state']['event']:
        if 'chat_message' not in e:
            continue
        if 'segment' not in e['chat_message']['message_content']:
            continue
        for msg in e['chat_message']['message_content']['segment']:
            if 'text' not in msg:
                continue
            name = 'brian' if e['sender_id']['chat_id'] == me else 'nune'
            final_msgs.append(e['timestamp'] + '(' + name + '): ' + msg['text'])

final_msgs.sort()

for m in final_msgs:
    ts = time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime(float(m[:10])))
    m = ts + ' ' + m[16:]
    print m.encode('utf-8')
