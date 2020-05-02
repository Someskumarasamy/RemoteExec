import json

class CommonUtils:

    def getJSONFromPath(self, filepath):
        try :
            data = json.load(filepath)
            return data
        except : 
            raise Exception("The give file has invalid data format")
            return None
