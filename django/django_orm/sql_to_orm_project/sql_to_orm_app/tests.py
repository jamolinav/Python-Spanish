import re

frase_en_pdf = 'acompesesituacinntributariadeterceros'
buscar = 'acomp[\w\ \.-]*[\w\ \.-]*ese[\w\ \.-]*situaci[\w\ \.-]*n[\w\ \.-]*tributaria[\w\ \.-]*de[\w\ \.-]*terceros'

encontrados = re.findall(buscar, frase_en_pdf)
for frase in encontrados:
    print(frase)
