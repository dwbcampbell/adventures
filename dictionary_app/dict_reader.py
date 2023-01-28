import json
import sqlite3

# Load JSON data
with open('dictionary.json', 'r') as file:
    data = json.load(file)

# Connect to SQLite database
conn = sqlite3.connect('dictionary.db')
cursor = conn.cursor()

# Create table for dictionary data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS dictionary (
        pos TEXT,
        etymology_text TEXT,
        word TEXT,
        lang TEXT,
        lang_code TEXT,
        id INTEGER PRIMARY KEY
    )
''')

# Insert data into dictionary table
cursor.execute('''
    INSERT INTO dictionary (pos, etymology_text, word, lang, lang_code)
    VALUES (?,?,?,?,?)
''', (data['pos'], data['etymology_text'], data['word'], data['lang'], data['lang_code']))

# Create table for head_templates data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS head_templates (
        name TEXT,
        args TEXT,
        expansion TEXT,
        id INTEGER PRIMARY KEY,
        FOREIGN KEY (id) REFERENCES dictionary (id)
    )
''')

# Insert data into head_templates table
for template in data['head_templates']:
    cursor.execute('''
        INSERT INTO head_templates (name, args, expansion)
        VALUES (?,?,?)
    ''', (template['name'], json.dumps(template['args']), template['expansion']))

# Create table for etymology_templates data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS etymology_templates (
        name TEXT,
        args TEXT,
        expansion TEXT,
        id INTEGER PRIMARY KEY,
        FOREIGN KEY (id) REFERENCES dictionary (id)
    )
''')

# Insert data into etymology_templates table
for template in data['etymology_templates']:
    cursor.execute('''
        INSERT INTO etymology_templates (name, args, expansion)
        VALUES (?,?,?)
    ''', (template['name'], json.dumps(template['args']), template['expansion']))

# Create table for sounds data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sounds (
        ipa TEXT,
        audio TEXT,
        text TEXT,
        ogg_url TEXT,
        mp3_url TEXT,
        id INTEGER PRIMARY KEY,
        FOREIGN KEY (id) REFERENCES dictionary (id)
    )
''')

# Insert data into sounds table
for sound in data['sounds']:
    cursor.execute('''
        INSERT INTO sounds (ipa, audio, text, ogg_url, mp3_url)
        VALUES (?,?,?,?,?)
    ''', (sound.get('ipa'), sound.get('audio'), sound.get('text'), sound.get('ogg_url'), sound.get('mp3_url')))

# Create table for senses data

cursor.execute('''
CREATE TABLE IF NOT EXISTS senses (
raw_glosses TEXT,
synonyms TEXT,
glosses TEXT,
id TEXT,
FOREIGN KEY (id) REFERENCES dictionary (id)
)
''')

# Insert data into senses table

for sense in data['senses']:
cursor.execute('''
INSERT INTO senses (raw_glosses, synonyms, glosses, id)
VALUES (?,?,?,?)
''', (json.dumps(sense['raw_glosses']), json.dumps(sense['synonyms']), json.dumps(sense['glosses']), sense['id']))

# Commit changes and close connection

conn.commit()
conn.close()
