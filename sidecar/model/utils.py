import re


def to_url_name(s):
    """
    Convert a string to match the conventions for URL names and titles. E.g.
    all lowercase, only alphanumeric characters, separated by hyphens.
    """
    if type(s) == str:
        raise ValueError("Need to be called with a unicode string!")
    # Transliterate accented unicode characters to the base character.  Not all
    # characters can be transliterated, so fallback to simple replacement.
    try:
        s = s.encode('ascii', 'transliterate')
    except UnicodeEncodeError:
        s = s.encode('ascii', 'replace')
    # Convert CamelCaseStrings to Camel Case Strings.
    s = re.sub(r'([a-z])([A-Z])', '\g<1> \g<2>', s)
    # Just eliminate apostrophes.
    s = re.sub(r'\'', '', s)
    # Convert & to and.
    s = re.sub(r'&', 'and', s)
    # Make lowercase and convert non-URLString chars to spaces.
    s = re.sub('[^a-z0-9\ \-]', ' ', s.lower())
    # Strip and convert whitespace blocks to hyphens.
    s = re.sub('\s+', '-', s.strip())
    return s
