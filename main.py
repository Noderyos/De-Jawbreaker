from base64 import b16decode,b32decode,b64decode
import requests
banner = '''
########  ########               ##    ###    ##      ## ########  ########  ########    ###    ##    ## ######## ########  
##     ## ##                     ##   ## ##   ##  ##  ## ##     ## ##     ## ##         ## ##   ##   ##  ##       ##     ## 
##     ## ##                     ##  ##   ##  ##  ##  ## ##     ## ##     ## ##        ##   ##  ##  ##   ##       ##     ## 
##     ## ######   #######       ## ##     ## ##  ##  ## ########  ########  ######   ##     ## #####    ######   ########  
##     ## ##               ##    ## ######### ##  ##  ## ##     ## ##   ##   ##       ######### ##  ##   ##       ##   ##   
##     ## ##               ##    ## ##     ## ##  ##  ## ##     ## ##    ##  ##       ##     ## ##   ##  ##       ##    ##  
########  ########          ######  ##     ##  ###  ###  ########  ##     ## ######## ##     ## ##    ## ######## ##     ##
'''
print(banner)
filename = input("\nName of obfuscated file : ")
with open(filename) as k:
	data = k.read().split('"')[1]
	file2 = b64decode(b32decode(b16decode(data)))
	out = ''.join(str(file2).split(";")).split("'")
	semidecoded = ''.join([h for h in out if len(h) == 1])
	decoded = b64decode(b32decode(b16decode(semidecoded)))
	real = requests.get(str(decoded).split('"')[1]).text
	print("\nDecoded : \n" + real)
	open("de-" + filename,"x").close()
	open("de-" + filename,"w").write(real)
	print("Content saved at de-" + filename)