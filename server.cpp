//socket includes
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <iostream>

//i found some information about how this works here: http://www.cplusplus.com/forum/articles/13355/
int main(int argc, char *argv[])
{
    //Create a socket with the socket() system call
    socklen_t clilen;	//moeten we nog opzoeken
    struct sockaddr_in serv_addr, cli_addr;	//moet noet uitgezet
    int n;    // return value of read and write?? iets
	
    if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }
     else {
        std::cout << "argc =" << argc << "argv =" << argv[0] << "\n";
        sleep(5);
     }
     
    auto sockfd = socket(AF_INET, SOCK_STREAM, 0);
     if (sockfd < 0) 
     {
        perror("ERROR opening socket");
        exit(2);
     }
	bzero((char *) &serv_addr, sizeof(serv_addr)); //zet alles in server_addr naar 0. for infor on sizeof see: https://en.cppreference.com/w/cpp/language/sizeof
    auto portno = atoi(argv[1]);	//poort argument van int naar string
    
    //The variable serv_addr is a structure of type struct sockaddr_in. This structure has four fields. The first field is short sin_family, which contains a code for the address family. It should always be set to the symbolic constant AF_INET.
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);
    if (bind(sockfd, (struct sockaddr *) &serv_addr,sizeof(serv_addr)) < 0)
		{
			perror("ERROR on binding");
            exit(1);
        }
    listen(sockfd,5);
    clilen = sizeof(cli_addr); 
    auto newsockfd = accept(sockfd,(struct sockaddr *) &cli_addr, &clilen);
	if (newsockfd < 0)
	{
		perror("ERROR on accept");
		exit(3);
	}
    //char buffer[256];	//buffer voor read and write;
    char buffer[256];
	bzero(buffer,sizeof(buffer));
	n = read(newsockfd,buffer,255);
	if (n < 0) 
	{
		perror("Error reading from socket");
		exit(4);
	}
	printf("Here is the message: %s\n",buffer);
	n = write(newsockfd,"I got your message",18);
	if (n < 0) 
	{
		perror("Error reading from socket");
		exit(5);
	}	
     close(newsockfd);
     close(sockfd);
     return 0;	
}
