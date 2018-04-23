# level1_weight = 1
# level2_weight = 0.5
# level3_weight = 0.25

# EMOTION_TREE = {
#     'love': [{'emotion': 'love', 'connnectedness': 1}],
#     'joy': [{'emotion': 'joy', 'connnectedness': 1}],
#     'surprise': [{'emotion': 'surprise', 'connnectedness': 1}],
#     'sadness': [{'emotion': 'sadness', 'connnectedness': 1}],
#     'fear': [{'emotion': 'fear', 'connnectedness': 1}],
#     'anger': [{'emotion': 'anger', 'connnectedness': 1}],

#     'Affection': [{'emotion': 'love', 'connnectedness': 0.5}],
#     'Adoration': [{'emotion': 'love', 'connnectedness': 0.25}],
#     'Fondness': [{'emotion': 'love', 'connnectedness': 0.25}],
#     'Liking': [{'emotion': 'love', 'connnectedness': 0.25}],
#     'Attraction': [{'emotion': 'love', 'connnectedness': 0.25}],
#     'Caring': [{'emotion': 'love', 'connnectedness': 0.25}],
#     'Tenderness': [{'emotion': 'love', 'connnectedness': 0.25}],
#     'Compassion': [{'emotion': 'love', 'connnectedness': 0.25}],
#     'Sentimentality': [{'emotion': 'love', 'connnectedness': 0.25}],
#     'Lust': [{'emotion': 'love', 'connnectedness': 0.5}],
#     'Desire': [{'emotion': 'love', 'connnectedness': 0.25}],
#     'Passion': [{'emotion': 'love', 'connnectedness': 02.5}],
#     'Infatuation': [{'emotion': 'love', 'connnectedness': 0.25}],
#     'Longing': [{'emotion': 'love', 'connnectedness': 0.5}],

#     'Cheerfulness': [{'emotion': 'joy', 'connnectedness': 0.5}],
#     'Zest': [{'emotion': 'joy', 'connnectedness': 0.5}],
#     'Contentment': [{'emotion': 'joy', 'connnectedness': 0.5}],
#     'Pride': [{'emotion': 'joy', 'connnectedness': 0.5}],
#     'Optimism': [{'emotion': 'joy', 'connnectedness': 0.5}],
#     'Enthrallment': [{'emotion': 'joy', 'connnectedness': 0.5}],
#     'Relief': [{'emotion': 'joy', 'connnectedness': 0.5}],

#     'Amusement': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Bliss': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Gaiety': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Glee': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Jolliness': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Joviality': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Delight': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Enjoyment': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Gladness': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Happiness': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Jubilation': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Elation': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Satisfaction': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Ecstasy': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Euphoria': [{'emotion': 'joy', 'connnectedness': 0.25}],

#     'Enthusiasm': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Zeal': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Excitement': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Thrill': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Exhilaration': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Pleasure': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Triumph': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Eagerness': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Hope': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Rapture': [{'emotion': 'joy', 'connnectedness': 0.25}],
#     'Amazement': [{'emotion': 'surprise', 'connnectedness': 0.25}],
#     'Astonishment': [{'emotion': 'surprise', 'connnectedness': 0.25}],
# }

EMOTION_DICT = {
    'Love':	{
        'Affection': ['Adoration', 'Fondness', 'Liking', 'Attraction',
             'Caring', 'Tenderness', 'Compassion', 'Sentimentalit'],
        'Lust': ['Desire', 'Passion', 'Infatuation'],
        'Longing': ['Longing']
    },
    'Joy': {
        'Zest':	['Enthusiasm', 'Zeal', 'Excitement', 'Thrill', 'Exhilaration'],
        'Contentment':	['Pleasure'],
        'Pride':	['Triumph'],
        'Optimism':	['Eagerness', 'Hope'],
        'Enthrallment':	['Enthrallment', 'Rapture'],
        'Relief':	['Relief'],
        'Cheerfulness': ['Amusement', 'Bliss', 'Gaiety', 'Glee', 'Jolliness',
            'Joviality', 'Joy', 'Delight', 'Enjoyment', 'Gladness',
            'Happiness', 'Jubilation', 'Elation', 'Satisfaction',
            'Ecstasy', 'Euphoria'],

},
    'Surprise': {
        'Surprise': ['Amazement', 'Astonishment']
    },
    'Anger': {
        'Irritability': ['Aggravation', 'Agitation', 'Annoyance', 'Grouchy', 'Grumpy', 'Crosspatch'],
        'Exasperation':	['Frustration'],
        'Rage':	['Anger', 'Outrage', 'Fury', 'Wrath', 'Hostility', 'Ferocity', 'Bitterness', 'Hatred', 'Scorn', 'Spite', 'Vengefulness', 'Dislike', 'Resentment'],
        'Disgust':	['Revulsion', 'Contempt', 'Loathing'],
        'Envy':	['Jealousy'],
        'Torment':	['Torment']
    },
    'Sadness': {
        'Suffering': ['Agony', 'Anguish', 'Hurt'],
        'Sadness':	['Depression', 'Despair', 'Gloom', 'Glumness', 'Unhappiness', 'Grief', 'Sorrow', 'Woe', 'Misery', 'Melancholy'],
        'Disappointment':	['Dismay', 'Displeasure'],
        'Shame':	['Guilt', 'Regret', 'Remorse'],
        'Neglect':	['Alienation', 'Defeatism', 'Dejection', 'Embarrassment', 'Homesickness', 'Humiliation', 'Insecurity', 'Insult', 'Isolation', 'Loneliness', 'Rejection'],
        'Sympathy':	['Pity', 'Mono no aware', 'Sympathy']
    },
'Fear': {
    'Horror':	['Alarm', 'Shock', 'Fear', 'Fright', 'Horror', 'Terror', 'Panic', 'Hysteria', 'Mortification'],
    'Nervousness':	['Anxiety', 'Suspense', 'Uneasiness', 'Apprehension', 'Worry', 'Distress', 'Dread']
}
}

EMOTION_TREE = {}

for l1 in EMOTION_DICT:
    EMOTION_TREE[l1]={
        'emotion': l1,
        'connnectedness': 1
    }
    for l2 in EMOTION_DICT[l1]:
        EMOTION_TREE[l2]={

        }
        for l3 in EMOTION_DICT[l1][l2]:
            EMOTION_TREE[l3]={}

print EMOTION_TREE