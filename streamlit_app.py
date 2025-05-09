import streamlit as st

st.markdown('''
## :blue[Blue] Prince Numerical Core :red[Decoder]

Type in the input box all four-character words from the message to be decoded. (Separate words by spaces)
''')

#"PIGS SAND MAIL DATE HEAD CLAM PEAK HEAT JOYA WELL TOAD CARD WILL TAPE LEGS TREE ROAD MAID SLAB ROCK HAND VASE SAFE CLAY TOES"
text_input = str(st.text_input("👇","AREA LEEK EACH DOCK FACE CALM SNUG PERK IDOL PIGS LACK JEST DUNE CLOG BALM WELD OBEY HAIR FILE OMEN NOOK MADE GRUB NAME FLOC"))

if st.button("Click to Decode", type="primary"):
    word_list= text_input.split()
    message = []
    error= []
    decoded_message = ''
    flag=False
    typo=False
    for word in word_list:
        if len(word)!=4:
            message = []
            typo=True
            st.write("Please, type ONLY :red[four-character] words separated by spaces in the input box\n (Check for typo)")
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
        count=0
        for num in result:
            if num.is_integer() and num > 0 and num <= 27:
                count+=1
                min_num.append(num)

        if count==0:
            flag=True
            error.append(word)

        if len(min_num)>0:
            message.append(min(min_num))

    if len(message)>0:
        for i, letter in enumerate(message):
            if i%5==0 and i!=0:
                decoded_message += ' '
            decoded_message += chr(int(letter)+96)
    
    if len(decoded_message)>0:
        st.write("Decoded message:\n> ",decoded_message)
    elif not typo and not flag:
        st.write("Please, type the four-characters words in the input box.")

    if flag:
        st.write("Some of the words typed :red[do not] have definitive numeric core: " + str(error))
