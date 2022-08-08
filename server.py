# Programmer: Sina Fathi-Kazerooni
# Email: sina@sinafathi.com
# WWW: sinafathi.com 

from searchapp import searchapp

if __name__ == "__main__":
    searchapp.run(host="0.0.0.0", port=int("8080"), debug=True)
