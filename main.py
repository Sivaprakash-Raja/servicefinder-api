import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

area = {
    "Alagappan nagar": {"Arappalayam": 7, "Alagappan nagar": 0, "Koodal nagar": 9, "Narimedu": 8, "K pudur": 11,
                            "Kumaran nagar": 10, "KK nagar": 10, "Avaniyapuram": 4, "Therkuvasal": 5},
    "Arappalayam": {"Arappalayam": 0, "Alagappan nagar": 7, "Koodal nagar": 5, "Narimedu": 4, "K pudur": 8,
                        "Kumaran nagar": 5, "KK nagar": 6, "Avaniyapuram": 8, "Therkuvasal": 6},
    "Koodal nagar": {"Arappalayam": 6, "Alagappan nagar": 9, "Koodal nagar": 0, "Narimedu": 7, "K pudur": 10,
                         "Kumaran nagar":4, "KK nagar": 9, "Avaniyapuram": 12, "Therkuvasal": 9},
    "Narimedu": {"Arappalayam": 4, "Alagappan nagar": 8, "Koodal nagar": 7, "Narimedu": 0, "K pudur": 4,
                     "Kumaran nagar": 3, "KK nagar": 3, "Avaniyapuram": 7, "Therkuvasal": 4},
    "K pudur": {"Arappalayam": 5, "Alagappan nagar": 8, "Koodal nagar": 6, "Narimedu": 2, "K pudur": 0,
                    "Kumaran nagar": 3, "KK nagar": 1, "Avaniyapuram": 7, "Therkuvasal": 4},
    "Kumaran nagar": {"Arappalayam": 4, "Alagappan nagar": 7, "Koodal nagar": 3, "Narimedu": 1, "K pudur": 5,
                          "Kumaran nagar": 0, "KK nagar": 2, "Avaniyapuram": 8, "Therkuvasal": 6},
    "Avaniyapuram": {"Arappalayam": 3, "Alagappan nagar": 1, "Koodal nagar": 7, "Narimedu": 2, "K pudur": 4,
                         "Kumaran nagar": 5, "KK nagar": 6, "Avaniyapuram": 0, "Therkuvasal": 7},
    "KK nagar": {"Arappalayam": 5, "Alagappan nagar": 8, "Koodal nagar": 6, "Narimedu": 3, "K pudur": 1,
                     "Kumaran nagar": 2, "KK nagar": 0, "Avaniyapuram": 7, "Therkuvasal": 4},
    "Therkuvasal": {"Arappalayam": 3, "Alagappan nagar": 5, "Koodal nagar": 8, "Narimedu": 2, "K pudur": 7,
                        "Kumaran nagar": 6, "KK nagar": 4, "Avaniyapuram": 1, "Therkuvasal": 0},
    "Sampatti puram": {"Arappalayam": 1, "Alagappan nagar": 4, "Koodal nagar": 3, "Narimedu": 5, "K pudur": 9,
                           "Kumaran nagar": 6, "KK nagar": 7, "Avaniyapuram": 8, "Therkuvasal": 2},
    "Kalavasal": {"Arappalayam": 0, "Alagappan nagar": 3, "Koodal nagar": 2, "Narimedu": 4, "K pudur": 8,
                      "Kumaran nagar": 5, "KK nagar": 6, "Avaniyapuram": 7, "Therkuvasal": 1},
    "Ponnagaram": {"Arappalayam": 0, "Alagappan nagar": 5, "Koodal nagar": 5, "Narimedu": 1, "K pudur": 5,
                       "Kumaran nagar": 3, "KK nagar": 4, "Avaniyapuram": 6, "Therkuvasal": 2},
    "Kudal nagar": {"Arappalayam": 2, "Alagappan nagar": 1, "Koodal nagar": 0, "Narimedu": 3, "K pudur": 6,
                        "Kumaran nagar": 1, "KK nagar": 4, "Avaniyapuram": 8, "Therkuvasal": 5},
    "Thathaneri": {"Arappalayam": 0, "Alagappan nagar": 7, "Koodal nagar": 2, "Narimedu": 1, "K pudur": 6,
                       "Kumaran nagar": 3, "KK nagar": 4, "Avaniyapuram": 8, "Therkuvasal": 5},
    "Tallakulam": {"Arappalayam": 5, "Alagappan nagar": 8, "Koodal nagar": 7, "Narimedu": 1, "K pudur": 2,
                       "Kumaran nagar": 4, "KK nagar": 0, "Avaniyapuram": 6, "Therkuvasal": 3},
    "Vandiyur": {"Arappalayam": 4, "Alagappan nagar": 7, "Koodal nagar": 8, "Narimedu": 1, "K pudur": 3,
                     "Kumaran nagar": 5, "KK nagar": 0, "Avaniyapuram": 6, "Therkuvasal": 2},
    "Chinthamani": {"Arappalayam": 4, "Alagappan nagar": 3, "Koodal nagar": 7, "Narimedu": 2, "K pudur": 7,
                        "Kumaran nagar": 6, "KK nagar": 5, "Avaniyapuram": 1, "Therkuvasal": 0},
    "S Alangulam": {"Arappalayam": 3, "Alagappan nagar": 7, "Koodal nagar": 3, "Narimedu": 1, "K pudur": 4,
                        "Kumaran nagar": 0, "KK nagar": 2, "Avaniyapuram": 6, "Therkuvasal": 5},
    "Mattuthavani": {"Arappalayam": 5, "Alagappan nagar": 7, "Koodal nagar": 8, "Narimedu": 2, "K pudur": 0,
                         "Kumaran nagar": 3, "KK nagar": 1, "Avaniyapuram": 6, "Therkuvasal": 4},
    "Thiruparankundram": {"Arappalayam": 3, "Alagappan nagar": 0, "Koodal nagar": 4, "Narimedu": 4, "K pudur": 5,
                              "Kumaran nagar": 4, "KK nagar": 4, "Avaniyapuram": 1, "Therkuvasal": 2},
    "Thiru nagar": {"Arappalayam": 3, "Alagappan nagar": 0, "Koodal nagar": 5, "Narimedu": 4, "K pudur": 6,
                        "Kumaran nagar": 5, "KK nagar": 5, "Avaniyapuram": 1, "Therkuvasal": 2},
    "Villapuram": {"Arappalayam": 4, "Alagappan nagar": 2, "Koodal nagar": 8, "Narimedu": 3, "K pudur": 7,
                       "Kumaran nagar": 6, "KK nagar": 5, "Avaniyapuram": 0, "Therkuvasal": 1},
    "Sellur": {"Arappalayam": 2, "Alagappan nagar": 7, "Koodal nagar": 6, "Narimedu": 0, "K pudur": 5,
                   "Kumaran nagar": 1, "KK nagar": 3, "Avaniyapuram": 8, "Therkuvasal": 4},
    "Fathima college": {"Arappalayam": 0, "Alagappan nagar": 6, "Koodal nagar": 1, "Narimedu": 3, "K pudur": 7,
                            "Kumaran nagar": 2, "KK nagar": 4, "Avaniyapuram": 8, "Therkuvasal": 5}

}

