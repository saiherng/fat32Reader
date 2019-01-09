/* Author: Diesburg
 *
 * This is a test program to show you how we can remove spaces from
 * file and directory names in C.  In this program, I open up the 
 * fat32.img file, seek to a directory entry in which I know there
 * are spaces in the name, remove the spaces, and add the . and file
 * extension on the end. 
 *
 * Feel free to copy and use the remove_spaces function in your programs.
 */ 

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>

void remove_spaces(char *name);

int main() {
	
	int fd;
	char name[12] = {0};


	fd = open("fat32.img",O_RDWR);

	lseek(fd,0x100440,SEEK_SET);

	read(fd,name,11);

	printf("[%s]\n", name);

	remove_spaces(name);
	
	printf("[%s]\n", name);

	close(fd);

	return 0;
}

void remove_spaces(char *name)
{
	char newName[12] = {0};

	int i;
	int j;

	for (i=0;i<8;i++) {
		if(name[i] != 0x20) {
			newName[i]=name[i];
		}
		else {
			break;
		}

	}

	/* i is where we need to start writing */
	if(name[8] != 0x20){
		newName[i] = '.';
		i++;
		for (j=8; j<11; j++){
			newName[i] = name[j];
			i++;
		}
	}
	printf("Name is %s\n", name);
	printf("newname is %s\n", newName);

	strcpy(name,newName);
}

	

	
	

	 
