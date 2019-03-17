class Apartment:
    def hey_buddy(self, user):
        familyfile = open("family.txt", "r")
        familylist = familyfile.readlines()
        familyfile.close()
        found = False

        for line in familylist:
            if str(user) in line:
                print("[Apartment=>hey_buddy] Found: ", user)
                found = True
                break

        return found

    def kiss_hello(self, user):
        try:
            familyfile = open("family.txt", "a")
            familyfile.write(str(user) + "\n")
            familyfile.close()

            print("[Apartment=>kiss_hello] Added: ", user)
            return True
        except Exception as e:
            print("[Apartment=>kiss_hello] Exception: ", e)
            return False
