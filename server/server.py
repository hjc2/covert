# code from https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client

import socket
import pdfcovert

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 7826 # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    i = 1

    while True:

        file = open('file_'+ str(i)+".pdf",'wb')

        receive_data = conn.recv(1024)  # receive response

        while receive_data:
            file.write(receive_data)
            print(receive_data)
            receive_data = conn.recv(1024)
            if b'%EOF' in receive_data:
                file.write(receive_data)
                break
        
        file.close()

        extracted_data = pdfcovert.extract_data_from_pdf('file_'+ str(i)+".pdf")
        print(extracted_data)

        hidden_data = input("Data to send -> ")

        send_pdf_name = input("Name of pdf to send -> ")  # 

        pdfcovert.embed_data_in_pdf(send_pdf_name, "encrypted.pdf", hidden_data)

        pdf = open("encrypted.pdf", "rb")
        send_data = pdf.read(1024)
        while not send_data.__contains__('%%EOF'):
            conn.send(send_data)
            send_data = pdf.read(1024)
        
        pdf.close()

        i += 1

    conn.close()


if __name__ == '__main__':
    server_program()