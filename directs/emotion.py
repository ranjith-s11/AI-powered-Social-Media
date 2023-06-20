import text2emotion as te
dic = {'':0,'Happy':1,'Angry':2,'Surprise':3,'Sad':4,'Fear':5}
def emotion_ratios(text):
    obj = te.get_emotion(text)
    return obj

def find_emotion(text):
    maxy = 0.0
    string =''
    e_r = emotion_ratios(text)
    print(e_r)
    for i in e_r:
        if maxy<e_r[i]:
            maxy=e_r[i]
            string=i

    return dic[string]
    
def text_to_emotion(text):
    emotion = find_emotion(text)
    return emotion


