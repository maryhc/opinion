file_name = "tweets.txt"
file_name_mod = file_name.replace(".txt","")
file_name_mod = file_name_mod + "m.txt"
mod_file = open(file_name_mod,"w")

raw_file = open(file_name,"r+")

for x in raw_file:
	xf = x.replace("!","")
	xf = x.replace("ñ","n")
	mod_file.write(xf)
print(x)
print(xf)
