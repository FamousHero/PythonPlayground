# Based on 'Fluent Python' ch.2 pg. 90-99 (Automatic Handling of Missing Keys & Subclassing UserDict instead of Dict)
import collections 

class MyDict(dict):
    # Auto called by base `dict` class when key is missing in __getitem__
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key] # explicit call to __getitem__ which in-turn calls __missing__
        except KeyError:
            return default
        
    def __contains__(self, key: object) -> bool:
        return str(key) in self.keys()

    def __setitem__(self, key: any, value: any) -> None:
        if isinstance(key, str):
            super().__setitem__(key, value)
        else:
            self[str(key)] = value
        
# Same functionality w/ less lines, UserDict already defines `get` as above
class FpDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key: object) -> bool:
       return str(key) in self. data

    def __setitem__(self, key: any, item: any) -> None:
        self.data[str(key)] = item 


if __name__ == '__main__':

    # Both classes have the same functionality
    # But FpDict is easier to follow and concise

    myDict = MyDict()
    myDict['a'] = 1
    myDict[10] = 'b'
    myDict[3.14] = 'c'
    myDict[True] = 2

    fpDict = FpDict()
    fpDict['a'] = 1
    fpDict[10] = 'b'
    fpDict[3.14] = 'c'
    fpDict[True] = 2
    print('myDict: ', myDict)
    print('fpDict: ', fpDict)
    print(f'{None}')
    print(f"{'myDict':15}| {'fpDict':15}")
    print("-"*50)
    print(f'{str(myDict.get(10)):15}| {str(fpDict.get(10)):15}')
    print(f'{str(myDict.get(90)):15}| {str(fpDict.get(90)):15}')

    print(f'{str(True in myDict):15}| {str(True in fpDict):15}')
    print(f'{str(0 in myDict):15}| {str(0 in fpDict):15}')
    print(f'{str(False in myDict):15}| {str(False in fpDict):15}')
    print(f'{str(3.14 in myDict):15}| {str(3.14 in fpDict):15}')