def count_words(text):

    count = 0
    words = text.split()
    for word in words:
        count +=1
    return count

def char_count(text):
    norm_text = text.lower()
    result = {}
    for c in norm_text:
        
        if c not in result:
            result[c] = 0
        
        result [c] += 1

    return result