"""
Fix double-encoded UTF-8 files.

PowerShell Get-Content -Raw read UTF-8 files as Windows cp1252,
then WriteAllText re-encoded as UTF-8-with-BOM, corrupting non-ASCII chars.

Recovery: for each Unicode char in the corrupted text:
  - Try cp1252 encode -> get original byte
  - If cp1252 undefined, use latin-1 -> get original byte
  - Then decode the reassembled bytes as UTF-8
"""
import pathlib

ROOT = pathlib.Path('d:/Fragments/Zelda/Ultrabroken Documentation/ultrabroken-documentation')

def degrade_char(c):
    n = ord(c)
    if n < 0x80:
        return bytes([n])
    try:
        return c.encode('cp1252')
    except (UnicodeEncodeError, LookupError):
        try:
            return c.encode('latin-1')
        except (UnicodeEncodeError, LookupError):
            return c.encode('utf-8')

def fix_encoding(text):
    raw = bytearray()
    for c in text:
        raw.extend(degrade_char(c))
    return raw.decode('utf-8')

glitchcraft = ROOT / 'docs/wiki/glitchcraft'
fixed_count = 0
bom_stripped = 0

for md in sorted(glitchcraft.glob('*.md')):
    raw = md.read_bytes()
    if not raw.startswith(b'\xef\xbb\xbf'):
        continue  # wasn't touched by the PowerShell script

    text = raw[3:].decode('utf-8')

    try:
        fixed = fix_encoding(text)
    except UnicodeDecodeError as e:
        print(f'DECODE ERROR {md.name}: {e}')
        continue

    if fixed != text:
        for i, (ol, fl) in enumerate(zip(text.splitlines(), fixed.splitlines())):
            if ol != fl:
                print(f'{md.name}:{i+1}')
                print(f'  WAS: {ol}')
                print(f'  NOW: {fl}')
        fixed_count += 1
        md.write_text(fixed, encoding='utf-8')
    else:
        # Same content but BOM stripped
        bom_stripped += 1
        md.write_text(text, encoding='utf-8')

print(f'\nEncoding-fixed: {fixed_count}, BOM-only stripped: {bom_stripped}')
