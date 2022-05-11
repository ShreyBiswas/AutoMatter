message_text = "Text messaging, or texting, is the act of composing and sending electronic messages, typically consisting of alphabetic and numeric characters, between two or more users of mobile devices, desktops/laptops, or another type of compatible computer. Text messages may be sent over a cellular network, or may also be sent via an Internet connection. The term originally referred to messages sent using the Short Message Service (SMS). It has grown beyond alphanumeric text to include multimedia messages using the Multimedia Messaging Service (MMS) containing digital images, videos, and sound content, as well as ideograms known as emoji (happy faces, sad faces, and other icons), and instant messenger applications (usually the term is used when on mobile devices)."
file_text = "In computing, plain text is a loose term for data (e.g. file contents) that represent only characters of readable material but not its graphical representation nor other objects (floating-point numbers, images, etc.). It may also include a limited number of 'whitespace' characters that affect simple arrangement of text, such as spaces, line breaks, or tabulation characters (although tab characters can 'mean' many different things, so are hardly 'plain'). Plain text is different from formatted text, where style information is included; from structured text, where structural parts of the document such as paragraphs, sections, and the like are identified; and from binary files in which some portions must be interpreted as binary objects (encoded integers, real numbers, images, etc.). The term is sometimes used quite loosely, to mean files that contain only 'readable' content (or just files with nothing that the speaker doesn't prefer). For example, that could exclude any indication of fonts or layout (such as markup, markdown, or even tabs); characters such as curly quotes, non-breaking spaces, soft hyphens, em dashes, and/or ligatures; or other things. In principle, plain text can be in any encoding, but occasionally the term is taken to imply ASCII. As Unicode-based encodings such as UTF-8 and UTF-16 become more common, that usage may be shrinking. Plain text is also sometimes used only to exclude 'binary' files: those in which at least some parts of the file cannot be correctly interpreted via the character encoding in effect. For example, a file or string consisting of 'hello' (in whatever encoding), following by 4 bytes that express a binary integer that is not just a character(s), is a binary file, not plain text by even the loosest common usages. Put another way, translating a plain text file to a character encoding that uses entirely different numbers to represent characters does not change the meaning (so long as you know what encoding is in use), but for binary files such a conversion does change the meaning of at least some parts of the file."



#* Cleaning text
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

def remove_nonletter(text):
    def is_letter(char):
        return char.lower() if char.isalpha() or char==' ' else ''
    return ''.join(list(map(is_letter,text)))
    

def stem(word):
    return stemmer.stem(word)


def words_to_ngram_vector(text, n=1):
    text = list(map(stem,remove_nonletter(text).split(' ')))
    vec = {}
    for word in range(len(text)-n+1):
        ngram = tuple(text[word:word+n])
        try: 
            vec[ngram]+=1
        except:
            vec[ngram]=1
    return vec

# cosine similarity 
from math import acos,pi

def magnitude(vec):
    return (sum([i**2 for i in vec]))**0.5

def cosine_similarity(vec1,vec2): # returns angle between vectors
    if len(list(vec1.keys())[0])!=len(list(vec2.keys())[0]):
        raise ValueError(f'Vectors do not have matching n-gram length: Vec1: {len(list(vec1.keys())[0])}, Vec2: {len(list(vec2.keys())[0])}')

    total = 0

    for word in vec1.keys(): # dot product of a and b
        if word in vec2.keys():
            total += (vec1[word]*vec2[word])

    total /= (magnitude(vec1.values())*magnitude(vec2.values()))

    return acos(total)


def angle_to_percentage_similarity(angle,decimals=2):
    return round((1-(angle/pi)*2)*100,decimals)



a =  words_to_ngram_vector(message_text,n=1)
b = words_to_ngram_vector(file_text,n=1)

print(cosine_similarity(a,b))
print(angle_to_percentage_similarity(cosine_similarity(a,b)))