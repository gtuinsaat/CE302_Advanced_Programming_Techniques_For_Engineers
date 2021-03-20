import random
answers= ['y', 'n']
seqs= ['a', 'nl', 'l', 'n', 'cn', 'cl']
print(33*('*'),"\nHi, Let's get you a new password.\n",(33*('*')))
ncha = int(input("How many characters do you want?"))
if ncha <= 5 or ncha >= 16:
    print('Your password length should be between 6 and 15')
    exit()
print(33*("*"))
sb = str(input('Do you want it to contain big letters? (Type Y for Yes and N for No) '))
if sb.lower() not in answers:
    print('you have to type y or n')
    exit()
print(33*("*"))
sim= str(input('Do you want characters to be sorted simultaneously? (Type Y for Yes and N for No) '))
if sim.lower() not in answers:
    print('you have to type y or n')
    exit()
print(33*("*"))
seq= str(input('Please type shortcode for contents of your password\n'
               '\na= All'
               '\nn= Only Numbers'
               '\nl = Only Letters'
               '\nnl = Numbers and Letters'
               '\ncn = Characters and Numbers'
               '\ncl = Characters and Letters'))
if seq.lower() not in seqs:
    print('you have to type a,nl,l,n,cn,cl')
    exit()
print(33 * (" "))
s_cha= '@ - * + - /'
numbers = '1 2 3 4 5 6 7 8 9 0'
lettersBS = 'A B C D E F G H I J K L M N O P Q R S T U W V X Y Z a b c d e f g h i j k l m n o p r s t u w x y z'
lettersS = 'a b c d e f g h i j k l m n o p q r s t u w v x y z'
num_lettersBS = 'A B C D E F G H I J K L M N O P Q R S T U W V X Y Z a b c d e f g h i j k l m n o p r s t u w x y z 0 1 2 3 4 5 6 7 8 9 '
num_lettersS = 'a b c d e f g h i j k l m n o p q r s t u w v x y z 0 1 2 3 4 5 6 7 8 9'
scha_lettersBS = 'A B C D E F G H I J K L M N O P Q R S T U W V X Y Z a b c d e f g h i j k l m n o p r s t u w x y z @ - * + - / '
scha_lettersS = 'a b c d e f g h i j k l m n o p q r s t u w v x y z @ - * + - /'
scha_numbers = '@ - * + - / 0 1 2 3 4 5 6 7 8 9'
AllBS = '1 2 3 4 5 6 7 8 9 0 A B C D E F G H I J K L M N O P Q R S T U W V X Y Z a b c d e f g h i j k l m n o p r s t u w x y z 1 2 3 4 5 6 7 8 9 @ - * + - / '
AllS = '1 2 3 4 5 6 7 8 9 0 a b c d e f g h i j k l m n o p r s t u w x y z 1 2 3 4 5 6 7 8 9 @ - * + - /'
output=[]
def creator():
    if seq.lower() == 'a':
        while len(output) != ncha:
            if sb.lower() == 'y':
                output.append(random.choice(AllBS.split()))
            else:
                output.append(random.choice(AllS.split()))
        if any(item in numbers.split() for item in output) == False:
            output.clear()
            creator()
        elif any(item in lettersBS.split() for item in output) == False:
            output.clear()
            creator()
        elif any(item in s_cha.split() for item in output) == False:
            output.clear()
            creator()
    if seq.lower() == 'nl':
        while len(output) != ncha:
            if sb.lower() =='y':
                output.append(random.choice(num_lettersBS.split()))
            else: output.append(random.choice(num_lettersS.split()))
        if any(item in numbers.split() for item in output) == False:
            output.clear()
            creator()
        elif any(item in lettersBS.split() for item in output) == False:
            output.clear()
            creator()
    if seq.lower() == 'n':
        while len(output) != ncha:
            output.append(random.choice(numbers.split()))
    if seq.lower() == 'cn':
        while len(output) != ncha:
            output.append(random.choice(scha_numbers.split()))
        if any(item in output for item in s_cha.split() )== False:
            output.clear()
            creator()
        elif any(item in output for item in numbers.split()) == False:
            output.clear()
            creator()
    if seq.lower() == 'cl':
        while len(output) != ncha:
            if sb.lower() == 'y':
                output.append(random.choice(scha_lettersBS.split()))
            else:
                output.append(random.choice(scha_lettersS.split()))
        if any(item in output for item in s_cha.split() )== False:
            output.clear()
            creator()
        if any(item in output for item in lettersBS.split() )== False:
            output.clear()
            creator()
    if seq.lower() == 'l':
        while len(output) != ncha:
            if sb.lower() =='y':
                output.append(random.choice(lettersBS.split()))
            else:
                output.append(random.choice(lettersS.split()))
creator()
print('˅˅˅˅˅˅˅ Here is your password ˅˅˅˅˅˅˅')
if sim.lower() == 'y':
    print(sorted(output))
else:
    print(output)
print('˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄˄')