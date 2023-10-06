# 1
# def display_text():
#     text = """/"Don't let the noise of others' opinions
# drown out your own inner voice."
#                                 Steve Jobs"""
#     print(text)
# display_text()
# 3
def line(l,d,s):
    if d == 'horizontal':
        horizontal_line= l * s
        print(horizontal_line)
    elif d == 'vertical':
        vertical_line= l * s
    print(vertical_line)
line(15, 'horizontal', '-')
line(6, 'vertical', '|')
# 4
# def max_num(a,b,c,d):
#     max_val = max(a,b,c,d)
#     return max_val
# result = max_num(21,5,15,20)
# print('Max number: ', result)