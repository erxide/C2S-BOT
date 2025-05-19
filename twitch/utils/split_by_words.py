"""fonction utils split by words"""
def split_by_words(text, max_length=480):
    """fonction pour split un text par chunks"""
    words = text.split()
    chunks = []
    current = ""

    for word in words:
        if len(current) + len(word) + 1 <= max_length:
            current += (" " if current else "") + word
        else:
            chunks.append(current)
            current = word

    if current:
        chunks.append(current)

    return chunks
