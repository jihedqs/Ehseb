e={
    "Arabe":{
        "Oral":0,
        "Control":0,
        "Synthese":0
    },
    "Français":{
        "Oral":0,
        "Control":0,
        "Synthese":0
    },
    "Anglais":{
        "Oral":0,
        "Control":0,
        "Synthese":0
    },
    "Histoire":{
        "Oral":0,
        "Control":0,
        "Synthese":0
    },
    "Géographie":{
        "Oral":0,
        "Control":0,
        "Synthese":0
    },
    "Philosophie":{
        "Synthese":0
    },
    "Option":{
        "Oral":0,
        "Control":0,
        "Synthese":0
    },
    "Math":{
        "Control":0,
        "Synthese":0
    },
    "Physique":{
        "Control":0,
        "Tp":0,
        "Synthese":0
    },
    "Programmation":{
        "Control":0,
        "Tp":0,
        "Synthese":0
    },
    "S.T.I":{
        "Oral":0,
        "Control":0,
        "Synthese":0
    },
    "Sport":{
        "Control":0,
        "Synthese":0
    }
    
}

cof={
    "Arabe":1,
    "Français":2,
    "Anglais":2,
    "Histoire":1,
    "Géographie":1,
    "Philosophie":1,
    "Option":1,
    "Math":3,
    "Physique":3,
    "Programmation":3,
    "S.T.I":3,
    "Sport":1
    
}
def ValidMark(x):
    return 0<=x<=20


def GetMarks():
    for subject,assessments in e.items():
        print(subject)
        for assessment in assessments:
            mark=float(input(f"{assessment}="))
            while not ValidMark(mark):
                print(mark,"!!!!! please try again")
                mark=float(input(f"{assessment}="))
            e[subject][assessment]=mark

def score():
    score=0
    for subject,assessments in e.items():
        SubScore=0
        i=0
        for assessment,mark in assessments.items():
            if assessment=="Synthese":
                SubScore=round((SubScore+mark*2)/(i+2),2)
                
            else:
                SubScore+=mark
                i+=1
        score+=(SubScore*cof[subject])
    return round(score/22,2)
GetMarks()
print("Notek",score())