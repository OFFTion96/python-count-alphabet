import sys
import re

class Sanitizer:
    def readData(self):
        text_concat = ""
        with open(sys.argv[1],'r') as f:
            text = f.read()
            text_concat = text_concat + text
        return text_concat

    def countAlphabet(self,text):
        text = text.lower()
        self.__text_count = {}
        self.text = text
        self.text = re.sub(r"\s+", '__', self.text)
      
        self.num_text_tab = re.findall('[a-z]*([^_]*__)',self.text)
        self.text_alphabet = re.findall('[a-z]',self.text)
        for tx in self.text_alphabet:
            self.__text_count[tx] = self.__text_count.get(tx,0) + 1
        self.__text_count.update({"__":len(self.num_text_tab)})
        return self.__text_count


if __name__ =='__main__':

    text_sanitizer = Sanitizer()
    read_text = text_sanitizer.readData()
    alphabet_count = text_sanitizer.countAlphabet(read_text)
    print(alphabet_count)