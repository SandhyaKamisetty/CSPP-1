'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    @author : SandhyaKamisetty
    Replace all the special characters(!, @, #, $, %, ^, &, *)
    in a given string with a space.
    Read string from the input, store it in variable str_input.
    '''
    str_input = "ab!@cd"
    a_input = ""
    for i in str_input:
        if i in "!@#$%^&*":
            a_input += " "
        else: 
            a_input += i

if __name__ == "__main__":
    main()
