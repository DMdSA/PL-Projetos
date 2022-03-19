class emdRecord:

    __slots__ = ["_id", "_date", "_name", "_surname", "_age", "_gender", "_address", "_modality", "_email", "_federated", "_medicalResult"]

    def __init__(self, argsList):

        if(len(argsList) != 13):            ## each line has 13 parameters
            raise ValueError

        self._id = argsList[0]
        self._date = argsList[2]
        self._name = argsList[3]
        self._surname = argsList[4]
        self._age = argsList[5]
        self._gender = argsList[6]
        self._address = argsList[7]
        self._modality = argsList[8]
        self._email = argsList[10]
        self._federated = argsList[11]
        self._medicalResult = argsList[12]
    
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @id.deleter
    def id(self):
        del self._id


    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @date.deleter
    def date(self):
        del self._date


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


    @property
    def surname(self):
        return self._surname
        
    @surname.setter
    def surname(self, value):
        self._surname = value

    @surname.deleter
    def surname(self):
        del self._surname


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        
    @age.deleter
    def age(self):
        del self._age


    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @gender.deleter
    def gender(self):
        del self._gender


    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @address.deleter
    def address(self):
        del self._address


    @property
    def modality(self):
        return self._modality

    @modality.setter
    def modality(self, value):
        self._modality = value

    @modality.deleter
    def modality(self):
        del self._modality


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @email.deleter
    def email(self):
        del self._email


    @property
    def federated(self):
        return self._federated

    @federated.setter
    def federated(self, value):
        self._federated = value

    @federated.deleter
    def federated(self):
        del self._federated


    @property
    def medicalResult(self):
        return self._medicalResult

    @medicalResult.setter
    def medicalResult(self, value):
        self._medicalResult = value
        
    @medicalResult.deleter
    def medicalResult(self):
        del self._medicalResult
    
    
    def __str__(self):

        a = "ID::[{}], Date::[{}], Name::[{}], Surname::[{}], Age::[{}], Gender::[{}], Address::[{}], Modality::[{}], Email::[{}], Federated::[{}], MedicalResult::[{}]".format(self._id, self._date, self._name, self._surname, self._age, self._gender, self._address, self._modality, self._email, self._federated, self._medicalResult)
        return a
