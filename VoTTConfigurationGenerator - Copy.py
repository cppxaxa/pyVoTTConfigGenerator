import json

class VoTTConfiguration:
    def CreateDummy(self):
        self.frames = {
            "0": [
                        {
                            "x1": 63,
                            "y1": 10,
                            "x2": 199,
                            "y2": 388,
                            "id": 0,
                            "width": 263,
                            "height": 396,
                            "type": "Rectangle",
                            "tags": [
                                    "person"
                                  ],
                            "name": 1                            
                        }
                ],
            "1": [
                        {
                            "x1": 42,
                            "y1": 5,
                            "x2": 192,
                            "y2": 396,
                            "id": 1,
                            "width": 257,
                            "height": 396,
                            "type": "Rectangle",
                            "tags": [
                                    "person",
                                  "girl"
                                  ],
                            "name": 1                            
                        }
                ]
        }
        self.framerate = "1"
        self.inputTags = "person,girl,hand-raised-person"
        self.suggestiontype = "track"
        self.scd = False
        self.visitedFrames = [0,1]
    
    def GetJson(self):
        return json.dumps(self.__dict__)