import json
import datetime
class Test:
    def update_json(self):
        myfile = open('formdb/b6696258d08d5655583df8a54e80df3d.json', 'r')
        data = json.load(myfile)
        myfile.close()

        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        data[-1]["value"] = time
        myfile2 = open('formdb/b6696258d08d5655583df8a54e80df3d.json', 'w')
        json.dump(data, myfile2, indent=4, ensure_ascii=False)
        myfile2.close()
        print(data)
        pass


if __name__ == "__main__":
    test = Test()
    test.update_json()