def train():

    df=pd.read_csv("Dataset.csv")
    df=df.loc[(df['Availability']=='Available')]

    Location_encoder = LabelEncoder()
    Skillset_encoder = LabelEncoder()

    df['Location_encoder']=Location_encoder.fit_transform(df['Location'])
    df['Skillset_encoder']=Skillset_encoder.fit_transform(df['Skillset'])

    inputs=df.drop(["Availability","Name","Contact no","Location","Skillset","Experience","Customer rating","index"], axis='columns')
    targets=df["index"]
    #model= RandomForestClassifier(n_estimators=100)
    model = tree.DecisionTreeClassifier()
    model.fit(inputs,targets)
    return model,df

def predict(model,loc,ser,df):

    if (loc.lower() == "koodal nagar"):
        lval = 5
    elif (loc.lower() == "arappalayam"):
        lval = 1
    elif (loc.lower() == "kk nagar"):
        lval = 4
    elif (loc.lower() == "alagappa nagar"):
        lval = 0
    elif (loc.lower() == "kumaran nagar"):
        lval = 6
    elif (loc.lower() == "narimedu"):
        lval = 7
    elif (loc.lower() == "k puthur"):
        lval = 3
    elif (loc.lower() == "avaniyapuram"):
        lval = 2
    elif (loc.lower() == "therkuvasal"):
        lval = 8
    else:
        lval=0


    if(ser.lower()=="carpenter"):
        sval=4
    elif (ser.lower() == "plumbing"):
        sval = 2
    elif (ser.lower() == "computer service"):
        sval = 5
    elif (ser.lower() == "ac mechanic"):
        sval = 0
    elif (ser.lower() == "ro water service"):
        sval = 3
    elif (ser.lower() == "house wiring"):
        sval = 1
    else:
        sval =0


    index=model.predict([[lval,sval]])

    result = df.loc[(df['index']==index[0])]
    result = result.drop(['Location_encoder','Skillset_encoder',"index","Availability"], axis='columns')



    return result


def findnow(loc, ser):

    if (area[loc]):
        model, df = train()
        dicts = area[loc]
        dicts = sorted(dicts.items(), key=lambda x: x[1])
        result = []
        for j in range(len(dicts)):
            lis = dicts[j][0]
            result.append(predict(model, lis, ser, df))

        dfs = pd.concat(result)
        dfs = dfs[dfs["Skillset"] == ser]
        dfs = dfs.sort_values(["Experience", "Customer rating"], ascending=False)
        dfs = dfs.drop_duplicates()

        ans = dfs.to_numpy().tolist()

        return ans


    else :
        print("Service not available")

