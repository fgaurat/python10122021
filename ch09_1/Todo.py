

class Todo:

    def __init__(self,id,userId,title,completed) -> None:
        self._id = id
        self._userId = userId
        self._title = title
        self._completed = completed
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        self._id = id

    @property
    def userId(self):
        return self._userId
    
    @userId.setter
    def userId(self,userId):
        self._userId = userId
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        self._title = title

    @property
    def completed(self):
        return self._completed
    
    @completed.setter
    def completed(self,completed):
        self._completed = completed

    def __str__(self) -> str:
        return f"{__class__.__name__} title={self._title}"

    def __repr__(self) -> str:
        return repr(self.__str__())