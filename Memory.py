class Memory:
    def save(data):
        f = open('data.txt', 'w')
        f.write(str(data))
        f.close()
        print("saved: "+str(data))
    def restore():
        f = open('data.txt', 'r')
        data = f.read()
        f.close()
        print("restored: "+str(data))
        return data
