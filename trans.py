import pandas as pd

en_to_ar={
    "start": {
        "1": ["1"],
        "2": ["أ","2", "إ", "ء", "آ"],
        "3": ["ع","3"],
        "4":["4"],
        "5": ["خ","5"],
        "6": ["6"],
        "7": ["ح","7"],
        "8": ["8","ق"],
        "9": ["9","ق"],
        "2a": ["أ"],
        "2e": ["ء"],
        "2i": ["إ"],
        "2o": ["أ"],
        "2u": ["أ"],
        "3'": ["غ"],
        "3'a": ["غ"],
        "3'e": ["غ"],
        "3'i": ["غ"],
        "3'o": ["غ"],
        "3'u": ["غ"],
        "3a": ["ع"],
        "3e": ["ع"],
        "3i": ["ع"],
        "3o": ["ع"],
        "3u": ["ع"],
        "5a": ["خ"],
        "5e": ["خ"],
        "5i": ["خ"],
        "5o": ["خ"],
        "5u": ["خ"],
        "6'": ["ظ"],
        "6'a": ["ظ"],
        "6'e": ["ظ"],
        "6'i": ["ظ"],
        "6'o": ["ظ"],
        "6'u": ["ظ"],
        "6a": ["ط"],
        "6e": ["ط"],
        "6i": ["ط"],
        "6o": ["ط"],
        "6u": ["ط"],
        "7'": ["خ"],
        "7'a": ["خ"],
        "7'e": ["خ"],
        "7'i": ["خ"],
        "7'o": ["خ"],
        "7'u": ["خ"],
        "7a": ["ح"],
        "7e": ["ح"],
        "7i": ["ح"],
        "7o": ["ح"],
        "7u": ["ح"],
        "8a": ["ق"],
        "8e": ["ق"],
        "8i": ["ق"],
        "8o": ["ق"],
        "8u": ["ق"],
        "9'": ["ض"],
        "9'a": ["ض"],
        "9'e": ["ض"],
        "9'i": ["ض"],
        "9'o": ["ض"],
        "9'u": ["ض"],
        "9a": ["ص", "ق"],
        "9e": ["ص", "ق"],
        "9i": ["ص", "ق"],
        "9o": ["ص", "ق"],
        "9u": ["ص", "ق"],
        "a": ["ا", "أ"],
        "b": ["ب"],
        "ba": ["ب"],
        "be": ["ب"],
        "bi": ["ب"],
        "bo": ["ب"],
        "bu": ["ب"],
        "ch": ["ش"],
        "cha": ["ش"],
        "che": ["ش"],
        "chi": ["ش"],
        "cho": ["ش"],
        "chu": ["ش"],
        "d": ["د", "ض"],
        "da": ["د", "ض"],
        "de": ["د", "ض"],
        "dh": ["ذ", "ظ"],
        "dha": ["ذ", "ظ"],
        "dhe": ["ذ", "ظ"],
        "dhi": ["ذ", "ظ"],
        "dho": ["ذ", "ظ"],
        "dhu": ["ذ", "ظ"],
        "di": ["د", "ض"],
        "dj": ["ج"],
        "dja": ["ج"],
        "dje": ["ج"],
        "dji": ["ج"],
        "djo": ["ج"],
        "dju": ["ج"],
        "do": ["د", "ض"],
        "du": ["د", "ض"],
        "e": ["ا", "إ"],
        "f": ["ف"],
        "fa": ["ف"],
        "fe": ["ف"],
        "fi": ["ف"],
        "fo": ["ف"],
        "fu": ["ف"],
        "g":  ["ج", "ق", "ك"],
        "ga": ["ج", "ق", "ك"],
        "ge": ["ج", "ق", "ك"],
        "gi": ["ج", "ق", "ك"],
        "go": ["ج", "ق", "ك"],
        "gu": ["ج", "ق", "ك"],
        "gh": ["غ"],
        "gha": ["غ"],
        "ghe": ["غ"],
        "ghi": ["غ"],
        "gho": ["غ"],
        "ghu": ["غ"],
        "h": ["ه"],
        "ha": ["ه"],
        "he": ["ه"],
        "hi": ["ه"],
        "ho": ["ه"],
        "hu": ["ه"],
        "i": ["ى", "ي"],
        "ia": ["ي"],
        "ie": ["ي"],
        "ii": ["ي"],
        "io": ["ي"],
        "iu": ["ي"],
        "j": ["ج"],
        "ja": ["ج"],
        "je": ["ج"],
        "ji": ["ج"],
        "jo": ["ج"],
        "ju": ["ج"],
        "k": ["ك"],
        "ka": ["ك"],
        "ke": ["ك"],
        "ki": ["ك"],
        "ko": ["ك"],
        "ku": ["ك"],
        "cu": ["ك"],
        "ca": ["ك"],
        "co": ["ك"],
        "c": ["ك"],
        "kh":  ["خ"],
        "kha": ["خ"],
        "khe": ["خ"],
        "khi": ["خ"],
        "kho": ["خ"],
        "khu": ["خ"],
        "l":  ["ل"],
        "la": ["ل"],
        "le": ["ل"],
        "li": ["ل"],
        "lo": ["ل"],
        "lu": ["ل"],
        "m":  ["م"],
        "ma": ["م"],
        "me": ["م"],
        "mi": ["م"],
        "mo": ["م"],
        "mu": ["م"],
        "n":  ["ن"],
        "na": ["ن"],
        "ne": ["ن"],
        "ni": ["ن"],
        "no": ["ن"],
        "nu": ["ن"],
        "o":  ["أ"],
        "p":  ["ب"],
        "pa": ["ب"],
        "pe": ["ب"],
        "pi": ["ب"],
        "po": ["ب"],
        "pu": ["ب"],
        "q":  ["ق"],
        "qa": ["ق"],
        "qe": ["ق"],
        "qi": ["ق"],
        "qo": ["ق"],
        "qu": ["ق"],
        "r":  ["ر"],
        "ra": ["ر"],
        "re": ["ر"],
        "ri": ["ر"],
        "ro": ["ر"],
        "ru": ["ر"],
        "s":  ["س", "ص", "ث"],
        "sa": ["س", "ص", "ث"],
        "se": ["س", "ص", "ث"],
        "si": ["ث", "س", "ص"],
        "so": ["ث", "س", "ص"],
        "su": ["ث", "س", "ص"],
        "sh":  ["ش"],
        "sha": ["ش"],
        "she": ["ش"],
        "shi": ["ش"],
        "sho": ["ش"],
        "shu": ["ش"],
        "t":  ["ت", "ط"],
        "ti": ["ت", "ط"],
        "to": ["ت", "ط"],
        "tu": ["ت", "ط"],
        "ta": ["ت", "ط"],
        "te": ["ت", "ط"],
        "t'":  ["ظ"],
        "t'a": ["ظ"],
        "t'e": ["ظ"],
        "t'i": ["ظ"],
        "t'o": ["ظ"],
        "t'u": ["ظ"],
        "th":  ["ث", "ذ"],
        "tha": ["ث", "ذ"],
        "the": ["ث", "ذ"],
        "thi": ["ث", "ذ"],
        "tho": ["ث", "ذ"],
        "thu": ["ث", "ذ"],
        "u":  ["و"],
        "ua": ["و"],
        "ue": ["و"],
        "ui": ["و"],
        "uo": ["و"],
        "uu": ["و"],
        "w":  ["و"],
        "wa": ["و"],
        "we": ["و"],
        "wi": ["و"],
        "wo": ["و"],
        "wu": ["و"],
        "y": ["ي", "ى"],
        "ya": ["ي"],
        "ye": ["ي"],
        "yi": ["ي"],
        "yo": ["ي"],
        "yu": ["ي"],
        "z":  ["ز", "ذ", "ظ"],
        "za": ["ز", "ذ", "ظ"],
        "ze": ["ز", "ذ", "ظ"],
        "zi": ["ز", "ذ", "ظ"],
        "zo": ["ز", "ذ", "ظ"],
        "zu": ["ز", "ذ", "ظ"]
    },
    "other": {
        "1": ["1"],
        "2": ["أ","2", "إ", "ء", "آ", "ؤ", "ئ", "ق"],
        "3": ["ع","3"],
        "4":["4"],
        "5": ["خ","5"],
        "6": ["ط","6"],
        "7": ["ح","7"],
        "8": ["8","ق"],
        "9": ["9","ق"],
        "2a": ["أ"],
        "2e": ["ء"],
        "2i": ["إ"],
        "2o": ["أ"],
        "2u": ["أ"],
        "3'": ["غ"],
        "3'a": ["غ"],
        "3'e": ["غ"],
        "3'i": ["غ"],
        "3'o": ["غ"],
        "3'u": ["غ"],
        "3a": ["ع"],
        "3e": ["ع"],
        "3i": ["ع"],
        "3o": ["ع"],
        "3u": ["ع"],
        "5a": ["خ"],
        "5e": ["خ"],
        "5i": ["خ"],
        "5o": ["خ"],
        "5u": ["خ"],
        "6'": ["ظ"],
        "6'a": ["ظ"],
        "6'e": ["ظ"],
        "6'i": ["ظ"],
        "6'o": ["ظ"],
        "6'u": ["ظ"],
        "6a": ["ط"],
        "6e": ["ط"],
        "6i": ["ط"],
        "6o": ["ط"],
        "6u": ["ط"],
        "7'": ["خ"],
        "7'a": ["خ"],
        "7'e": ["خ"],
        "7'i": ["خ"],
        "7'o": ["خ"],
        "7'u": ["خ"],
        "7a": ["ح"],
        "7e": ["ح"],
        "7i": ["ح"],
        "7o": ["ح"],
        "7u": ["ح"],
        "8a": ["ق"],
        "8e": ["ق"],
        "8i": ["ق"],
        "8o": ["ق"],
        "8u": ["ق"],
        "9'": ["ض"],
        "9'a": ["ض"],
        "9'e": ["ض"],
        "9'i": ["ض"],
        "9'o": ["ض"],
        "9'u": ["ض"],
        "9a": ["ص", "ق"],
        "9e": ["ص", "ق"],
        "9i": ["ص", "ق"],
        "9o": ["ص", "ق"],
        "9u": ["ص", "ق"],
        "a": [ "ا", "ة"],
        "ah": ["ه", "ة"],
        "ai": ["ى", "ي", "ي"],
        "ao": ["ه", "ي", "ة"],
        "au": ["ه", "ي", "ة"],
        "b": ["ب"],
        "ba": ["ب"],
        "be": ["ب"],
        "bi": ["ب"],
        "bo": ["ب"],
        "bu": ["ب"],
        "ch": ["ش"],
        "cha": ["ش"],
        "che": ["ش"],
        "chi": ["ش"],
        "cho": ["ش"],
        "chu": ["ش"],
        "d": ["د", "ض"],
        "da": ["د", "ض"],
        "de": ["د", "ض"],
        "dh": ["ذ", "ظ"],
        "dha": ["ذ", "ظ"],
        "dhe": ["ذ", "ظ"],
        "dhi": ["ذ", "ظ"],
        "dho": ["ذ", "ظ"],
        "dhu": ["ذ", "ظ"],
        "di": ["د", "ض"],
        "dj": ["ج"],
        "dja": ["ج"],
        "dje": ["ج"],
        "dji": ["ج"],
        "djo": ["ج"],
        "dju": ["ج"],
        "do": ["د", "ض"],
        "du": ["د", "ض"],
        "e": ["ا", "ه", "ة"],
        "eea": ["ي"],
        "eee": ["ي"],
        "eei": ["ي"],
        "eeo": ["ي"],
        "eeu": ["ي"],
        "eh": ["ه", "ة"],
        "eia": ["ي"],
        "eie": ["ي"],
        "eii": ["ي"],
        "eio": ["ي"],
        "eiu": ["ي"],
        "f": ["ف"],
        "fa": ["ف"],
        "fe": ["ف"],
        "fi": ["ف"],
        "fo": ["ف"],
        "fu": ["ف"],
        "g":  ["ج", "ق", "ك"],
        "ga": ["ج", "ق", "ك"],
        "ge": ["ج", "ق", "ك"],
        "gi": ["ج", "ق", "ك"],
        "go": ["ج", "ق", "ك"],
        "gu": ["ج", "ق", "ك"],
        "gh": ["غ"],
        "gha": ["غ"],
        "ghe": ["غ"],
        "ghi": ["غ"],
        "gho": ["غ"],
        "ghu": ["غ"],
        "h": ["ه"],
        "ha": ["ه"],
        "he": ["ه"],
        "hi": ["ه"],
        "ho": ["ه"],
        "hu": ["ه"],
        "i": ["ى", "ي"],
        "ia": ["ي"],
        "ie": ["ي"],
        "ii": ["ي"],
        "io": ["ي"],
        "iu": ["ي"],
        "j": ["ج"],
        "ja": ["ج"],
        "je": ["ج"],
        "ji": ["ج"],
        "jo": ["ج"],
        "ju": ["ج"],
        "k": ["ك"],
        "ka": ["ك"],
        "ke": ["ك"],
        "ki": ["ك"],
        "ko": ["ك"],
        "ku": ["ك"],
        "cu": ["ك"],
        "ca": ["ك"],
        "co": ["ك"],
        "c": ["ك"],
        "kh":  ["خ"],
        "kha": ["خ"],
        "khe": ["خ"],
        "khi": ["خ"],
        "kho": ["خ"],
        "khu": ["خ"],
        "l":  ["ل"],
        "la": ["ل"],
        "le": ["ل"],
        "li": ["ل"],
        "lo": ["ل"],
        "lu": ["ل"],
        "m":  ["م"],
        "ma": ["م"],
        "me": ["م"],
        "mi": ["م"],
        "mo": ["م"],
        "mu": ["م"],
        "n":  ["ن"],
        "na": ["ن"],
        "ne": ["ن"],
        "ni": ["ن"],
        "no": ["ن"],
        "nu": ["ن"],
        "o":  ["و"],
        "oa": ["و"],
        "oe": ["و"],
        "oi": ["و"],
        "oo": ["و"],
        "ou": ["و"],
        "ooa": ["و"],
        "ooe": ["و"],
        "ooi": ["و"],
        "ooo": ["و"],
        "oou": ["و"],
        "oua": ["و"],
        "oue": ["و"],
        "oui": ["و"],
        "ouo": ["و"],
        "ouu": ["و"],
        "p":  ["ب"],
        "pa": ["ب"],
        "pe": ["ب"],
        "pi": ["ب"],
        "po": ["ب"],
        "pu": ["ب"],
        "q":  ["ق"],
        "qa": ["ق"],
        "qe": ["ق"],
        "qi": ["ق"],
        "qo": ["ق"],
        "qu": ["ق"],
        "r":  ["ر"],
        "ra": ["ر"],
        "re": ["ر"],
        "ri": ["ر"],
        "ro": ["ر"],
        "ru": ["ر"],
        "s":  ["س", "ص", "ث"],
        "sa": ["س", "ص", "ث"],
        "se": ["س", "ص", "ث"],
        "si": ["ث", "س", "ص"],
        "so": ["ث", "س", "ص"],
        "su": ["ث", "س", "ص"],
        "sh":  ["ش"],
        "sha": ["ش"],
        "she": ["ش"],
        "shi": ["ش"],
        "sho": ["ش"],
        "shu": ["ش"],
        "t":  ["ت", "ط"],
        "ti": ["ت", "ط"],
        "to": ["ت", "ط"],
        "tu": ["ت", "ط"],
        "ta": ["ت", "ط"],
        "te": ["ت", "ط"],
        "t'":  ["ظ"],
        "t'a": ["ظ"],
        "t'e": ["ظ"],
        "t'i": ["ظ"],
        "t'o": ["ظ"],
        "t'u": ["ظ"],
        "th":  ["ث", "ذ"],
        "tha": ["ث", "ذ"],
        "the": ["ث", "ذ"],
        "thi": ["ث", "ذ"],
        "tho": ["ث", "ذ"],
        "thu": ["ث", "ذ"],
        "u":  ["و"],
        "ua": ["و"],
        "ue": ["و"],
        "ui": ["و"],
        "uo": ["و"],
        "uu": ["و"],
        "w":  ["و"],
        "wa": ["و"],
        "we": ["و"],
        "wi": ["و"],
        "wo": ["و"],
        "wu": ["و"],
        "y": ["ي", "ى"],
        "ya": ["ي"],
        "ye": ["ي"],
        "yi": ["ي"],
        "yo": ["ي"],
        "yu": ["ي"],
        "z":  ["ز", "ذ", "ظ"],
        "za": ["ز", "ذ", "ظ"],
        "ze": ["ز", "ذ", "ظ"],
        "zi": ["ز", "ذ", "ظ"],
        "zo": ["ز", "ذ", "ظ"],
        "zu": ["ز", "ذ", "ظ"]
    }
}

