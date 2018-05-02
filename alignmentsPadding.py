#First alignment method
print('{0:8} | {1:9}'.format('Hola','Mundo'))
print('{0:8} | {1:9}'.format('This',2))
print('{0:8} | {1:9}'.format('a',3.1))

#Second alignment method
print('\n')
print('{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Center', 'Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

#Padding character
print('\n')
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left', 'Center', 'Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

#Float with precision
print('\n')
print('This is ten-characters, two-decimal number:{0:10.2f}'.format(13.579))
#Other precision DOCTYPE
num = 23.45678
print(f"Ten characters, two decimal is:{num:{10}.{2}}")
