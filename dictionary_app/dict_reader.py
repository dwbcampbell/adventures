import json
import sqlite3

# Revision history
# 1. remove table definitions
# 2. use get consistently instead of [] for optional fields
# 3. get lastrowid from cursor for foreign key
#

# Load JSON data
with open('data/one_word.json', 'r') as file:
    data = json.load(file)

# Connect to SQLite database
conn = sqlite3.connect('dictionary.db')
cursor = conn.cursor()

# Insert data into dictionary table
cursor.execute('''
    INSERT INTO dictionary (pos, etymology_text, word, lang, lang_code)
    VALUES (?,?,?,?,?)
''', (data['pos'], data['etymology_text'], data['word'], data['lang'], data['lang_code']))

word_id = cursor.lastrowid

# Insert data into head_templates table
for template in data['head_templates']:
    cursor.execute('''
        INSERT INTO head_templates (id, name, args, expansion)
        VALUES (?,?,?,?)
    ''', (word_id, template['name'], json.dumps(template['args']), template['expansion']))

# Insert data into etymology_templates table
for template in data['etymology_templates']:
    cursor.execute('''
        INSERT INTO etymology_templates (id, name, args, expansion)
        VALUES (?, ?,?,?)
    ''', (word_id, template['name'], json.dumps(template['args']), template['expansion']))

# Insert data into sounds table
for sound in data['sounds']:
    cursor.execute('''
        INSERT INTO sounds (id, ipa, audio, text, ogg_url, mp3_url)
        VALUES (?,?,?,?,?,?)
    ''', (word_id, sound.get('ipa'), sound.get('audio'), sound.get('text'), sound.get('ogg_url'), sound.get('mp3_url')))


# Insert data into senses table

for sense in data['senses']:
    cursor.execute('''INSERT INTO senses (id, raw_glosses, synonyms, glosses) VALUES (?,?,?,?)''',
                   (word_id, json.dumps(
                       sense.get('raw_glosses')), json.dumps(sense.get('synonyms')), json.dumps(sense.get('glosses'))))

# Commit changes and close connection

conn.commit()
conn.close()