def transliterate_word(english):
  ret = set()

  def recur(letters, word, start=False):
    if len(letters) == 0:
      ret.add(word)
      return
    if start:
      table = en_to_ar['start']
    else:
      table = en_to_ar['other']
    max_key_len = len(max(list(table), key=len))
    for i in range(1, max_key_len + 1):
      l = letters[:i]
      if l in table:
        for ar in table[l]:
          recur(letters[i:], word + ar)

  recur(english, '', True)
  return ret

nbr=[]
for i in range(18,78):
    nbr=nbr+[str(i)]

stemm=pd.read_excel('New_Stemming.xlsx')
stemmin=stemm['نصايب'].tolist()+stemm['نصاوب'].tolist()+stemm['نصوب'].tolist()+stemm['نصيب'].tolist()+stemm['نسايب'].tolist()+stemm['نسيب'].tolist()+stemm['نساوب'].tolist()+stemm['نسوب'].tolist()+stemm['Unnamed: 8'].tolist()+stemm['Unnamed: 9'].tolist()+stemm['Unnamed: 10'].tolist()+stemm['Unnamed: 11'].tolist()+stemm['Unnamed: 12'].tolist()+stemm['Unnamed: 13'].tolist()+stemm['Unnamed: 14'].tolist()+stemm['Unnamed: 15'].tolist()+stemm['Unnamed: 16'].tolist()+stemm['Unnamed: 17'].tolist()+stemm['Unnamed: 18'].tolist()
stemming = [x for x in stemmin if pd.isnull(x) == False]
stemming=stemming+['نصايب','نصاوب','نصوب','نصيب','نسايب','نسيب','نساوب','نسوب']+nbr
noise=pd.read_excel('new_noise.xlsx')
noise=noise[0].tolist()
def transliterate_ar(eng):
    k=[]
    s=transliterate_word(eng)
    s = list(s)
    for i in s:
        if i in stemming:
            k=k+[i]
    if len(k)==0:
        for i in s:
            if i in noise:
                k = k + [i]
    if len(k)==0:
        k=s
    return k[0]


def transliterate(sentence):
    words = sentence.split()
    klma = ''
    for word in words:
        klma = klma + transliterate_ar(word) + ' '

    return klma
