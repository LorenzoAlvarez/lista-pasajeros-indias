import re
import pandas as pd


CONSTANT_ENTRY = r"[0-9]([0-9]{1,2}|\.[0-9]{3})?\."

class Parser():

    """
        This class will analyze the text file extracted from the PDF
            and will take the information to save it in an JSON file
    """
    def __init__(self, file_path):
        super().__init__()
        self.filepath = file_path
        self.data = dict()
        self.data["Book"] = list()
        self.data["Entry"] = list()

    def load_file(self, book, type_of_loading="Passengers"):
        """
        This method will load the file and try to make a json file with all
        the information
            @param: the number of the book
            @return: a string function
        """
        entry = ""
        first_entry = True
        with open(self.filepath, "r") as f:
            for line in f:
                if re.search(CONSTANT_ENTRY, line) is not None:
                    if first_entry:
                        first_entry = False
                    else:    
                        # take the data from entry and save it on the dataframe
                        self.data["Book"].append(book)
                        self.data["Entry"].append(entry)
                        entry = ""
                    entry = entry + line
                else:
                    entry = entry + line
        
    def from_dict_to_json(self):
        dataframe = pd.DataFrame(data=self.data)
        print(dataframe.tail())
        dataframe.to_excel("lista.xls", index=None)


if __name__ == "__main__":
    print("Start the script")
    parser = Parser("./vol IV passengers.txt")
    parser.load_file("IV")
    parser.from_dict_to_json()
