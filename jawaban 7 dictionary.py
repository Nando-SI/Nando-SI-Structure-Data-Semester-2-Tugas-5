engToSp = {"one":"uno", "two":"dos", "three":"tres"} # membuat dictionary dengan nama engToSp
print(engToSp["dos"]) # mengakses nilai dengan key "dos" pada dictionary engToSp
# output: KeyError: 'dos'
# karena "dos" bukanlah key dalam dictionary engToSp, melainkan nilai/value dari key "two"
# dapat diperbaiki dengan mengakses nilai dengan key "two" pada dictionary engToSp, yaitu engToSp["two"] yang hasilnya adalah "dos"