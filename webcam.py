import cv2





def chamarCamera():
   #Abrindo camera padrão
    cap = cv2.VideoCapture(0)

    #Definindo codec e criando o objeto video

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
       #Capturando quadro a quadro
       ret, frame = cap.read()

       if ret == True:
           frame = cv2.flip(frame, 0)

           out.write(frame)
           cv2.imshow('Camera de Gravacao', frame)
           if cv2.waitKey(1) & 0xFF == ord('q'):
            break
           
    cap.release()
    out.release()
    cv2.destroyAllWindows()

       
       



if __name__ == "__main__":
    while True:
        print("SISTEMA DE CAMERA")
        selecao_de_opcao = input("1- Para ativar a camera;\n2-Para sair da camera\n")

        if selecao_de_opcao == "1":
            chamarCamera()
        elif selecao_de_opcao =="2":
           print("Programa Finalizado")
           break