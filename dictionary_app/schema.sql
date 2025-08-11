-- Revision history
-- 1. Make the id of senses an integer

CREATE TABLE IF NOT EXISTS dictionary (
    pos TEXT,
    etymology_text TEXT,
    word TEXT,
    lang TEXT,
    lang_code TEXT,
    id INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS head_templates (
    name TEXT,
    args TEXT,
    expansion TEXT,
    id INTEGER,
    FOREIGN KEY (id) REFERENCES dictionary (id)
);

CREATE TABLE IF NOT EXISTS etymology_templates (
    name TEXT,
    args TEXT,
    expansion TEXT,
    id INTEGER,
    FOREIGN KEY (id) REFERENCES dictionary (id)
);

CREATE TABLE IF NOT EXISTS sounds (
    ipa TEXT,
    audio TEXT,
    text TEXT,
    ogg_url TEXT,
    mp3_url TEXT,
    id INTEGER,
    FOREIGN KEY (id) REFERENCES dictionary (id)
);

CREATE TABLE IF NOT EXISTS senses (
    raw_glosses TEXT,
    synonyms TEXT,
    glosses TEXT,
    id INTEGER,
    FOREIGN KEY (id) REFERENCES dictionary (id)
);