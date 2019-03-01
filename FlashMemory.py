class FlashMemory:
    def save(name, data):
        f = open(name+'.json', 'w')
        f.write(str(data))
        f.close()
        print("saved: "+str(data)) # TODO: remove print
    def restore(name):
        f = open(name+'.json', 'r')
        data = f.read()
        f.close()
        print("restored: "+str(data)) # TODO: remove print
        return data
