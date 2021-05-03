"""import json
import pickle
import numpy as np


class abc:
    def __init__(self):
        self.__locations = None
        self.__data_columns = None
        self.__model = None

    def get_estimated_price(self,location, sqft, bhk, bath):
        try:
            loc_index = self.__data_columns.index(location.lower())
        except Exception:
            loc_index = -1

        x = np.zeros(len(self.__data_columns))
        x[0] = sqft
        x[1] = bhk
        x[2] = bath
        
        if loc_index >= 0:
            x[loc_index] = 1
        return round(self.__model.predict([x])[0], 2)

    def get_location_names(self):
        return self.__locations

    def load_saved_artifacts(self):
        print("Loading saved artifacts.. Start..")

        with open("./artifacts/columns.json", "r") as f:
            self. __data_columns = json.load(f)['data_columns']
            self.__locations = self.__data_columns[3:]

        with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f:
            self. __model = pickle.load(f)


if __name__=="__main__":
    obj = abc()
    obj.load_saved_artifacts()
    print(obj.get_location_names())
    print(obj.get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(obj.get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(obj.get_estimated_price('1st Phase JP Nagar', 1200, 3, 3))
    print(obj.get_estimated_price('Kalhalli', 1000, 2, 2)) #other location
    print(obj.get_estimated_price('Ejipura', 1000, 2, 2)) #other location

"""

import json
import pickle
import numpy as np


class abc:
    def __init__(self):
        self.__locations = None
        self.__data_columns = None
        self.__model = None

    def get_estimated_price(self,location, sqft, bhk, bath):
        try:
            loc_index = self.__data_columns.index(location.lower())
        except Exception:
            loc_index = -1

        x = np.zeros(len(self.__data_columns))
        x[0] = sqft
        x[1] = bhk
        x[2] = bath
        
        if loc_index >= 0:
            x[loc_index] = 1
        return round(self.__model.predict([x])[0], 2)

    def get_location_names(self):
        return self.__locations

    def load_saved_artifacts(self):
        print("Loading saved artifacts.. Start..")

       # with open("C:\\Code\\BHP\\server\\artifacts\\columns.json", "r") as f:
        self. __data_columns = json.loads('{"data_columns": ["total_sqft", "bath", "bhk", "1st block jayanagar", "1st phase jp nagar", "2nd phase judicial layout", "2nd stage nagarbhavi", "5th block hbr layout", "5th phase jp nagar", "6th phase jp nagar", "7th phase jp nagar", "8th phase jp nagar", "9th phase jp nagar", "aecs layout", "abbigere", "akshaya nagar", "ambalipura", "ambedkar nagar", "amruthahalli", "anandapura", "ananth nagar", "anekal", "anjanapura", "ardendale", "arekere", "attibele", "beml layout", "btm 2nd stage", "btm layout", "babusapalaya", "badavala nagar", "balagere", "banashankari", "banashankari stage ii", "banashankari stage iii", "banashankari stage v", "banashankari stage vi", "banaswadi", "banjara layout", "bannerghatta", "bannerghatta road", "basavangudi", "basaveshwara nagar", "battarahalli", "begur", "begur road", "bellandur", "benson town", "bharathi nagar", "bhoganhalli", "billekahalli", "binny pete", "bisuvanahalli", "bommanahalli", "bommasandra", "bommasandra industrial area", "bommenahalli", "brookefield", "budigere", "cv raman nagar", "chamrajpet", "chandapura", "channasandra", "chikka tirupathi", "chikkabanavar", "chikkalasandra", "choodasandra", "cooke town", "cox town", "cunningham road", "dasanapura", "dasarahalli", "devanahalli", "devarachikkanahalli", "dodda nekkundi", "doddaballapur", "doddakallasandra", "doddathoguru", "domlur", "dommasandra", "epip zone", "electronic city", "electronic city phase ii", "electronics city phase 1", "frazer town", "gm palaya", "garudachar palya", "giri nagar", "gollarapalya hosahalli", "gottigere", "green glen layout", "gubbalala", "gunjur", "hal 2nd stage", "hbr layout", "hrbr layout", "hsr layout", "haralur road", "harlur", "hebbal", "hebbal kempapura", "hegde nagar", "hennur", "hennur road", "hoodi", "horamavu agara", "horamavu banaswadi", "hormavu", "hosa road", "hosakerehalli", "hoskote", "hosur road", "hulimavu", "isro layout", "itpl", "iblur village", "indira nagar", "jp nagar", "jakkur", "jalahalli", "jalahalli east", "jigani", "judicial layout", "kr puram", "kadubeesanahalli", "kadugodi", "kaggadasapura", "kaggalipura", "kaikondrahalli", "kalena agrahara", "kalyan nagar", "kambipura", "kammanahalli", "kammasandra", "kanakapura", "kanakpura road", "kannamangala", "karuna nagar", "kasavanhalli", "kasturi nagar", "kathriguppe", "kaval byrasandra", "kenchenahalli", "kengeri", "kengeri satellite town", "kereguddadahalli", "kodichikkanahalli", "kodigehaali", "kodigehalli", "kodihalli", "kogilu", "konanakunte", "koramangala", "kothannur", "kothanur", "kudlu", "kudlu gate", "kumaraswami layout", "kundalahalli", "lb shastri nagar", "laggere", "lakshminarayana pura", "lingadheeranahalli", "magadi road", "mahadevpura", "mahalakshmi layout", "mallasandra", "malleshpalya", "malleshwaram", "marathahalli", "margondanahalli", "marsur", "mico layout", "munnekollal", "murugeshpalya", "mysore road", "ngr layout", "nri layout", "nagarbhavi", "nagasandra", "nagavara", "nagavarapalya", "narayanapura", "neeladri nagar", "nehru nagar", "ombr layout", "old airport road", "old madras road", "padmanabhanagar", "pai layout", "panathur", "parappana agrahara", "pattandur agrahara", "poorna pragna layout", "prithvi layout", "r.t. nagar", "rachenahalli", "raja rajeshwari nagar", "rajaji nagar", "rajiv nagar", "ramagondanahalli", "ramamurthy nagar", "rayasandra", "sahakara nagar", "sanjay nagar", "sarakki nagar", "sarjapur", "sarjapur  road", "sarjapura - attibele road", "sector 2 hsr layout", "sector 7 hsr layout", "seegehalli", "shampura", "shivaji nagar", "singasandra", "somasundara palya", "sompura", "sonnenahalli", "subramanyapura", "sultan palaya", "tc palaya", "talaghattapura", "thanisandra", "thigalarapalya", "thubarahalli", "thyagaraja nagar", "tindlu", "tumkur road", "ulsoor", "uttarahalli", "varthur", "varthur road", "vasanthapura", "vidyaranyapura", "vijayanagar", "vishveshwarya layout", "vishwapriya layout", "vittasandra", "whitefield", "yelachenahalli", "yelahanka", "yelahanka new town", "yelenahalli", "yeshwanthpur"]}')['data_columns']
        self.__locations = self.__data_columns[3:]

        with open("C:\\Code\\BHP\\server\\artifacts\\banglore_home_prices_model.pickle", "rb") as f:
            self. __model = pickle.load(f)


if __name__=="__main__":
    obj = abc()
    obj.load_saved_artifacts()
    print(obj.get_location_names())
    print(obj.get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(obj.get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(obj.get_estimated_price('1st Phase JP Nagar', 1200, 3, 3))
    print(obj.get_estimated_price('Kalhalli', 1000, 2, 2)) #other location
    print(obj.get_estimated_price('Ejipura', 1000, 2, 2)) #other location

