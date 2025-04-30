import streamlit as st

st.markdown('''
## :blue[Blue] Prince Numerical Core :red[Decoder]

Type in the input box all four-digit words from the message to be decoded. (Separate words by spaces)
''')

#"PIGS SAND MAIL DATE HEAD CLAM PEAK HEAT JOYA WELL TOAD CARD WILL TAPE LEGS TREE ROAD MAID SLAB ROCK HAND VASE SAFE CLAY TOES"
text_input = str(st.text_input("👇","AREA PEAK EACH MAIL FACE CLAM VASE WELL IDOL PIGS LACK JEST MAID CLOG ROCK WELD OBEY HAIR FILE OMEN NOOK SAFE GRUB JOYA TOES"))

if st.button("Click to Decode", type="primary"):
    word_list= text_input.split()

    skip=False
    flag=False
    message = []
    decoded_message = ''
    for word in word_list:
        if len(word)!=4:
            skip=True
            decoded_message = ''
            break
        output = []
        for character in word.lower():
            number = ord(character) - 96
            output.append(number)

        result =[]
        result.append(((output[0]-output[1])*output[2])/output[3])
        result.append(((output[0]-output[1])/output[2])*output[3])
        result.append(((output[0]*output[1])-output[2])/output[3])
        result.append(((output[0]*output[1])/output[2])-output[3])
        result.append(((output[0]/output[1])-output[2])*output[3])
        result.append(((output[0]/output[1])*output[2])-output[3])

        min_num=[]
        for num in result:
            if num.is_integer() and num > 0:
                min_num.append(num)
            else:
                flag=True
                min_num.append(32)
        
        message.append(min(min_num))

    if not skip:
        for i, letter in enumerate(message):
            if i%5==0 and i!=0:
                decoded_message += ' '
            decoded_message += chr(int(letter)+96)
    
    if len(decoded_message)>0 and not flag:
        st.write("Decoded message:\n> ",decoded_message)
    elif skip:
        skip=False
        flag=False
        st.write("Please, type ONLY :red[four-digit] words separated by spaces in the input box\n (Check for typo)")
    elif flag:
        skip=False
        flag=False
        st.write("Decoded message:\n> ",decoded_message)
        st.write("Some of the words typed :red[do not] have definitive numeric core.")
    else:
        st.write("Please, type the four-digit words in the input box.")
