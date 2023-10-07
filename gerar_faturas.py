import PyPDF2
import os

pdf_file = open('C:/Users/Victor/projetos_git/teste_faturamento/teste3/arquivos_base/boletos.pdf', 'rb')
dados_do_pdf = PyPDF2.PdfFileReader(pdf_file)
for i in range(dados_do_pdf.numPages):
    pagina = dados_do_pdf.getPage(i)
    texto_da_pagina = pagina.extractText()
    mensagem = "boleto-"
    for j in range(len(texto_da_pagina)):
        if texto_da_pagina[j:j+3] == ' 35':
            mensagem += texto_da_pagina[j+1:j+6]
            break
    nome2 = 'C:/Users/Victor/projetos_git/teste_faturamento/teste3/arquivos_base/' + mensagem + '.pdf'
    novo_pdf2 = PyPDF2.PdfFileWriter()
    novo_pdf2.addPage(pagina)
    with open(nome2, 'wb') as novo_pdf_file:
        novo_pdf2.write(novo_pdf_file)


pdf_file = open('C:/Users/Victor/projetos_git/teste_faturamento/teste3/arquivos_base/capas.pdf', 'rb')
dados_do_pdf = PyPDF2.PdfFileReader(pdf_file)

for i in range(dados_do_pdf.numPages):
    pagina = dados_do_pdf.getPage(i)
    texto_da_pagina = pagina.extractText()
    mensagem = "capa-"
    
    for j in range(len(texto_da_pagina)):
        if texto_da_pagina[j-5:j] == ' L 35':
            mensagem += texto_da_pagina[j-2:j+3] + "-"
            break

    for j in range(len(texto_da_pagina)):
        cont = 0
        if texto_da_pagina[j - 8:j] == "- Diaria":
            for k in range(j, len(texto_da_pagina)):
                if texto_da_pagina[k] == " ":
                    cont = cont + 1
                if cont == 2:
                    mensagem += texto_da_pagina[k+1:k+6] 
                    break

    nome2 = 'C:/Users/Victor/projetos_git/teste_faturamento/teste3/arquivos_base/' + mensagem + '.pdf'
    novo_pdf2 = PyPDF2.PdfFileWriter()
    novo_pdf2.addPage(pagina)
    
    with open(nome2, 'wb') as novo_pdf_file:
        novo_pdf2.write(novo_pdf_file)

pdf_file.close()



folder = r'C:/Users/Victor/projetos_git/teste_faturamento/teste3/arquivos_base//'

for file_name in os.listdir(folder):
    if file_name.startswith('nota') and file_name.endswith('.pdf'):
        pdf_file = open(os.path.join(folder, file_name), 'rb')
        dados_do_pdf = PyPDF2.PdfFileReader(pdf_file)
        pagina = dados_do_pdf.getPage(0)
        texto_da_pagina = pagina.extractText()
        texto_da_pagina = texto_da_pagina.encode("utf-8")
        for i in range(5, len(texto_da_pagina)):
            if texto_da_pagina[i - 5:i] == "RPS:":
                print(texto_da_pagina)
                print("RPS: " + texto_da_pagina[i - 5:i - 1])
                print(file_name[-9:-4])
                print(texto_da_pagina[i - 1:i + 4])
                old_name = os.path.join(folder, file_name)
                nome = "nota-" + file_name[-9:-4] + "rps-" + texto_da_pagina[i - 1:i + 4]
                new_name = os.path.join(folder, nome + ".pdf")
                os.rename(old_name, new_name)
        pdf_file.close()

print(os.listdir(folder))


folder = r'C:/Users/Victor/projetos_git/teste_faturamento/teste3/arquivos_base//'

for file_name in os.listdir(folder):
    if file_name.startswith('nota'):
        old_name = folder + file_name
        nome = "nota-"
        pdf_file = open(os.path.join(folder, file_name), 'rb')
        dados_do_pdf = PyPDF2.PdfFileReader(pdf_file)
        pagina = dados_do_pdf.getPage(0)
        texto_da_pagina = pagina.extractText()
        texto_da_pagina.encode("utf-8")
        for i in range(len(texto_da_pagina)):
            if(texto_da_pagina[i-8:i] == 'Numero: '):
                nome += texto_da_pagina[i:i + 5] + "-"
        for i in range(len(texto_da_pagina)):
            if(texto_da_pagina[i-4:i] == 'RPS:'):
                nome += texto_da_pagina[i:i + 5] + ".pdf"
        pdf_file.close()
        new_name = folder + nome
        os.rename(old_name, new_name)    

print(os.listdir(folder))



folder = r'C:/Users/Victor/projetos_git/teste_faturamento/teste3/arquivos_base/'
nome = 'C:/Users/Victor/projetos_git/teste_faturamento/teste3/'

novo_pdf_imprimir = PyPDF2.PdfFileWriter()

for rps in os.listdir(folder):
    if(len(rps) == 9 and rps != 'capas.pdf'):
        for capa in os.listdir(folder):
            if (capa.startswith('capa') and capa[11:16] == rps[0:-4]):
                for boleto in os.listdir(folder):
                    if(boleto.startswith('boleto') and boleto[7:12] == capa[5:10]):
                        for nota in os.listdir(folder): 
                            if(nota.startswith('nota') and nota.endswith('.pdf') and capa[-9:-4] == nota[-9:-4]):
                                caminho_entrada_boleto = os.path.join(folder, boleto)
                                caminho_entrada_capa = os.path.join(folder, capa)
                                caminho_entrada_nota = os.path.join(folder, nota)
                                caminho_entrada_rps = os.path.join(folder, rps)
                                caminho_saida = os.path.join(nome, boleto[7:-4] + '.pdf')
                                novo_pdf = PyPDF2.PdfFileWriter()
                                
                                pdf_entrada_boleto = open(caminho_entrada_boleto, 'rb')
                                pdf_entrada_capa = open(caminho_entrada_capa, 'rb')
                                pdf_entrada_nota = open(caminho_entrada_nota, 'rb')
                                
                                for pdf_entrada in [pdf_entrada_boleto, pdf_entrada_capa, pdf_entrada_nota,caminho_entrada_rps]:
                                    pdf_reader = PyPDF2.PdfFileReader(pdf_entrada)
                                    for i in range(pdf_reader.numPages):
                                        novo_pdf.addPage(pdf_reader.getPage(i))
                                
                                with open(caminho_saida, 'wb') as pdf_saida:
                                    novo_pdf.write(pdf_saida)

                                # Adicione as páginas correspondentes a boleto, capa e nota ao arquivo IMPRIMIR.pdf
                                for pdf_entrada_imprimir in [pdf_entrada_boleto, pdf_entrada_capa, pdf_entrada_nota]:
                                    pdf_reader_imprimir = PyPDF2.PdfFileReader(pdf_entrada_imprimir)
                                    for i in range(pdf_reader_imprimir.numPages):
                                        novo_pdf_imprimir.addPage(pdf_reader_imprimir.getPage(i))

# Salve o arquivo IMPRIMIR.pdf
caminho_saida2 = 'C:/Users/Victor/projetos_git/teste_faturamento/teste3/IMPRIMIR.pdf'
with open(caminho_saida2, 'wb') as pdf_saida2:
    novo_pdf_imprimir.write(pdf_saida2)

'''
Precisa arrumar :
NF - nota + rps
CAPA - rps + fatura
BOLETO - fatura
Doc. Escaneado - rps

'''