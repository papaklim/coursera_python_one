class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, "r") as f:
                parse_file = f.read()
                return parse_file
        except IOError:
            return ""




# def main():
#     file = FileReader(r"C:\Users\papak\Desktop\text.tx1t")
#     print(file.read())
#
#
# if __name__ == "__main__":
#     main()
#
